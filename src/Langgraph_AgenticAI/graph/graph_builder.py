from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.Langgraph_AgenticAI.state.state import State
from src.Langgraph_AgenticAI.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:

     def __init__(self, model):
          self.llm = model
          self.graph_builder = StateGraph(State)

     def basic_chabot_build_graph(self):
          """
          Builds a basic chatbot graph using LangGraph.
          This method initializes a chatbot node using the BaSicChatbotNode class and integrates it into the graph. 
          The chatbot node is set as both the entry and exit point of the graph.
          """

          self.basic_chabot_node = BasicChatbotNode(self.llm)
          self.graph_builder.add_node("chatbot", self.basic_chabot_node.process)
          self.graph_builder.add_edge(START, "chatbot")
          self.graph_builder.add_edge("chatbot", END)


     def setup_graph(self, usecase: str):
          """
          Sets up the graph for the selected use case
          """

          if usecase == "Basic Chatbot":
               self.basic_chabot_build_graph()

          return self.graph_builder.compile()