from src.converters.pdf_to_md import convert_all_pdfs
from src.parsers.ftc_parser import parse_ftc_document
from src.extractors.entity_extractor import extract_entities
from src.graph.graph_builder import build_graph, save_graph


if __name__ == "__main__":
    convert_all_pdfs()


with open(md_path, encoding="utf-8") as f:
    text = f.read()

doc = parse_ftc_document(text)

entities = extract_entities(doc)

graph = build_graph(
    doc,
    entities
)

save_graph(
    graph,
    "generated/graph.json"
)