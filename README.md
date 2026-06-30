# PDF Chatbot using Ollama and Flask

## Project Overview

This project is a PDF-based Question Answering Chatbot developed as part of the "Generative AI for Beginners" learning journey through Infosys Springboard and Udemy. The application enables users to upload PDF documents and ask questions related to the content of those documents. The chatbot extracts text from the uploaded PDF and uses a locally running Large Language Model (LLM) through Ollama to generate accurate responses based on the document content.

The project demonstrates the practical implementation of Generative AI concepts, document processing, prompt engineering, and integration of local language models into web applications.

## Objectives

* Build a chatbot capable of answering questions from PDF documents.
* Understand the fundamentals of Generative AI applications.
* Learn how to integrate Large Language Models using Ollama.
* Implement PDF text extraction and document-based question answering.
* Develop a user-friendly web interface using Flask, HTML, and CSS.

## Features

* Upload PDF documents through a web interface.
* Extract text from uploaded PDFs using PyMuPDF.
* Ask natural language questions related to the document content.
* Generate answers using the Llama 3.2 model running locally through Ollama.
* Maintain chat history during the session.
* Simple and responsive user interface.
* Works without cloud APIs, reducing dependency on external services.

## Technologies Used

### Backend

* Python
* Flask

### Generative AI

* Ollama
* Llama 3.2

### PDF Processing

* PyMuPDF (fitz)

### Frontend

* HTML
* CSS

## Project Structure

```text
pdf_chatbot/
│
├── app.py
├── uploads/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Workflow

1. The user uploads a PDF document.
2. The application extracts text from the PDF using PyMuPDF.
3. The extracted text is stored as context.
4. The user enters a question through the chatbot interface.
5. The question and PDF content are sent to the Llama 3.2 model via Ollama.
6. The model generates a response based on the uploaded document.
7. The answer is displayed in the chat interface and stored in the chat history.

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd pdf_chatbot
```

### Install Dependencies

```bash
pip install flask pymupdf ollama
```

### Install and Run Ollama

Download and install Ollama from the official website.

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Verify the installation:

```bash
ollama run llama3.2
```

### Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Sample Images
<img width="1912" height="915" alt="image" src="https://github.com/user-attachments/assets/61a4a928-b92e-416f-867d-959846e8582f" />

## Learning Outcomes

Through this project, the following concepts were explored:

* Introduction to Generative AI
* Large Language Models (LLMs)
* Prompt Engineering
* Local AI Model Deployment using Ollama
* PDF Document Processing
* Flask Web Development
* Frontend and Backend Integration
* Building AI-powered Applications

## Future Enhancements

* Support for multiple PDF uploads.
* Retrieval-Augmented Generation (RAG) using vector databases.
* Semantic search with embeddings.
* User authentication and session management.
* Dark mode and advanced user interface improvements.
* Export chat history functionality.
* Support for DOCX and TXT files.

## Conclusion

This project successfully demonstrates the integration of Generative AI with document processing to create an intelligent PDF Question Answering Chatbot. By leveraging Ollama and the Llama 3.2 model, the application provides an efficient and cost-effective solution for interacting with document content while running entirely on a local machine.

## Author

Prithiga-tech
