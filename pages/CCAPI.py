from ccapi import CCAPI
import streamlit as st
import os
from cloudmesh.common.Tabulate import Printer

# def handle_ip():
#     print("IP", st.session_state.ip)
#     os.system(f"export CANONE_IP={st.session_state.ip}")
#     os.environ["CANON_IP"] = st.session_state.ip
#
#
# st.text_input("IP Address",
#                       key="ip",
#                       on_change=handle_ip())
#
# print(st.session_state.ip)

st.markdown("# CCAPI Table")

camera = CCAPI()
ccapi_table = camera.ccapi(output="github")
st.markdown(ccapi_table)




