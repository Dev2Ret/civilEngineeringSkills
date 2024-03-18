import streamlit as st

class Tab4:
    def __init__(self):
        st.header("PDF File Upload")
        file_upload = st.file_uploader(label="Choose a PDF file")