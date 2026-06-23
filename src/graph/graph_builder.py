import json


def build_graph(doc, entities):

    nodes = []
    edges = []

    node_set = set()

    def add_node(node_id, node_type):

        if node_id in node_set:
            return

        nodes.append({
            "data": {
                "id": node_id,
                "label": node_id,
                "type": node_type
            }
        })

        node_set.add(node_id)

    agency = doc["기관"]
    company = doc["피심인"]

    add_node(agency, "기관")
    add_node(company, "회사")

    edges.append({
        "data": {
            "source": agency,
            "target": company,
            "label": "의결"
        }
    })

    for entity_type, entity_name in entities:

        add_node(entity_name, entity_type)

        edges.append({
            "data": {
                "source": company,
                "target": entity_name,
                "label": entity_type
            }
        })

    return {
        "nodes": nodes,
        "edges": edges
    }


def save_graph(graph, path):

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            graph,
            f,
            ensure_ascii=False,
            indent=2
        )