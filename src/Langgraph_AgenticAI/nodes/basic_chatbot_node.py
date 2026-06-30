from src.Langgraph_AgenticAI.state.state import State

class BasicChatbotNode:
     """
          Basic Chatbot Node Implementation 
     """

     def __init__(self, model):
          self.llm = model

     def process(self, state: State) -> dict:
          """
               Processes the input data and generates the chatbot output
          """

          return {
               "messages": self.llm.invoke(state['messages'])
          }