def read_code_file(file_path: str) -> str:
    """读取本地代码文件，返回文本内容"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"错误：文件 {file_path} 不存在"
    except Exception as e:
        return f"读取文件失败：{str(e)}"
