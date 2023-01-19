import streamlit as st
from PIL import Image

from ccapi import CCAPI

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

st.session_state.image_available = False

if not st.session_state.image_available:
    st.sidebar.markdown("# Canon Remote Control")

values = {}
st.session_state.camera_values = values

camera = CCAPI()

settings = camera.get_settings()


def preview():
    camera = CCAPI()
    device = camera.get_deviceinformation()

    name = "./preview.jpeg"
    # camera.release()
    r = camera.liveview(display="on", size="medium")
    r = camera.get_image(name)
    # camera.preview(name)
    st.markdown("# Preview")

    try:
        image = Image.open('./preview.jpeg')
        st.image(image, caption='Preview')
        st.session_state.image_available = True
    except Exception as e:
        st.write("error loading preview")
        st.write(e)
    print("preview")


def stack():
    print("stack")
    camera = CCAPI()
    device = camera.get_deviceinformation()
    camera.shoot(af=False)


def generate_selectbox(label=None, key=None, version="ver110", position=st.sidebar, on_change=preview):
    value = settings[version][key]["value"]
    ability = settings[version][key]["ability"]
    index = ability.index(value)
    component = position.selectbox(label=label, key=key, options=ability, index=index, on_change=on_change)
    return component


def generate_slider(label=None, key=None, version="ver110", position=st.sidebar):
    value = settings[version][key]["value"]
    ability = settings[version][key]["ability"]
    minimum = ability["min"]
    maximum = ability["max"]
    step = ability["step"]
    component = position.slider(label=label,
                                key=key,
                                value=value,
                                min_value=minimum,
                                max_value=maximum,
                                step=step)
    return component


def save():
    print("save")
    print(st.session_state.camera_values)

    for key, version in [("iso", "ver110"),
                         ("av", "ver110"),
                         ("tv", "ver110"),
                         ("drive", "ver110"),
                         ("aeb", "ver110"),
                         ("flash", "ver110"),
                         ("shuttermode", "ver100"),
                         # ("exposure", "ver100"),
                         ("focusbracketing", "ver110"),
                         ("focusbracketing_numberofshots", "ver110"),
                         ("focusbracketing_focusincrement", "ver110")]:
        print(key, ":", st.session_state.camera_values[key])

    camera.focusbracketing = st.session_state.camera_values["focusbracketing"]
    camera.exposuresmoothing = True
    camera.numberofshots = st.session_state.camera_values["focusbracketing_numberofshots"]
    camera.focusincrement = st.session_state.camera_values["focusbracketing_focusincrement"]


st.sidebar.markdown("# Shoot")

st.sidebar.button("Save Parameters to :camera:", on_click=save)

st.sidebar.button("Preview Image from :camera:", on_click=preview)
st.sidebar.button("Create Stack :camera: ... :camera:", on_click=stack)

st.sidebar.markdown("# Focusbracketing")
for label, key, version in [("Focusbracketing", "focusbracketing", "ver110")]:
    values[key] = generate_selectbox(label=label, key=key, version=version)

for label, key, version in [("Number of shots", "focusbracketing_numberofshots", "ver110"),
                            ("Focus increment", "focusbracketing_focusincrement", "ver110")]:
    values[key] = generate_slider(label=label, key=key, version=version)

st.sidebar.markdown("# General")

for key, version in [("iso", "ver110"),
                     ("av", "ver110"),
                     ("tv", "ver110"),
                     ("drive", "ver110"),
                     ("aeb", "ver110"),
                     ("flash", "ver110"),
                     ("shuttermode", "ver100"),
                     ("afmethod", "ver110"),
                     # ("exposure", "ver100")
                     ]:
    values[key] = generate_selectbox(label=key, key=key, version=version)
st.session_state.camera_values = values

log = st.container()

log.write("msg")
