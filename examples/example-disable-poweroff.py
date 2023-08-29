from ccapi.ccapi import CCAPI
from pprint import pprint
ip="192.168.50.210"
camera = CCAPI(ip=ip, debug=False)
df = camera.ccapi(output="df")
pprint(df)
r = camera.get_autopoweroff()
print(r)

print(camera.autopoweroff)
camera.autopoweroff = "180"
print(camera.autopoweroff)
camera.autopoweroff = "disable"
print(camera.autopoweroff)

