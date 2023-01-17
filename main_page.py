import os

import streamlit as st
from cloudmesh.common.util import readfile


about = """
This application uses is used to control a Canon camera remotely.

The copyright of the application is with Gregor von Laszewski, 
laszewski@gmail.com and is under Apache Licence.

It uses internally the Canon CCAPI. The current implementation of the 
GUI portion uses StreamIt which has a separate copyright."
"""

st.set_page_config(
    page_title="Canon Camera Control",
    # page_icon=":alert:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://google.com',
        'Report a bug': "https://google.com",
        'About': about
    }
)

st.markdown("# Main page")
st.sidebar.markdown("# Main page")

# picture = st.camera_input("Take a picture")
# if picture:
#    st.image(picture)

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# # Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone')
)

#
# # Add a slider to the sidebar:
add_slider = st.sidebar.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0)
)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

label1 = st.checkbox("foo")


st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil")


st.metric(label="Step", value="1 μm", delta="0.4 μm")

iso = st.sidebar.selectbox(
    'iso',
     [100,200,300])

tv = st.sidebar.selectbox(
    'Tv',
     ["1/60","250"])

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

