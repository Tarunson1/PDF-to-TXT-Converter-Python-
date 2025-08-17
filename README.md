# PDF to TXT Converter (Python)

This is a simple Python script that converts one or more PDF files into `.txt` files using the **PyPDF2** library. Each converted file will be saved with the name `word_<original_filename>.txt`.

---

## 📌 Features

* Extracts text from PDFs and saves them into text files.
* Handles multiple PDFs in a single run.
* Automatically names the output `.txt` files based on the input PDF name.
* Skips pages without text to avoid errors.

---

## 🛠️ Requirements

Make sure you have Python installed (>=3.7) and install the required dependency:

```bash
pip install PyPDF2
```

---

## 🚀 Usage

1. Clone or download this repository.
2. Place your PDF files in the same folder as the script (or provide full paths).
3. Run the script:

```bash
python pdf_to_txt.py
```

4. Enter the number of PDFs you want to convert and provide their filenames when prompted.

Example:

```
enter the number of PDFs you want to work on: 2
enter the pdf no.1: sample1.pdf
enter the pdf no.2: sample2.pdf
```

5. The script will generate:

```
word_sample1.txt
word_sample2.txt
```

---

## 📂 Project Structure

```
├── pdf_to_txt.py       # Main script
├── README.md           # Documentation
├── sample1.pdf         # Example input (user provided)
└── word_sample1.txt    # Example output
```

---

## 💻 Example Code Snippet

```python
import PyPDF2 
import os

# pdf to word.txt converter
pdfs=[]
n=int(input('enter the number of PDFs you want to work on'))
for i in range(n):
    name=input(f'enter the pdf no.{i+1} ')
    pdfs.append(name)

for pdf in pdfs:
    with open(pdf,'rb') as temp:
        reader=PyPDF2.PdfReader(temp)
        text_content=""
        for page in reader.pages:
            text_content+=page.extract_text() or '' 

    with open(f'word_{os.path.splitext(pdf)[0]}.txt','w',encoding='utf-8') as f:
        f.write(text_content)

    print('your pdf to text conversion is done')
```

---

## ⚠️ Notes

* This script works best with text-based PDFs. For scanned/image PDFs, you’ll need OCR tools like **pytesseract** instead.
* Empty pages or non-extractable content will simply be skipped.

---

## 📜 License

This project is open-source and free to use under the **MIT License**.

---


