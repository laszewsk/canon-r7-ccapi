import streamlit as st
from cloudmesh.common.util import readfile

contributors = readfile("CONTRIBUTORS.md")
st.write(contributors)