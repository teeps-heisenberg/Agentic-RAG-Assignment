"""
Agentic RAG Agent Module
Demonstrates autonomous decision-making and tool orchestration
"""

import google.generativeai as genai
from typing import List, Dict, Optional
from vector_store import VectorStore


class AgenticRAGAgent:
    """Agent with RAG capabilities and autonomous decision-making"""
    
    def __init__(self, api_key: str, vector_store: VectorStore):
        """Initialize the agent with Gemini API and vector store"""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.vector_store = vector_store
        
        # Agent reasoning tools
        self.tools = {
            'retrieve': self._retrieve_documents,
            'reason': self._reason_about_query,
            'synthesize': self._synthesize_response
        }
    
    def _retrieve_documents(self, query: str, num_docs: int = 3) -> List[Dict]:
        """Tool: Retrieve relevant documents from vector store"""
        results = self.vector_store.search(query, n_results=num_docs)
        return results
    
    def _reason_about_query(self, query: str) -> str:
        """Tool: Analyze the query to determine retrieval strategy"""
        reasoning_prompt = f"""Analyze this query and determine:
1. What specific information is needed?
2. What keywords should be used for retrieval?
3. How many documents should be retrieved?

Query: {query}

Provide a brief reasoning:"""
        
        response = self.model.generate_content(reasoning_prompt)
        return response.text
    
    def _synthesize_response(self, query: str, context: List[str]) -> str:
        """Tool: Synthesize final response from context"""
        context_text = "\n\n".join([f"Document {i+1}:\n{doc}" for i, doc in enumerate(context)])
        
        synthesis_prompt = f"""Based on the following context documents, provide a comprehensive answer to the query.

Context Documents:
{context_text}

Query: {query}

Provide a detailed answer that synthesizes information from the context:"""
        
        response = self.model.generate_content(synthesis_prompt)
        return response.text
    
    def process_query(self, query: str) -> Dict:
        """
        Main agentic method that autonomously decides which tools to use
        Demonstrates agentic behavior through multi-step reasoning
        """
        print(f"\n🤖 Agent Processing Query: {query}")
        print("-" * 60)
        
        # Step 1: Agent reasons about the query (agentic decision)
        print("\n📋 Step 1: Reasoning about query...")
        reasoning = self._reason_about_query(query)
        print(f"Agent reasoning: {reasoning[:200]}...")
        
        # Step 2: Agent retrieves relevant documents (tool use)
        print("\n🔍 Step 2: Retrieving relevant documents...")
        retrieved_docs = self._retrieve_documents(query, num_docs=3)
        context_list = [doc['content'] for doc in retrieved_docs]
        print(f"Retrieved {len(retrieved_docs)} documents")
        for i, doc in enumerate(retrieved_docs[:2], 1):
            print(f"  Doc {i}: {doc['content'][:100]}...")
        
        # Step 3: Agent synthesizes response (tool use)
        print("\n🎯 Step 3: Synthesizing response...")
        final_response = self._synthesize_response(query, context_list)
        
        # Step 4: Return comprehensive result
        result = {
            'query': query,
            'reasoning': reasoning,
            'retrieved_docs': retrieved_docs,
            'response': final_response,
            'steps_executed': 3
        }
        
        print("\n✅ Agent completed processing")
        print("=" * 60)
        
        return result
    
    def autonomous_research(self, topic: str, iterations: int = 2) -> Dict:
        """
        Advanced agentic behavior: Multi-iteration research
        Agent autonomously decides to dig deeper based on initial results
        """
        print(f"\n🔬 Starting Autonomous Research on: {topic}")
        print("=" * 60)
        
        all_responses = []
        current_topic = topic
        
        for i in range(iterations):
            print(f"\n--- Iteration {i+1} ---")
            result = self.process_query(current_topic)
            all_responses.append(result)
            
            # Agent decides what to research next (autonomous decision)
            if i < iterations - 1:
                follow_up_prompt = f"""Based on this research: {result['response'][:300]}
What aspect should be explored further to provide a complete answer? Respond with a single follow-up question."""
                
                follow_up = self.model.generate_content(follow_up_prompt)
                current_topic = follow_up.text.strip()
                print(f"\n🔄 Agent decided to explore: {current_topic}")
        
        return {
            'initial_topic': topic,
            'iterations': iterations,
            'responses': all_responses
        }
