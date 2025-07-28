#!/usr/bin/env python3

import os
import sys
import json
import time
from pathlib import Path

from src.pdf_processor import PDFProcessor

def main():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    
    output_dir.mkdir(exist_ok=True)
    
    processor = PDFProcessor()
    
    pdf_files = list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in input directory")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process")
    
    for pdf_path in pdf_files:
        start_time = time.time()
        
        try:
            print(f"Processing: {pdf_path.name}")
            
            result = processor.extract_outline(pdf_path)
            
            output_filename = pdf_path.stem + ".json"
            output_path = output_dir / output_filename
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            
            processing_time = time.time() - start_time
            print(f"✓ Completed {pdf_path.name} in {processing_time:.2f}s")
            
        except Exception as e:
            print(f"✗ Error processing {pdf_path.name}: {str(e)}")
            error_result = {
                "title": "Error: Could not process document",
                "outline": []
            }
            output_filename = pdf_path.stem + ".json"
            output_path = output_dir / output_filename
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(error_result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
