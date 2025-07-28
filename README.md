# PDF Outline Extractor

A robust PDF outline extraction system that automatically detects document titles and hierarchical headings (H1, H2, H3) with high accuracy from PDF files, producing structured JSON outlines.

---

## 🧠 Approach

### Multi-Signal Heading Detection

Our solution intelligently combines several signals beyond simple font size to identify headings and build document outlines:

1. **Font Analysis:**
   Examines font size, weight (boldness), and style differences.

2. **Pattern Matching:**  
   Detects common heading formats such as numbered sections (`1.`, `1.1`), title case, and ALL CAPS headings.

3. **Positional Context:**  
   Considers the text location within pages and overall document flow.

4. **Text Characteristics:**  
   Uses text length, capitalization, and punctuation patterns to distinguish headings from body text.

---

## ⚙️ Key Features

- **Robust Font Handling:** Accurately detects headings even if font sizes are inconsistent.  
- **Pattern Recognition:** Supports numbered headings and diverse styles including uppercase and title case.  
- **Multilingual Support:** Handles various character sets, including non-Latin scripts (e.g., Japanese).  
- **Confidence Scoring:** Assigns a confidence score to each detected heading to prioritize results.  
- **Duplicate Removal:** Removes redundant headings appearing multiple times across pages.

---

## 📚 Libraries Used

- **PyMuPDF (fitz):** For PDF parsing and extracting text with detailed font metadata.  
- **Python Standard Library:** For regex, statistics, JSON handling, and file operations.

---

## 🏗️ Project Structure


main.py                 # Entry point for processing all PDFs in batch
src/
├── pdf_processor.py    # Core logic for PDF parsing and heading extraction
└── __init__.py        # Package initializer (empty)



## 🚀 How It Works
Extract Text Blocks: Extracts text with font and style metadata from all pages.

Detect Title: Finds the largest font-size text within the first two pages to identify the document title.

Classify Headings: Uses font size, boldness, text patterns, and heuristics to classify headings into H1, H2, and H3.

Calculate Confidence: Scores headings based on multiple features to rank their likelihood.

Generate Outline: Constructs a structured, hierarchical JSON outline per PDF.



## 🛠️ Build and Run
Build Docker Image
bash
Copy code
docker build --platform linux/amd64 -t pdf-extractor:latest .
Run the Container
bash
Copy code
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-extractor:latest


## ⚡ Performance Characteristics
Execution Time: Under 10 seconds for 50-page PDFs on CPU with 8 cores and 16GB RAM.

Memory Usage: Efficient handling optimized for 16GB RAM limit.

Model Size: No external ML models used; total dependencies < 200MB.

Offline Capability: Fully functional with no internet access required.

## 🧩 Handling Edge Cases
Complex Layouts: Supports multi-column text, tables, headers, and footers.

Formatting Variability: Works with inconsistent font sizes and mixed styles.

Multilingual Content: Unicode support allows processing documents in various languages.

Scanned PDFs: Only supports text-based PDFs; scanned images require OCR preprocessing.

## 📄 Output Format Example
Each PDF produces a JSON file matching this structure:

json
Copy code
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Chapter 1: Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 2 },
    { "level": "H3", "text": "Related Work", "page": 3 }
  ]
}


