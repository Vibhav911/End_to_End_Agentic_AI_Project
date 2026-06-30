import streamlit as st       
from src.Langgraph_AgenticAI.ui.streamlitui.loadui import LoadStreamlitUI
from src.Langgraph_AgenticAI.LLMs.groqllm import GroqLLM
from src.Langgraph_AgenticAI.graph.graph_builder import GraphBuilder
from src.Langgraph_AgenticAI.ui.streamlitui.display_result import DisplayResultStreamlit


# Main Function Start
def load_langgraph_agenticai_app():
      """
      Loads and runs the LangGraph AgenticAI application with Streamlit UI. 
      This function initializes the UI, handles user input, configures the LLM model, 
      sets up the graph based on the selected use case, and displays the output while
      implementing exception handling for robustness.
      """

      # Load UI
      ui = LoadStreamlitUI()
      user_input = ui.load_streamlit_ui()

      if not user_input:
            st.error("Error: Failed to load user input from the UI")
            return 

      
      # Text Input for User Message
      if st.session_state.IsFetchButtonClicked:
            user_message = st.session_state.timeframe

      elif st.session_state.IsSDLC:
            user_message = st.session_state.state 
      
      else:
            user_message = st.chat_input("Enter your Message: ")


      if user_message:
            try:
                  # Configure LLM
                  obj_llm_config = GroqLLM(user_controls_input=user_input)
                  model = obj_llm_config.get_llm_model()

                  if not model:
                        st.error("Error: LLM Model cannot be initialized")
                        return

                  # Initialize and set up the graph based on use case
                  usecase = user_input.get("selected_usecase")
                  if not usecase:
                        st.error("Error: No usecase selected")


                  # Graph Builder
                  graph_builder = GraphBuilder(model)
                  try:
                        graph = graph_builder.setup_graph(usecase)
                        DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

                  except Exception as e:
                        st.error(f"Error: Graph setup failed - {e}")
                        return

                  


            except Exception as e:
                  raise ValueError(f"Error occurred with Exception: {e}")