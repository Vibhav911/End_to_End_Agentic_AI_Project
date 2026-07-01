from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
     """
     Return the lsit of tools to be used in the chabot
     """

     tools = [TavilySearch(max_results=2)]
     return tools

def create_tool_node(tools):
     """
     creates and returns a tool node for the graph
     """

     return ToolNode(tools=tools)
     