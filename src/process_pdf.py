from src.converters.pdf_to_md import convert_pdf
from src.parsers.clean_text import clean_text
from src.parsers.ftc_parser import parse_ftc_document
from src.extractors.entity_extractor import extract_entities
from src.graph.graph_builder import build_graph


def process_pdf(pdf_path):

    md_path = convert_pdf(pdf_path)

    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    text = clean_text(text)

    doc = parse_ftc_document(text)

    entities = extract_entities(doc)

    graph = build_graph(
        doc,
        entities
    )

    return graph