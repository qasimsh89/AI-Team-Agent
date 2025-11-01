import json
import streamlit as st

from core.agent_manager import AgentManager

st.set_page_config(page_title="Agent Team GUI", layout="wide")

st.title("🤖 Agent Team GUI")

manager = AgentManager()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Agents")
    agents = manager.list_agents()
    selected_agent = st.selectbox("Select agent", agents)
    user_query = st.text_area("Your task / query")

    run_btn = st.button("Run agent")

with col2:
    st.subheader("Output")
    if run_btn and user_query:
        result = manager.run(selected_agent, user_query)
        st.json(result)
    else:
        st.info("Select an agent and enter a query, then click **Run agent**.")

st.markdown("---")
st.caption("Plug in your phi/OpenAI logic in each agent file.")