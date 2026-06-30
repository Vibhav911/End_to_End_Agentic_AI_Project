from typing import Annotated, Literal, Optional, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage


class State(TypedDict):
     """
     Represents the structure of the states used in the grpah
     """

     messages: Annotated[list, add_messages]
     
