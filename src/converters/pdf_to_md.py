from pathlib import Path
from src.parsers.clean_text import clean_text
import fitz


def convert_pdf_to_markdown(
        input_pdf: Path,
        output_dir: Path,
        output_name=None
):

    print(f"Converting {input_pdf.name}...")

    doc = fitz.open(input_pdf)

    lines = []

    for page_num, page in enumerate(doc, start=1):

        print(f"  Page {page_num}/{len(doc)}")

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                line_text = "".join(
                    span["text"]
                    for span in line["spans"]
                )

                line_text = line_text.strip()

                if line_text:
                    lines.append(line_text)

        lines.append("")

    markdown = "\n".join(lines)

    markdown = clean_text(markdown)

    if output_name is None:
        md_name = f"{input_pdf.stem}.md"
    else:
        md_name = f"{Path(output_name).stem}.md"

    output_path = output_dir / md_name

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Saved {output_path.name}")


def convert_all_pdfs():

    raw_dir = Path("raw_pdfs")
    md_dir = Path("markdown")

    md_dir.mkdir(exist_ok=True)

    pdf_files = list(raw_dir.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDFs")

    for pdf_file in pdf_files:

        convert_pdf_to_markdown(
            pdf_file,
            md_dir
        )


def convert_pdf(
        pdf_path,
        original_filename=None
):

    pdf_path = Path(pdf_path)

    md_dir = Path("markdown")

    md_dir.mkdir(exist_ok=True)

    convert_pdf_to_markdown(
        pdf_path,
        md_dir,
        original_filename
    )

    if original_filename is None:

        md_name = f"{pdf_path.stem}.md"

    else:

        md_name = f"{Path(original_filename).stem}.md"

    md_path = md_dir / md_name

    return md_path