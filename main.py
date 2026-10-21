"""
Main Application: Agentic RAG Demonstration
Shows practical usage of the agentic RAG system with Gemini
"""

import utils.session
import os
from dotenv import load_dotenv
from vector_store import VectorStore
from agentic_rag_agent import AgenticRAGAgent


def setup_knowledge_base(vector_store: VectorStore):
    """Populate the vector store with sample knowledge"""
    print("📚 Setting up knowledge base...")
    
    # Sample documents demonstrating RAG capabilities
    documents = [
        """Agentic RAG (Retrieval-Augmented Generation) is an advanced approach that combines 
retrieval systems with large language models. Unlike traditional RAG, agentic RAG systems 
demonstrate autonomous decision-making capabilities, allowing them to determine when to 
retrieve information, which tools to use, and how to synthesize responses.""",
        
        """Key features of agentic systems include:
1. Autonomous decision-making without explicit instructions
2. Multi-step reasoning and planning
3. Tool use and orchestration
4. Dynamic adaptation based on context
5. Iterative refinement of responses

These features enable more sophisticated question-answering and information synthesis.""",
        
        """Google's Gemini model is a state-of-the-art multimodal AI model capable of 
understanding and generating text, code, and other content types. It excels at:
- Natural language understanding and generation
- Code generation and analysis
- Multimodal reasoning
- Long-context handling
- Tool use and API integration""",
        
        """Vector databases like ChromaDB enable efficient similarity search over document 
embeddings. They work by:
1. Converting text documents into high-dimensional vectors using embedding models
2. Storing vectors with their metadata
3. Performing fast similarity searches using cosine similarity or other distance metrics
4. Enabling RAG systems to quickly find relevant context for generation""",
        
        """The RAG workflow typically involves:
1. Query understanding and analysis
2. Retrieval of relevant documents from a knowledge base
3. Context preparation and formatting
4. Generation using LLM with context
5. Response refinement and synthesis

Agentic RAG extends this with autonomous decision-making at each step."""
    ]
    
    metadatas = [
        {"source": "rag_introduction", "topic": "agentic_rag"},
        {"source": "agentic_features", "topic": "agentic_systems"},
        {"source": "gemini_model", "topic": "llm_models"},
        {"source": "vector_databases", "topic": "retrieval"},
        {"source": "rag_workflow", "topic": "rag_process"}
    ]
    
    vector_store.add_documents(documents, metadatas=metadatas)
    print("✅ Knowledge base ready!")
    print()


def main():
    """Main demonstration application"""
    print("=" * 60)
    print("  AGENTIC RAG DEMONSTRATION WITH GEMINI")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    # Get Gemini API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("⚠️  GEMINI_API_KEY not found in environment variables")
        print("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
        print("\nTo get an API key: https://makersuite.google.com/app/apikey")
        return
    
    # Initialize components
    print("\n🔧 Initializing components...")
    vector_store = VectorStore()
    agent = AgenticRAGAgent(api_key, vector_store)
    
    # Setup knowledge base
    setup_knowledge_base(vector_store)
    
    # Demo 1: Single query with agentic reasoning
    print("\n" + "=" * 60)
    print("DEMO 1: Single Query with Agentic Reasoning")
    print("=" * 60)
    
    query1 = "What is agentic RAG and how does it differ from traditional RAG?"
    result1 = agent.process_query(query1)
    
    print(f"\n📝 Final Response:\n{result1['response']}")
    
    # Demo 2: Autonomous multi-step research
    print("\n" + "=" * 60)
    print("DEMO 2: Autonomous Multi-Step Research")
    print("=" * 60)
    
    query2 = "Explain how Gemini models work with vector databases"
    research_result = agent.autonomous_research(query2, iterations=2)
    
    print(f"\n📊 Research Summary:")
    print(f"Completed {research_result['iterations']} autonomous research iterations")
    print(f"Final insights:\n{research_result['responses'][-1]['response'][:500]}...")
    
    print("\n" + "=" * 60)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
