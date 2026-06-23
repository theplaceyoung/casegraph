import re

LAW_KEYWORDS = [
    "가맹사업법",
    "표시광고법",
    "독점규제법",
    "약관법"
]

COURTS = [
    "대법원",
    "서울고등법원"
]

MONEY_PATTERN = r"[\d,]+원"


def extract_entities(doc):

    entities = []

    if doc["기관"]:
        entities.append(("기관", doc["기관"]))

    if doc["피심인"]:
        entities.append(("회사", doc["피심인"]))

    if doc["사건명"]:
        entities.append(("사건", doc["사건명"]))

    full_text = "\n".join([
        doc["주문"],
        doc["이유"],
        doc["기초사실"],
        doc["처분"],
        doc["결론"]
    ])

    # 법률
    for law in LAW_KEYWORDS:
        if law in full_text:
            entities.append(("법률", law))

    # 법원
    for court in COURTS:
        if court in full_text:
            entities.append(("법원", court))

    # 금액
    amounts = set(re.findall(MONEY_PATTERN, full_text))

    for amount in amounts:
        entities.append(("금액", amount))

    return entities