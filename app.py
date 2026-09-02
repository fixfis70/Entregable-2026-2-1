import streamlit as st

st.title("Entregable")

if "times" not in st.session_state:
    st.session_state.times = 0

if st.button("Haz clic"):
    st.session_state.times += 1

st.write(f"Has hecho clic {st.session_state.times} veces")