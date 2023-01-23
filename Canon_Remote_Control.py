import streamlit as st
from PIL import Image

from ccapi.ccapi import CCAPI

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

tab_preview, tab_general, tab_focusbracketing, = st.tabs(["Preview", "Settings", "Focusbraceting"])

st.session_state.image_available = False

if not st.session_state.image_available:
    st.sidebar.markdown("# Canon Remote Control")

values = {}
st.session_state.camera_values = values

camera = CCAPI()

settings = camera.get_settings()


def preview(position=tab_preview):
    camera = CCAPI()
    device = camera.get_deviceinformation()

    name = "./preview.jpeg"
    # camera.release()
    r = camera.liveview(display="on", size="medium")
    r = camera.get_liveview_image(name)
    # camera.preview(name)

    position.markdown("# Preview")

    try:
        image = Image.open('./preview.jpeg')
        position.image(image, caption='Preview')
        position.session_state.image_available = True
    except Exception as e:
        position.write("error loading preview")
        position.write(e)
    print("preview")


def stack():
    print("stack")
    camera = CCAPI()
    device = camera.get_deviceinformation()
    camera.shoot(af=False)


def generate_selectbox(label=None, key=None, version="ver110", position=st.sidebar, on_change=preview):
    version = camera.get_settings_version(key=key)
    value = settings[version][key]["value"]
    ability = settings[version][key]["ability"]
    disabled = len(ability) == 0
    if not disabled:
        index = ability.index(value)
        component = position.selectbox(label=label, key=key, options=ability, index=index, on_change=on_change)
    else:
        component = position.selectbox(label=label,
                                       key=key,
                                       options=["av is disabled and not be set"],
                                       index=0,
                                       disabled=disabled)
    return component


def generate_slider(label=None, key=None, version="ver110", position=st.sidebar):
    version = camera.get_settings_version(key=key)
    value = settings[version][key]["value"]
    ability = settings[version][key]["ability"]
    minimum = ability["min"]
    maximum = ability["max"]
    step = ability["step"]
    if len(ability) != 0:
        component = position.slider(label=label,
                                    key=key,
                                    value=value,
                                    min_value=minimum,
                                    max_value=maximum,
                                    step=step)
    else:
        position.markdown(f"**{key}** can not be set")
        component = None
    return component


def save():
    print("save")
    print(st.session_state.camera_values)

    for key in ["iso",
                "av",
                "tv",
                "drive",
                "aeb",
                "flash",
                "shuttermode",
                # ("exposure", "ver100"),
                "focusbracketing",
                "focusbracketing_numberofshots",
                "focusbracketing_focusincrement"]:
        print(key, ":", st.session_state.camera_values[key])

    camera.focusbracketing = st.session_state.camera_values["focusbracketing"]
    camera.exposuresmoothing = True
    camera.numberofshots = st.session_state.camera_values["focusbracketing_numberofshots"]
    camera.focusincrement = st.session_state.camera_values["focusbracketing_focusincrement"]


st.sidebar.markdown("# Shoot")

st.sidebar.button("Save Parameters to :camera:", on_click=save)

st.sidebar.button("Preview Image from :camera:", on_click=preview)
st.sidebar.button("Create Stack :camera: ... :camera:", on_click=stack)


tab_focusbracketing.markdown("# Focusbracketing")
for label, key in [("Focusbracketing", "focusbracketing")]:
    values[key] = generate_selectbox(position=tab_focusbracketing, label=label, key=key)

for label, key in [("Number of shots", "focusbracketing_numberofshots"),
                   ("Focus increment", "focusbracketing_focusincrement")]:
    values[key] = generate_slider(position=tab_focusbracketing,label=label, key=key)

tab_general.markdown("# General")

for key in ["iso",
            "av",
            "tv",
            "drive",
            "aeb",
            "flash",
            "shuttermode",
            "afmethod"
            # ("exposure", "ver100")
            ]:
    values[key] = generate_selectbox(position=tab_general,label=key, key=key)
st.session_state.camera_values = values

# log = st.container()
#
# log.write("msg")
