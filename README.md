# Smart Consultation of Colombia National Development Plan

This project presents the development of an intelligent query tool that leverages Retrieval Augmented Generation (RAG) to provide context-aware, natural language answers from the [National Development Plan of Colombia (2022-2026)](https://colaboracion.dnp.gov.co/CDT/Prensa/Publicaciones/plan-nacional-de-desarrollo-2022-2026-colombia-potencia-mundial-de-la-vida.pdf).

The solution combines the text generation capabilities of a large language model (OpenAI `gpt-4o-mini`), an embedding model for vectorization (OpenAI `text-embedding-3-large`) and the efficiency of a vector database (`ChromaDB`).

## 💡 Purpose

The main objective of this project is to simplify access to and understanding of the Colombian National Development Plan by allowing users to ask questions in plain language and receive precise answers — along with references to the original document.

This system was designed to:
- Improve the accessibility of public policy documents.
- Provide fast and reliable answers grounded in the original source.
- Demonstrate the practical use of RAG, Embeddings, and Vector Databases.

## 📚 Technologies & Concepts

This project applies several concepts covered in the Gen AI Intensive Course 2025Q1 (Kaggle):
- Retrieval-Augmented Generation (RAG).
- Embeddings for semantic understanding.
- Vector Search / Vector Storage / Vector Databases using ChromaDB.
- Grounding by referencing the original document in the answer of the RAG.

## ⚙️ How it Works

1. The large source document is split into smaller text chunks to make it manageable for embedding and retrieval.
2. Each chunk is converted into a vector representation (embedding).
3. These vectors are stored in ChromaDB, a vector database optimized for semantic search.
4. When a user submits a question, the most relevant chunks are retrieved and sent along with the prompt to the GPT-4o Mini model.
5. The model generates an answer grounded in the retrieved context, including references to the specific pages or sections of the source document.

## 📝 Grounding for Transparency

To ensure transparency and improve user trust, every response includes grounding references — pointing directly to the section or page of the source document from which the answer was derived.

## 🚀 Getting Started

1. Clone this repository.
2. Install dependencies:
   pip install -r requirements.txt
**Note:** You need to have Python already installed to use the project. This project was made using Python 3.12.9.
3. Add your OpenAI API key.
4. Run the notebook and explore the system!

### ⚠️ Disclaimer

This project is intended for educational purposes only. While the model provides helpful answers, users are encouraged to always refer to the official National Development Plan document for authoritative information.
