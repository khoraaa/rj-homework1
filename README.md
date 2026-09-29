# 代码解析 Agent
> 基于智谱GLM-4-Flash大模型实现的Python代码智能解析工具。
> 课程大作业项目 | 使用Python开发，uv包管理器

## 1. 项目简介
本项目实现一个本地代码解析Agent，读取本地Python源代码文件，调用智谱大模型API，自动完成代码分析。
程序会输出：代码整体功能、逐段逻辑解释、变量含义、输入输出说明、代码优缺点评价。

### 项目目标
简化代码阅读成本，输入`.py`文件名称即可自动生成结构化的代码解读文档。

## 2. 技术栈
- 编程语言：Python 3.10+
- 大模型：智谱 GLM-4-Flash（免费API）
- API SDK：openai兼容接口
- 环境变量管理：python-dotenv
- 包管理工具：uv

## 3. 项目目录结构

code_explain_agent/
├── main.py              # 程序主入口，代码读取 + API 调用逻辑
├── test_code.py         # 测试样例代码
├── .env.example         # 环境变量模板（提交到仓库，不含真实密钥）
├── .gitignore           # Git 忽略配置，保护密钥与本地缓存
└── README.md            # 项目说明文档


## 4. 环境部署与安装
### 前置条件
1. 本地已安装Python 3.10 及以上版本
2. 安装uv工具
3. 智谱开放平台账号，创建API Key

### 步骤1：拉取项目代码
powershell
git clone https://github.com/你的用户名/code_explain_agent.git
cd code_explain_agent

### 步骤 2：创建虚拟环境

uv venv

### 步骤 3：安装项目依赖

uv pip install openai python-dotenv

## 5. API 密钥配置

1. 将 `.env.example` 文件复制一份，重命名为 `.env`
2. 登录【智谱 AI 开放平台】，新建 API Key，复制完整密钥
3. 在 `.env` 填入密钥

ZHIPU_API_KEY=在此粘贴你的智谱完整API密钥

## 6. 运行方式

在项目根目录终端执行：

uv run python main.py

1. 根据提示，输入需要解析的 Python 文件名，例如：`test_code.py`
2. 程序读取本地代码文件，调用 GLM-4-Flash 模型
3. 在控制台打印完整代码解析报告

## 7. 模块设计说明

### 7.1 文件读取模块 `read_code_file(filename)`

- 接收文件名参数，读取本地`.py`文件
- 异常捕获：文件不存在、编码读取异常，返回错误提示文本

### 7.2 大模型调用模块 `explain_code(code_text)`

- 构造 Prompt，将源代码送入 GLM-4-Flash
- 设定固定输出格式，强制模型从 5 个维度解析代码
- 返回模型生成的代码分析结果

### 7.3 主程序入口

- 控制台交互，接收用户输入文件名
- 调用文件读取函数，判断读取结果
- 正常读取后调用大模型接口，打印解析结果

## 8. 程序示例运行效果

===== 代码解析Agent =====
请输入要解析的代码文件名(例如 test_code.py)：test_code.py
正在调用大模型解析，请稍等...

===== 代码解析结果 =====
1. 整体功能：该程序定义加法函数，对两个数字求和并打印结果
2. 逐段代码逻辑解释：
……

## 9. 注意事项

1. 智谱 API 密钥**仅新建弹窗瞬间展示完整字符串**，网页列表截断的片段无法使用；密钥泄露请立即在平台删除旧密钥并新建。
2. `.env` 文件已经写入 `.gitignore`，不会被 Git 提交上传，保护个人 API 凭证。
3. GLM-4-Flash 免费模型存在调用额度、频率限制，大量连续调用会触发限流。
4. 网络需要能够访问智谱 API 地址，网络不通会造成请求失败。