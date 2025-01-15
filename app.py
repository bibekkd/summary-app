import streamlit as st
from utils.file_upload import process_uploaded_file
from utils.summarize import generate_summary

# Main App
st.title("Document Summary Assistant")

# File Upload Section
st.sidebar.title("Upload Your Document")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "jpg", "png"])

# Summary Length Selection
summary_length = st.sidebar.radio(
    "Choose Summary Length", ["Short", "Medium", "Long"], index=1
)

if uploaded_file:
    # Process uploaded file
    with st.spinner("Processing your document..."):
        extracted_text = process_uploaded_file(uploaded_file)

    # Show extracted text
    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Preview", extracted_text, height=200)

        # Generate Summary
        with st.spinner("Generating Summary..."):
            summary = generate_summary(extracted_text, summary_length)

        # Display Summary
        if summary:
            st.subheader("Generated Summary")
            st.text_area("Summary", summary, height=200)
    else:
        st.error("Could not extract text from the document.")
