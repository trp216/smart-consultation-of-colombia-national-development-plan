from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate  
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import gradio as gr

OPENAI_API_KEY = "" # Replace with your OpenAI API key

vector_store = Chroma(persist_directory=".././vectordb", embedding_function=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model = "text-embedding-3-large"))

llm_model = ChatOpenAI(temperature=0.2, openai_api_key=OPENAI_API_KEY, model="gpt-4o-mini")

system_message = (
    '''Eres un asistente experto en políticas públicas encargado de responder preguntas de los ciudadanos 
    con respecto al plan de desarrollo de colombia. 
    A partir de la siguiente informacion extraída del plan de desarrollo:

    {context}

    Responde de manera clara y detallada, utilizando un lenguaje accesible para el público en general, las preguntas de un ciudadano.

    '''
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_message), 
        ("human", "{input}"),
     ]
)

def answer(query,history):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    #print(retriever.invoke("Que se planea hacer para proteger a los ciudadanos del desempleo?"))

    chain = create_stuff_documents_chain(llm_model,prompt)
    rag_chain = create_retrieval_chain(retriever, chain)

    results = rag_chain.invoke({"input": query})
    answer = results["answer"] + "\n\n"
    
    pages = ""
    
    for doc in results["context"]:
        pages += doc.metadata.get("page_label", "") + " "


    answer += f"Tomado de las páginas: {pages}"

    return answer

gr.ChatInterface(answer).launch()

#if __name__ == "__main__":
#    print(answer(input("Pregunta: ")))