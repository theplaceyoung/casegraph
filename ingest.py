from src.converters.pdf_to_md import convert_all_pdfs
from src.parsers.ftc_parser import parse_ftc_document
from src.extractors.entity_extractor import extract_entities
from src.graph.graph_builder import build_graph, save_graph
from src.parsers.clean_text import clean_text
from pathlib import Path


if __name__ == "__main__":
    convert_all_pdfs()


    for md_path in Path("markdown").glob("*.md"):

        with open(md_path, encoding="utf-8") as f:
            text = f.read()
            
        text = clean_text(text)

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
    
    graph = process_pdf(
        "raw/의결서_귀한사람들.pdf"
    )

    save_graph(
        graph,
        "generated/graph.json"
    )