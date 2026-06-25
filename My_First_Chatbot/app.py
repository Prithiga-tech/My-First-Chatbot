from flask import Flask, render_template, request
import fitz
import ollama
import os

app = Flask(__name__)

# Store PDF text
pdf_text = ""

# Store chat history
chat_history = []

# Create uploads folder if not exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")


@app.route("/", methods=["GET", "POST"])
def home():
    global pdf_text
    global chat_history

    if request.method == "POST":

        # PDF Upload
        if "pdf" in request.files:
            file = request.files["pdf"]

            if file.filename != "":
                filepath = os.path.join("uploads", file.filename)
                file.save(filepath)

                # Read PDF
                doc = fitz.open(filepath)

                pdf_text = ""

                for page in doc:
                    pdf_text += page.get_text()

        # Question Ask
        question = request.form.get("question")

        if question and pdf_text:

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
You are a PDF assistant.

Answer ONLY using the PDF content below.

PDF Content:
{pdf_text}

Question:
{question}
"""
                    }
                ]
            )

            answer = response["message"]["content"]

            chat_history.append({
                "question": question,
                "answer": answer
            })

    return render_template(
        "index.html",
        history=chat_history
    )


if __name__ == "__main__":
    app.run(debug=True)