import re


SECTION_HEADERS = [
    "주문",
    "이유",
    "기초사실",
    "처분",
    "결론"
]


def extract_field(text, field_name):
    pattern = rf"{field_name}\s*\n(.*?)(?=\n\S)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return ""


def extract_section(text, start_header, end_headers=None):

    if end_headers is None:
        end_headers = []

    end_pattern = "|".join(end_headers)

    if end_pattern:
        pattern = rf"{start_header}(.*?)(?={end_pattern}|$)"
    else:
        pattern = rf"{start_header}(.*)"

    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()

    return ""


def parse_ftc_document(text):

    result = {}

    result["기관"] = "공정거래위원회"
    
    m = re.search(
    r"사건명\s*(.*?)\s*피심인",
    text,
    re.DOTALL
    )
    result["사건명"] = m.group(1).strip() if m else ""


    m = re.search(
        r"피심인\s*(.*?)\s*심의종결일",
        text,
        re.DOTALL
    )
    result["피심인"] = m.group(1).split("\n")[0].strip() if m else ""

    m = re.search(r"제\d{4}\s*[–-]\s*\d+호", text)
    result["의결번호"] = m.group(0) if m else ""

    m = re.search(r"\d{4}\.\s*\d+\.\s*\d+", text)
    result["의결일"] = m.group(0) if m else ""

    result["사건번호"] = extract_field(text, "사건번호")

    result["주문"] = extract_section(
        text,
        "주문",
        ["이유"]
    )

    result["이유"] = extract_section(
        text,
        "이유",
        ["기초사실"]
    )

    result["기초사실"] = extract_section(
        text,
        "기초사실",
        ["처분"]
    )

    result["처분"] = extract_section(
        text,
        "처분",
        ["결론"]
    )

    result["결론"] = extract_section(
        text,
        "결론"
    )
    print("피심인 =", result["피심인"])
    print("사건명 =", result["사건명"])
    return result