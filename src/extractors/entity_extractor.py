import re


LAW_PATTERN = r".+법"
MONEY_PATTERN = r"[\d,]+원"


def extract_entities(doc):

    entities = []

    if doc["기관"]:
        entities.append(
            ("기관", doc["기관"])
        )

    if doc["피심인"]:
        entities.append(
            ("회사", doc["피심인"])
        )

    if doc["사건명"]:
        entities.append(
            ("사건", doc["사건명"])
        )

    full_text = "\n".join([
        doc["주문"],
        doc["이유"],
        doc["기초사실"],
        doc["처분"],
        doc["결론"]
    ])

    laws = set(re.findall(LAW_PATTERN, full_text))

    for law in laws:
        entities.append(
            ("법률", law)
        )

    amounts = set(re.findall(MONEY_PATTERN, full_text))

    for amount in amounts:
        entities.append(
            ("금액", amount)
        )

    return entities