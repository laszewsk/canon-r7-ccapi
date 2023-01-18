import streamlit as st
from ccapi import CCAPI
from cloudmesh.common.Tabulate import Printer
import os

st.markdown("# Camera Settings")

camera = CCAPI()

s = camera.get_settings()

st.write(s)
