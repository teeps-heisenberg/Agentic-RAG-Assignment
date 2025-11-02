"""
Vector Store Module for Document Retrieval
Handles document embedding, storage, and similarity search
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Optional
import uuid


class VectorStore:
    """Manages document embeddings and similarity search"""
    
    def __init__(self, collection_name: str = "agentic_rag_docs"):
        """Initialize vector store with embedding model and ChromaDB"""
        self.collection_name = collection_name
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize ChromaDB client
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./chroma_db"
        ))
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )
    
    def add_documents(self, texts: List[str], metadatas: Optional[List[Dict]] = None):
        """Add documents to the vector store"""
        # Generate embeddings
        embeddings = self.embedding_model.encode(texts).tolist()
        
        # Prepare IDs
        ids = [str(uuid.uuid4()) for _ in texts]
        
        # Prepare metadatas
        if metadatas is None:
            metadatas = [{"text": text[:100]} for text in texts]
        
        # Add to collection
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
    
    def search(self, query: str, n_results: int = 3) -> List[Dict]:
        """Search for similar documents"""
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query]).tolist()[0]
        
        # Search collection
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        # Format results
        formatted_results = []
        if results['documents']:
            for i, doc in enumerate(results['documents'][0]):
                formatted_results.append({
                    'content': doc,
                    'metadata': results['metadatas'][0][i] if results['metadatas'] else {}
                })
        
        return formatted_results
    
    def clear_collection(self):
        """Clear all documents from the collection"""
        self.client.delete_collection(name=self.collection_name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )
