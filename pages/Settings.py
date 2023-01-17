from ccapi import CCAPI
import streamlit as st
import os

def handle_ip():
    print("IP", st.session_state.ip)
    os.system(f"export CANONE_IP={st.session_state.ip}")
    os.environ["CANON_IP"] = st.session_state.ip

st.session_state.ip = None
if os.environ["CANON_IP"]:
    st.session_state.ip = os.environ["CANON_IP"]

st.text_input("IP Address",
                      key="ip",
                      on_change=handle_ip())

print(st.session_state.ip)

# camera = CCAPI("192.168.50.210")
# r = camera.ccapi(output="table")
# st.write(r)