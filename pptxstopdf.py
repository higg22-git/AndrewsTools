import os
import subprocess
from pypdf import PdfWriter

def combine_presentations(input_dir, output_file):
    temp_pdfs = []
    
    for filename in sorted(os.listdir(input_dir)):
        if filename.lower().endswith((".pptx", ".ppt")) and not filename.startswith("~$"):
            in_path = os.path.abspath(os.path.join(input_dir, filename))
            
            subprocess.run([
                "libreoffice", 
                "--headless", 
                "--convert-to", 
                "pdf", 
                in_path, 
                "--outdir", 
                input_dir
            ], check=True)
            
            out_path = os.path.abspath(os.path.join(input_dir, f"{os.path.splitext(filename)[0]}.pdf"))
            temp_pdfs.append(out_path)
            
    merger = PdfWriter()
    for pdf in temp_pdfs:
        merger.append(pdf)
        
    final_path = os.path.abspath(os.path.join(input_dir, output_file))
    merger.write(final_path)
    merger.close()
    
    for pdf in temp_pdfs:
        os.remove(pdf)

combine_presentations("/home/andrewhiggins/Downloads/CS235Midterm1", "/home/andrewhiggins/Downloads/combined_output.pdf")