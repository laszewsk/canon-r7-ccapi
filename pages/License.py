import streamlit as st
from cloudmesh.common.util import readfile

license = readfile("LICENSE.txt")
st.write(license)
