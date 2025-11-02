"""
Example: Custom Usage of Agentic RAG
Shows how to add your own documents and query them
"""

import os
from dotenv import load_dotenv
from vector_store import VectorStore
from agentic_rag_agent import AgenticRAGAgent


def example_custom_documents():
    """Example using custom documents"""
    print("=" * 60)
    print("  CUSTOM DOCUMENT EXAMPLE")
    print("=" * 60)
    
    # Load environment
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ Please set GEMINI_API_KEY in .env file")
        return
    
    # Initialize with a custom collection
    vector_store = VectorStore(collection_name="custom_docs")
    
    # Add your custom documents
    my_documents = [
        "My company specializes in AI-powered solutions for healthcare. "
        "We develop machine learning models to assist in medical diagnosis.",
        
        "Our team consists of data scientists, software engineers, and domain experts. "
        "We use technologies like TensorFlow, PyTorch, and cloud computing.",
        
        "Recent projects include predicting patient outcomes, automating medical coding, "
        "and developing chatbots for patient engagement.",
        
        "We follow agile methodology and prioritize innovation and research. "
        "Our focus areas are precision medicine and healthcare automation."
    ]
    
    print("\n📚 Adding custom documents to knowledge base...")
    vector_store.add_documents(my_documents)
    
    # Initialize agent
    agent = AgenticRAGAgent(api_key, vector_store)
    
    # Query your documents
    print("\n🔍 Querying custom knowledge base...\n")
    result = agent.process_query(
        "What does the company do and what are the main technologies used?"
    )
    
    print(f"\n📝 Answer:\n{result['response']}")
    
    # Clean up (optional)
    print("\n🧹 Cleaning up custom collection...")
    vector_store.clear_collection()


def example_simple_query():
    """Simple single-query example"""
    print("\n" + "=" * 60)
    print("  SIMPLE QUERY EXAMPLE")
    print("=" * 60)
    
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ Please set GEMINI_API_KEY in .env file")
        return
    
    # Use existing collection from main.py
    vector_store = VectorStore()
    agent = AgenticRAGAgent(api_key, vector_store)
    
    # Simple query
    query = "How do vector databases work in RAG systems?"
    result = agent.process_query(query)
    
    print(f"\nQuestion: {query}")
    print(f"\nAnswer: {result['response']}")


if __name__ == "__main__":
    # Run simple example
    example_simple_query()
    
    # Uncomment to run custom documents example
    # example_custom_documents()
