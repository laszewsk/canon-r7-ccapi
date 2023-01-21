import os

import streamlit as st
from ccapi.ccapi import CCAPI
from cloudmesh.common.Tabulate import Printer

st.markdown("# Cards")

camera = CCAPI()

storage = camera.get_storage()

cards = Printer.write(storage,
                      max_width=128,
                      order=["name", "maxsize", "spacesize", "contentsnumber", "accesscapability"],
                      header=["Name", "Total", "Free", "Images", "Accesscapability"],
                      output="github")
st.markdown(cards)

card1 = st.sidebar.checkbox('Card 1', value=True)
card2 = st.sidebar.checkbox('Card 2', value=True)

st.markdown("# Content")

r = camera.contents()

table = {}

for image in r:
    location = image.split("contents")[1]
    name = os.path.basename(location)
    url = f"[{name}](http://{camera.ip}:8080{image})"
    id, kind = name.split(".")

    card = location.split("/")[1].replace("card", "Card ")

    if (card1 and "card1" in location) or (card2 and "card2" in location):
        entry = {
            "name": name,
            "location": location,
            "id": id,
            "card": card,
            "thumbnail_url": f"http://{camera.ip}:8080{image}" + "?kind=thumbnail",
            "thumbnail_link": f"![thumbnail](http://{camera.ip}:8080{image}" + "?kind=thumbnail)",
            "thumbnail_src": f'<img src="http://{camera.ip}:8080{image}?kind=thumbnail" />'

        }
        entry[kind] = url
        if id not in table.keys():
            table[id] = entry
        else:
            table[id].update(entry)

# st.markdown("| Images |\n | --- |\n" + table)

images = Printer.write(table,
                       max_width=128,
                       order=["card", "id", "thumbnail_link", "JPG", "CR3"],
                       header=["card", "ID", "Thumbnail", "JPG", "CR3"],
                       output="github")
st.markdown(images)

# for name, entry in table.items():
#     print (entry)
#     url = entry["thumbnail_url"]
#     print(url)
#     r = camera.get_thumbnail(url)

# url = "http://192.168.50.210:8080/ccapi/ver110/contents/card1/100EOSR7/2Z7A0224.JPG?kind=thumbnail"
# r = camera.get_thumbnail(url)
