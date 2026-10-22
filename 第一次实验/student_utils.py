
def parse_student(line):
    """将一行 name,score 解析为字典；无效记录抛出 ValueError。"""
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}")

    name = parts[0].strip()
    score_text = parts[1].strip()

    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩必须为整数，当前为 {score_text!r}") from None

    if not 0 <= score <= 100:
        raise ValueError(f"成绩必须在 0 到 100 之间，当前为 {score}")

    return {"name": name, "score": score}
