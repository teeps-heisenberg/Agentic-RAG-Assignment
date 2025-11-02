# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Setup API Key

**Option A: Using the setup script**
```bash
python setup_env.py
```

**Option B: Manual setup**

Create a `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key: https://makersuite.google.com/app/apikey

### Step 3: Run the Demo

```bash
python main.py
```

## 📁 Project Files

- `main.py` - Main demonstration with sample knowledge
- `example_custom_usage.py` - Examples with your own documents
- `agentic_rag_agent.py` - Agentic RAG agent implementation
- `vector_store.py` - Vector database management
- `requirements.txt` - Python dependencies
- `setup_env.py` - Environment setup helper

## 🎯 What You'll See

The demo will show:

1. **Agentic Reasoning**: How the agent analyzes queries
2. **Document Retrieval**: Intelligent context selection
3. **Response Synthesis**: Combining information from multiple sources
4. **Autonomous Research**: Multi-step exploration

## 💡 Next Steps

- Try `example_custom_usage.py` with your own documents
- Modify the agent in `agentic_rag_agent.py`
- Add more tools and capabilities
- Integrate with your own data sources

## ⚙️ Customization

### Add Your Own Documents

```python
vector_store.add_documents(["Your doc 1", "Your doc 2"])
```

### Change Retrieval Settings

```python
results = vector_store.search("query", n_results=5)
```

### Adjust Agent Behavior

Modify the agent tools in `agentic_rag_agent.py`

## 🐛 Troubleshooting

**API Key Error**: Make sure `.env` file exists with correct API key

**Import Error**: Run `pip install -r requirements.txt`

**Memory Error**: Reduce `n_results` in search or batch size

## 📚 Learn More

See `README.md` for detailed documentation.

---

Happy Coding! 🎉
