import os
import fitz  # PyMuPDF
import json
from datetime import datetime

# Load persona
with open("persona.json", "r", encoding="utf-8") as f:
    persona_data = json.load(f)

keywords = persona_data["job_to_be_done"].lower().split()

output_data = {
    "metadata": {
        "persona": persona_data["persona"],
        "job_to_be_done": persona_data["job_to_be_done"],
        "input_documents": [],
        "processing_timestamp": datetime.now().isoformat()
    },
    "extracted_sections": [],
    "subsection_analysis": []
}

rank_counter = 1

for filename in os.listdir("input"):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join("input", filename)
        output_data["metadata"]["input_documents"].append(filename)

        doc = fitz.open(pdf_path)
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            for line in text.split("\n"):
                lowered = line.lower()
                match_count = sum(1 for kw in keywords if kw in lowered)
                if match_count >= 2 and len(line.strip()) > 30:
                    output_data["extracted_sections"].append({
                        "document": filename,
                        "page": page_num,
                        "section_title": line.strip(),
                        "importance_rank": rank_counter
                    })
                    output_data["subsection_analysis"].append({
                        "document": filename,
                        "page": page_num,
                        "section_title": line.strip(),
                        "refined_text": line.strip()
                    })
                    rank_counter += 1

with open("output/intelligent_output.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)