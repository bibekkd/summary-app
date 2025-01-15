from utils.text_extraction import extract_text_from_image, extract_text_from_pdf

def process_uploaded_file(uploaded_file):
    try:
        file_type = uploaded_file.type

        if "pdf" in file_type:
            return extract_text_from_pdf(uploaded_file)
        elif "image" in file_type:
            return extract_text_from_image(uploaded_file)
        else:
            raise ValueError("Unsupported file type. Please upload a PDF or an image file.")
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"An error occurred while processing the file: {str(e)}"



