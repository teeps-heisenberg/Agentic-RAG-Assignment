# Agentic RAG with Gemini

A practical demonstration of an **Agentic RAG (Retrieval-Augmented Generation)** system using Google's Gemini model. This project showcases autonomous decision-making, multi-step reasoning, and intelligent tool orchestration.

## 🚀 Features

### Core Components

1. **Vector Store** (`vector_store.py`)
   - Document embedding using Sentence Transformers
   - Persistent storage with ChromaDB
   - Fast similarity search for context retrieval

2. **Agentic RAG Agent** (`agentic_rag_agent.py`)
   - Autonomous query analysis and reasoning
   - Dynamic document retrieval decision-making
   - Multi-tool orchestration (retrieve, reason, synthesize)
   - Iterative research capabilities

3. **Main Application** (`main.py`)
   - Complete demonstration workflow
   - Sample knowledge base setup
   - Multiple demo scenarios

### Agentic Behaviors Demonstrated

- **Autonomous Decision-Making**: Agent decides when and how to retrieve information
- **Multi-Step Reasoning**: Breaks down complex queries into reasoning steps
- **Tool Orchestration**: Seamlessly uses multiple tools (retrieve, reason, synthesize)
- **Iterative Research**: Autonomously decides what to explore further
- **Context Synthesis**: Intelligently combines information from multiple sources

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## 🔧 Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## 🎯 Usage

### Run the Demonstration

```bash
python main.py
```

### What You'll See

1. **Single Query Demo**: Agentic reasoning on a single question
   - Query analysis and reasoning
   - Document retrieval
   - Response synthesis

2. **Autonomous Research Demo**: Multi-iteration research
   - Initial query processing
   - Autonomous follow-up questions
   - Deep information synthesis

### Code Examples

#### Basic Usage

```python
from vector_store import VectorStore
from agentic_rag_agent import AgenticRAGAgent

# Initialize components
vector_store = VectorStore()
agent = AgenticRAGAgent(api_key="your_key", vector_store=vector_store)

# Add documents
vector_store.add_documents(["Document 1", "Document 2"])

# Process query
result = agent.process_query("What are the key features?")
print(result['response'])
```

#### Autonomous Research

```python
# Multi-step autonomous research
research = agent.autonomous_research("Explain AI agents", iterations=3)
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Main Application                  │
└────────────────────┬────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼──────────┐    ┌─────────▼──────────┐
│ Agentic RAG Agent│    │   Vector Store     │
│                  │    │                    │
│ • Reason         │    │ • Embed Documents  │
│ • Retrieve       │    │ • Similarity Search│
│ • Synthesize     │    │ • ChromaDB         │
└───────┬──────────┘    └────────────────────┘
        │
┌───────▼────────────────────────────────┐
│      Google Gemini API                 │
│      (Text Generation)                 │
└────────────────────────────────────────┘
```

## 📊 Key Concepts

### Traditional RAG vs Agentic RAG

**Traditional RAG:**
- Fixed retrieval pipeline
- No autonomous decisions
- Single-step processing

**Agentic RAG:**
- Adaptive retrieval strategies
- Autonomous decision-making
- Multi-step reasoning
- Dynamic tool selection

### Agent Components

- **Vector Store**: Manages document embeddings and retrieval
- **Gemini Model**: Handles generation and reasoning
- **Agent Orchestrator**: Coordinates tools and decisions
- **Knowledge Base**: Pre-loaded context documents

## 🔍 How It Works

1. **Query Analysis**: Agent reasons about what information is needed
2. **Retrieval Strategy**: Decides which documents to fetch
3. **Context Preparation**: Formats retrieved information
4. **Generation**: Uses Gemini to synthesize response
5. **Iteration**: Optionally explores deeper aspects

## 📝 File Structure

```
agentic-rag-project/
├── main.py                    # Main demonstration
├── agentic_rag_agent.py       # Agent with tool orchestration
├── vector_store.py            # Vector database management
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .env                       # Environment config (create this)
```

## 🛠️ Technologies Used

- **Google Generative AI**: Gemini model integration
- **ChromaDB**: Vector database for embeddings
- **Sentence Transformers**: Document embeddings
- **Python-dotenv**: Environment configuration

## 🎓 Learning Outcomes

This project demonstrates:
- RAG system implementation
- Vector database usage
- LLM integration with Gemini
- Agentic AI patterns
- Tool orchestration
- Autonomous decision-making

## 📖 License

This is a demonstration project for educational purposes.

## 🤝 Contributing

Feel free to extend this project with:
- Additional tools and capabilities
- Different vector databases
- Alternative LLM integrations
- Web interface
- Database persistence

## ⚠️ Notes

- Ensure you have a valid Gemini API key
- ChromaDB data is stored in `./chroma_db` directory
- First run may download embedding models (~90MB)

## 🔗 Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)

---

**Built as a practical demonstration of Agentic RAG capabilities with Google Gemini**
