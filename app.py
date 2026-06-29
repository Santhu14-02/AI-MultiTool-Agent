import streamlit as st
from agent import run_agent_with_logs

st.set_page_config(
    page_title="MultiTool Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 MultiTool Agent")

query = st.text_input("Ask me anything")

if st.button("Run") and query:

    result = run_agent_with_logs(query)

    st.subheader("Agent Execution")

    st.code(result["logs"], language="text")

    st.subheader("Final Answer")

    st.success(result["answer"])