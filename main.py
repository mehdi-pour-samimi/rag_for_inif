import os
import pandas as pd
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openrouter import ChatOpenRouter


df = pd.read_csv("knowledge.csv")

documents = []

for _, row in df.iterrows():
    
    content = f"""
    Category: {row['category']}
    
    Question: {row['question']}
    
    Answer: {row['answer']}
    """
    
    documents.append(content)
    
print(documents[:2])

#embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    Document(
        page_content=content,
        metadata={"row": i}
    )
    for i, content in enumerate(documents)
]

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

vectorstore.save_local("faiss_index")

#connect groq

load_dotenv()

llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0,
    max_tokens=1024
)

#create a prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the user's question using ONLY
the following context.

If the answer is not in the context,
say: I don't know based on my CSV data.

Context:
{context}

User Question:
{question}

Answer:
""")

rag_chain = prompt | llm | StrOutputParser()

#search the csv
def ask_question(question):
    
    results = vectorstore.similarity_search(
        question,
        k=3
    )
    
    
    context = "\n\n".join(
        doc.page_content for doc in results
    )
    
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })
    
    return answer

print("\n========== CSV RAG CHATBOT ==========")
print("Type 'exit' to quit.\n")

while True:
    
    question = input("You: ")
    
    if question.lower() == "exit":
        break
    
    
    answer = ask_question(question)
    
    
    print("\nAssistant:", answer)
    print("-" * 50)