# 📄 Document Summary Assistant

**Document Summary Assistant** is a smart application that allows users to upload PDF or image files and generates concise, smart summaries of their content. The app uses advanced text extraction techniques (OCR and PDF parsing) combined with AI-powered summarization to highlight key points and main ideas.

---

## 🌟 Features

- **Document Upload**:  
  - Supports uploading PDF files and image files (e.g., scanned documents).  
  - Easy drag-and-drop or file picker interface.

- **Text Extraction**:  
  - Extracts text from PDF files while maintaining the original structure.  
  - Uses OCR (Optical Character Recognition) for text extraction from image files.

- **Smart Summarization**:  
  - Generates summaries in different lengths: **Short**, **Medium**, and **Long**.  
  - Highlights key points and captures the main theme and essential information.  

- **Error Handling**:  
  - Provides error messages for unsupported file types or processing issues.

---
## 🚀 Getting Started

Check out the live app here: https://ai-smart-summary.streamlit.app/


Follow these steps to set up and run the project locally:

### 1. Clone the Repository
    git clone https://github.com/bibekkd/summary-app.git
    
    cd summary-app
    

### 2. Create a Virtual Environment
    # For Linux/Mac
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Run the Application

Start the Streamlit app:

    streamlit run app.py

### 📁 File Structure
    document_summary_assistant/
    ├── app.py                 # Main Streamlit app
    ├── requirements.txt       # Python dependencies
    ├── utils/
    │   ├── file_upload.py     # File upload handling
    │   ├── text_extraction.py # PDF and OCR text extraction logic
    │   └── summarize.py       # AI-powered summarization logic
    └── assets/                # Static files (optional)

## 🔧 Tech Stack

- **Streamlit**: Interactive web application framework. 
- **PyPDF2**: For extracting text from PDF documents.
- **pytesseract**:OCR library for text extraction from images. 
- **Gemini AI API**: For generating smart summaries. 
- **Pillow**: Image processing library.

## 💡 Usage Instructions

1. Upload a PDF or image file via the app’s interface.

2. Choose the summary length: Short, Medium, or Long.

3. View the extracted text and generated summary directly in the app.


## ❓ Troubleshooting

- If a file type other than PDF or image is uploaded, the app will display an error:  
  *"Unsupported file type. Please upload a PDF or an image file."*  
- If no text is found in the uploaded PDF or image, the app will display an error:  
  *"No text detected. Please upload a valid document with readable text."*  
- Ensure all dependencies are installed using the `requirements.txt` file.

## 🛠 Future Improvements


- Support for additional file types (e.g., DOCX, TXT). 

- Multi-language text extraction and summarization.

- Batch document processing.

## 📄 License
This project is open-source and available under the MIT License.


