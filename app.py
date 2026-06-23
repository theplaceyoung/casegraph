from flask import Flask, send_from_directory, request, jsonify

from src.process_pdf import process_pdf
from src.graph.graph_builder import save_graph

import os

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(
        "src/viewer",
        "index.html"
    )


@app.route("/upload", methods=["POST"])
def upload():

    os.makedirs(
    "uploads",
    exist_ok=True
    )

    os.makedirs(
        "generated",
        exist_ok=True
    )

    file = request.files["pdf"]

    filename = file.filename

    path = "uploads/tmp.pdf"

    file.save(path)

    graph = process_pdf(
        path,
        filename
    )

    save_graph(
        graph,
        "generated/graph.json"
    )

    return jsonify(
        {
            "success": True
        }
    )


@app.route("/reset")
def reset():

    os.makedirs(
        "generated",
        exist_ok=True
    )

    save_graph(
        {
            "nodes": [],
            "edges": []
        },
        "generated/graph.json"
    )

    return jsonify(
        {
            "success": True
        }
    )


@app.route("/generated/<path:path>")
def generated(path):

    return send_from_directory(
        "generated",
        path
    )


@app.route("/<path:path>")
def static_files(path):

    return send_from_directory(
        "src/viewer",
        path
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )