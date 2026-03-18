import streamlit as st
from utils.db import run_query

st.title("Energy Cycle Studio")
st.caption("Internal analytics · live data")

if st.button("Test database connection"):
    try:
        df = run_query("SELECT NOW()")
        st.success(f"Connected — {df.iloc[0,0]}")
    except Exception as e:
        st.error(f"Error: {e}")