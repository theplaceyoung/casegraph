import json
import uuid
from datetime import datetime

def build_graph(doc, entities):

    nodes = []
    edges = []

    node_ids = set()

    def add_node(node_id, node_type, extra_data=None):

        if not node_id:
            return

        if node_id in node_ids:
            return

        data = {
            "id": node_id,
            "label": node_id,
            "type": node_type
        }

        if extra_data:
            data.update(extra_data)

        nodes.append({
            "data": data
        })

        node_ids.add(node_id)

    company = doc.get("피심인")
    agency = doc.get("기관")

    add_node(
        agency,
        "기관",
        {
            "case_name": doc.get("사건명")
        }
    )
    add_node(
        company,
        "회사",
        {
            "case_name": doc.get("사건명"),

            "order": doc.get("주문"),

            "reason": doc.get("이유"),

            "facts": doc.get("기초사실"),

            "decision": doc.get("결론")
        }
    )
    if agency and company:
        edges.append({
        "data": {
            "id": str(uuid.uuid4()),
            "source": agency,
            "target": company,
            "label": "의결"
        }
    })

    for entity_type, entity_name in entities:

        if entity_name == company:
                continue
            
        add_node(entity_name, entity_type)

        if company:
            edges.append({
                "data": {
                    "id": str(uuid.uuid4()),
                    "source": company,
                    "target": entity_name,
                    "label": entity_type
                }
            })


    return {

        "casegraph_version": "0.1.0",

        "generated_at":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "source_file":
            doc.get("filename"),

        "case_name":
            doc.get("사건명"),

        "nodes": nodes,

        "edges": edges

    }


def save_graph(graph, output_path):

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            graph,
            f,
            ensure_ascii=False,
            indent=2
        )