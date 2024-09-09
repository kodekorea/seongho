import streamlit as st
import time

@st.cache_data
def show():
    time.sleep(5)
    "HiHi"

show()
#st.write(st.secrets["apiKey"])