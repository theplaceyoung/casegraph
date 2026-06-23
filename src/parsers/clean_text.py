import re


def normalize_title(line_text: str) -> str:
    """
    짧은 제목이나 헤더에서
    '공 정 거 래 위 원 회' -> '공정거래위원회'
    같은 형태를 정리한다.
    """

    line_text = line_text.strip()

    # 너무 긴 문장은 건드리지 않음
    if len(line_text) > 50:
        return line_text

    # 한글 사이 공백 제거
    line_text = re.sub(
        r'(?<=[가-힣])\s+(?=[가-힣])',
        '',
        line_text
    )

    # 숫자 사이 공백 제거
    line_text = re.sub(
        r'(?<=\d)\s+(?=\d)',
        '',
        line_text
    )

    return line_text


def clean_text(text: str) -> str:
    """
    전체 markdown 텍스트 정리
    """

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = normalize_title(line)

        # 양쪽 공백 제거
        line = line.strip()

        cleaned_lines.append(line)

    # 빈 줄 3개 이상 → 2개
    result = "\n".join(cleaned_lines)

    result = re.sub(r"\n{3,}", "\n\n", result)

    return result