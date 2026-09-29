import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载.env里面的API密钥
load_dotenv()
api_key = os.getenv("ZHIPU_API_KEY")

# 智谱大模型接口地址
base_url = "https://open.bigmodel.cn/api/paas/v4/"

# 创建客户端
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def read_code_file(filename):
    """
    文件读取模块：读取本地代码文件，捕获异常
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"【错误】文件不存在：{filename}"
    except Exception as e:
        return f"【读取异常】{str(e)}"

def explain_code(code_text):
    """
    大模型调用模块：发送代码给GLM-4-Flash，返回代码解析结果
    """
    prompt = f"""
请详细解析下面这段Python源代码：
1. 整体实现的功能
2. 逐段代码逻辑解释
3. 变量含义
4. 输入与输出说明
5. 简单评价代码优缺点

代码内容：
{code_text}
"""
    response = client.chat.completions.create(
        model="glm-4-flash",  # 免费模型
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print("===== 代码解析Agent =====")
    fname = input("请输入要解析的代码文件名(例如 test_code.py)：")
    print("正在调用大模型解析，请稍等...\n")

    code_content = read_code_file(fname)
    # 判断读取是否出错
    if code_content.startswith("【"):
        print(code_content)
    else:
        result = explain_code(code_content)
        print("===== 代码解析结果 =====")
        print(result)
