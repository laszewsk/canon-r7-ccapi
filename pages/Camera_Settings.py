import streamlit as st
from ccapi.ccapi import CCAPI

st.markdown("# Camera Settings")

camera = CCAPI()

s = camera.get_settings()

st.write(s)
