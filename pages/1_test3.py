import streamlit as st
if "cnt" not in st.session_state :
    st.session_state.cnt = 0

if st.button("plus"):
    if "cnt" in st.session_state:
        st.session_state.cnt += 1
        st.write(st.session_state.cnt)