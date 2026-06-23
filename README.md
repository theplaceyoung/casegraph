# CaseGraph

CaseGraph is an assistant for researchers that transforms legal decisions into structured graphs and machine-readable data.

## Overview

CaseGraph converts legal documents (initially FTC decisions) into structured entities and relationships, providing interactive exploration and export capabilities.

### Current Focus

* Single PDF processing
* Interactive graph visualization
* JSON export
* Research support and exploratory analysis

### Future Directions

* Multiple document integration
* Cross-institution comparison
* Court decisions and committee decisions
* Knowledge graph analysis

---

## Project Structure

```text
casegraph/

app.py              # Web application
ingest.py           # Experimental / local execution

src/

    process_pdf.py  # Core pipeline

    converters/
        pdf_to_md.py

    parsers/
        ftc_parser.py
        clean_text.py

    extractors/
        entity_extractor.py

    graph/
        graph_builder.py

    viewer/
        index.html
        graph.js
        style.css

generated/
uploads/
raw/
markdown/
```

---

## Current Pipeline

```text
PDF
 ↓
pdf_to_md()
 ↓
clean_text()
 ↓
parse_ftc_document()
 ↓
extract_entities()
 ↓
build_graph()
 ↓
Graph JSON
 ↓
Interactive Viewer
 ↓
Export JSON
```

---

## Current Features

* ✅ Single PDF processing
* ✅ Entity extraction
* ✅ Interactive graph viewer
* ✅ Node detail panel
* ✅ JSON export

---

## Architecture

```text
app.py
      ↓
process_pdf()
      ↓
pdf_to_md()
      ↓
clean_text()
      ↓
ftc_parser()
      ↓
entity_extractor()
      ↓
graph_builder()
```

---

## Development Roadmap

### v0.1

* [x] Single PDF support
* [x] Graph visualization
* [x] Node information panel
* [x] JSON export

### v0.2

* [ ] PDF upload from browser
* [ ] Generate graph from uploaded PDF
* [ ] Standardize FTC parser

### v0.3

* [ ] Multiple PDF integration
* [ ] Unified graph

### v1.0

* [ ] Cross-institution comparison
* [ ] Court decisions
* [ ] Knowledge graph exploration

---

## Philosophy

CaseGraph is not merely a graph visualization tool.

Its primary objective is to support researchers by transforming legal decisions into structured, machine-readable representations that can be explored, analyzed, and extended.

The long-term goal of CaseGraph is to assist researchers in understanding how institutions and courts interpret similar issues from different perspectives.
