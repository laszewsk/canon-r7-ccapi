import streamlit as st
from ccapi import CCAPI
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


camera = CCAPI()
private = st.sidebar.checkbox('Private', value=False, key="private")

device = camera.get_deviceinformation()

st.markdown("# Owner")

if private:
    author = "Your name"
    owner = "Your name"
    copyright = "Your e-mail or name"
    nickname = "The nickname of the camera on Wifi"
    ip = "192.168.xxx.xxx"
    device["guid"] = "54effad035450c40b62717ba5468cf2a"
    device["guid"] = "00000000000000000000000000000000"
    device["macaddress"] = "aa:bb:cc:dd:ee:ff"
    device["serialnumber"] = "000000000000"
else:
    author = camera.author
    owner = camera.owner
    copyright = camera.copyright
    nickname = camera.nickname
    ip = camera.ip

st.markdown(f"""
| Camera ID Info      | Values |
| --- | --- |
| Author    | {author} |
| Owner     | {owner} | 
| Copyright | {copyright} |
| Nickname  | {nickname} |
| IP        | {ip} |
| Battery Level | {camera.charge} |
""")

st.markdown("# Device")

st.markdown(Printer.attribute(device, output="github"))

st.markdown("# Storage")

storage = camera.get_storage()

cards = Printer.write(storage,
                      max_width=128,
                      order=["name", "maxsize", "spacesize", "contentsnumber", "accesscapability"],
                      header=["Name", "Total", "Free", "Images", "Accesscapability"],
                      output="github")
st.markdown(cards)

for i in range(2):
    m = float(storage[i]["maxsize"].replace(" GB", ""))
    free = float(storage[i]["spacesize"].replace(" GB", ""))
    level = str(round(free / m * 100.0, 2))
    st.sidebar.metric(label=f"Card {i + 1}", value=f"{level} % free")

st.markdown("# Battery")

b = [camera.get_battery(output="json")]

st.markdown(Printer.write(b,
                          order=["name", "level", "quality"],
                          header=["Name", "Level", "Quality"],
                          output="github"))
level = b[0]["level"]
st.sidebar.metric(label="Battery", value=f"{level} % charged")

temp = camera.get_temperature()["status"]
st.sidebar.metric(label="Temperature", value=f"{temp}")

dt = camera.get_datetime()["datetime"]
st.sidebar.write(f"{dt}")
