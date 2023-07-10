from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
import os
os.environ["OPENAI_API_KEY"] = "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"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            reader = PdfReader(r"C:\Users\ASUS\Downloads\Eknath Easwaran - The Bhagavad Gita  -Nilgiri Press (2007).pdf")
            raw_text = ''
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    raw_text += text

            text_splitter = CharacterTextSplitter(
                separator=".",
                chunk_size=len(raw_text) // 120,
                chunk_overlap=0,
                length_function=len,
            )
            documents = text_splitter.split_text(raw_text)

            embeddings = OpenAIEmbeddings()
            docs_embeddings = FAISS.from_texts(documents, embeddings)

            chain = load_qa_chain(OpenAI(), chain_type="stuff")

            docs = docs_embeddings.similarity_search(query)
            answer = chain.run(input_documents=docs, question=query)

            return render_template("index.html", heading="Bhagavad Gita", query=query, answer=answer)

    return render_template("index.html", heading="Bhagavad Gita")

if __name__ == "__main__":
    app.run(debug=True)
