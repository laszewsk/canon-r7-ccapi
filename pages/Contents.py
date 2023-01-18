import streamlit as st
from ccapi import CCAPI
from cloudmesh.common.Tabulate import Printer
import os

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
            "card": card
        }
        entry[kind] = url
        if id not in table.keys():
            table[id] = entry
        else:
            table[id].update(entry)

#st.markdown("| Images |\n | --- |\n" + table)

images = Printer.write(table,
                  max_width=128,
                  order=["card", "id","JPG", "CR3"],
                  header=["card", "ID", "JPG", "CR3"],
                  output="github")
st.markdown(images)