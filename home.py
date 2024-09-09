#pip install streamlit
import streamlit as st
st.session_state.cnt = 0
if st.button("a"):
    st.write("안녕하세요.")
else :
    st.write("안녕히가세요.")

st.button("b")
#인터렉션 되는 순간 전체 리렌더링
#버튼은 가장 마지막에 누른 버튼만 true를 반환하고 나머지는 false가 된다.
#Next.js