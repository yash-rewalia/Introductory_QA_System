# Document-Based QnA System using LlamaIndex

## Introduction

This project is a Question-and-Answer (QnA) system that allows users to extract information from documents using semantic search and vector embeddings. The system processes documents, converts their content into embeddings, stores them in a knowledge base, and retrieves relevant answers based on user queries. 

## Project Workflow

Below is the step-by-step process of how this system works:

![NoteGPT-Flowchart-1739817148268](https://github.com/user-attachments/assets/178313dc-af39-478c-8435-d7e2475afbf8)
8.png)

1. **Document Input**: A document is provided for data extraction.
2. **Data Extraction & Chunking**: The document is processed, and its content is split into smaller chunks.
3. **Vector Embedding Generation**: Each chunk is converted into a vector embedding.
4. **Semantic Indexing**: A semantic index is built using LlamaIndex.
5. **Storage**: The embeddings are stored in a knowledge base or vector storage.
6. **User Query**: A user submits a question.
7. **Query Embedding Generation**: The query is transformed into an embedding.
8. **Semantic Search**: The system performs a semantic search in the knowledge base.
9. **Best Match Selection**: The most relevant answer is identified.
10. **Response**: The answer is returned to the user.

## Technologies Used

- **LlamaIndex**: For building the semantic index.
- **Vector Embeddings**: Used for document and query representation.
- **Semantic Search**: To retrieve the most relevant answers.

## Usage

1. Upload a document.
2. Ask a question related to the document.
3. Receive the best possible answer based on the content.

## Conclusion

This system enables efficient information retrieval from documents using AI-powered search techniques. Happy querying!

