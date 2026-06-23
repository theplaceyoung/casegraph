import re


def normalize_title(line_text: str) -> str:

    line_text = line_text.strip()

    if len(line_text) > 50:
        return line_text

    line_text = re.sub(
        r'(?<=[가-힣])\s+(?=[가-힣])',
        '',
        line_text
    )

    line_text = re.sub(
        r'(?<=\d)\s+(?=\d)',
        '',
        line_text
    )

    return line_text

def normalize_headers(text):

    replacements = {
        "사\n건\n명": "사건명",
        "피\n심\n인": "피심인",
        "주\n문": "주문",
        "이\n유": "이유"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def clean_text(text: str):
    
    text = normalize_headers(text)

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = normalize_title(line)
        line = line.strip()

        cleaned_lines.append(line)

    result = "\n".join(cleaned_lines)

    result = re.sub(r"\n{3,}", "\n\n", result)

    return result