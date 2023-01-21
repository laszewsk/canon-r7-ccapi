from ..ccapi import CCAPI
from pprint import pprint

camera = CCAPI()

#
# Prints the CCAPI in github markdown format
#
r = camera.ccapi(output="github")
print(r)


#
# Prints the CCAPI in github markdown format
#
r = camera.ccapi(output="json")
print(r)

#
# Prints the CCAPI in ASCII table format
#
r = camera.ccapi(output="table")
print (r)

# Demonstrates setting the author
#
camera.author = "Gregor von Laszewski"

#
# Demonstartes on how to get author, owner and copyright from the camera
# Nickname is the name used to find the camera by that
# name (not needed as we use the IP)

author = camera.author
owner = camera.owner
copyright = camera.copyright
# nickname = camera.nickname

print(f"Author: {author}")
print(f"Owner: {owner}")
print(f"Copyright: {copyright}")
# print(f"Nickname: {nickname}")

#
# Gets the battery information in json format
#
r = camera.get_battery(output="json")
print(r)

#
# Gets the battery level
#
r = camera.charge
print (r)

#
# Gets the settings form the camera as json object.
# This will also write them into a file called canon-settings.json
# This file can then be used to probe the values without constantly probing the camers

r = camera.settings()
pprint (r)

#
# Lists the contents of the images on the sd cards

r = camera.contents()
pprint(r)

#
# macro = Focus(camera)
# r = macro.focusbracketing()
# print (r)
#
# r = macro.focusbracketing("enable")
# # print (r)
#
# r = macro.focusbracketing()
# print (r)
#
# r = camera.get_battery()
# print (r)
#
# #print (r)
#
beep()

#
# COCUS BRACKETING RELATED
#

#
# Prints if focus bracekting is enabled
#
print (camera.focusbracketing)

#
# Enables focus bracketing
#
camera.focusbracketing = True
print (camera.focusbracketing)

#
# Enables exposure smoothing
#
camera.exposuresmoothing = True
print (camera.exposuresmoothing)

#
# sets the number of shots for focus bracketing
#
camera.numberofshots = 13
print(camera.numberofshots)

#
# sets the focusincrement
#

camera.focusincrement = 4
print (camera.focusincrement)

#
# returns information about the storage
#
print(camera.get_storage())

#
# Next functions relate to taking pictures
#

#
# TODO: do not just print the text, but display image
#       an exampleon how to do that is shown in
#       Canon_Remote_Control.py

# camera.release()
# r = camera.liveview(display="on", size="medium")
# print(r.text)
#
# for i in range(3):
#     name = f"img{i}.jpeg"
#     r = camera.get_image(name)
#     camera.preview(name)
#     print(r)
#     print(r.headers)

# r = camera.shoot(af=1)
# r = camera.shoot_control(af=True, action="full_press")
# r = camera.shoot_control(af=True, action="release")
# r = camera.shoot_control(af=True, action="half_press")
# r = camera.focus()

