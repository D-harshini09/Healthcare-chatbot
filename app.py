import streamlit as st
import PyPDF2
import nltk
from nltk.corpus import words

# Download the NLTK words corpus
nltk.download('words')

# Title of the app
st.title('PDF Text Extraction and AI-Generated Content Analysis')

# Input from user
pdf_file = st.file_uploader('Upload a PDF file', type='pdf')

# Check if a file has been uploaded
if pdf_file is not None:
    # Load the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract the text from each page of the PDF
    text = ""
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text += page.extract_text()

    # Remove non-alphanumeric characters and convert to lowercase
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    text = text.lower()

    # Check for AI-generated content
    word_set = set(words.words())
    words_in_text = text.split()
    num_ai_words = 0
    for word in words_in_text:
        if word not in word_set:
            num_ai_words += 1
    ai_percentage = num_ai_words / len(words_in_text) * 100

    # Write the text to a file
    with open('output.txt', 'w') as text_file:
        text_file.write(text)

    # Display the AI-generated content percentage
    st.write(f"AI-generated content percentage: {ai_percentage:.2f}%")
