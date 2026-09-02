import streamlit as st
import time

st.title("Test de Clicks por Segundo")

#aqui se guarda la data
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "finished" not in st.session_state:
    st.session_state.finished = False

#se ejecuta cada 0.1
@st.fragment(run_every=0.1)
def test():
    #si ya se inició
    if st.session_state.start_time is not None:

        elapsed = time.time() - st.session_state.start_time
        remaining = 10 - elapsed

        if not st.session_state.finished:
            if st.button("CLICK"):
                st.session_state.clicks += 1

        else:
            final_cps = st.session_state.clicks / 10
            st.success(f"¡Terminado! CPS final: {final_cps:.2f}")

        if remaining <= 0:
            st.session_state.finished = True
            remaining = 0

        st.write(f"⏱️ Tiempo: {remaining:.1f} segundos")
        st.write(f"🖱️ Clicks: {st.session_state.clicks}")

        if elapsed > 0 and st.session_state.finished == False:
            cps = st.session_state.clicks / elapsed
        else:
            cps = st.session_state.clicks

        st.write(f"⚡ CPS: {cps:.2f}")
test()

#En caso de q no halla nada
if st.session_state.start_time is None:
    if st.button("🚀 Iniciar test"):
        st.session_state.clicks = 0
        st.session_state.finished = False
        st.session_state.start_time = time.time()
        st.rerun()
