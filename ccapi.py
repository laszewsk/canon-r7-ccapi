import os
import shutil
import sys

import humanize
import requests
from cloudmesh.common.Printer import Printer

# def get
#  r = requests.get('https://httpbin.org/basic-auth/user/pass')
# >>> r.status_code

debug = True


class CCAPI:

    #
    # http://<IP>:8080/ccapi
    # /ver100/deviceinformation
    # /ver100/devicestatus/temperature
    # /ver100/devicestatus/battery
    # /ver110/devicestatus/batterylist # gives more detailed infrmation
    # /ver100/devicestatus/lens

    def __init__(self, ip, port=8080):
        self.ip = ip
        self.port = port

    @property
    def copyright(self):
        r = self._get(path="/ccapi/ver100/functions/registeredname/copyright").json()['copyright']
        return r

    @copyright.setter
    def copyright(self, _copyright):
        r = self._put(path="/ccapi/ver100/functions/registeredname/copyright",
                      json={"copyright": _copyright})
        return r

    @property
    def author(self):
        r = self._get(path="/ccapi/ver100/functions/registeredname/author").json()['author']
        return r

    @author.setter
    def author(self, _author):
        r = self._put(path="/ccapi/ver100/functions/registeredname/author",
                      json={"author": _author})
        return r

    @property
    def owner(self):
        r = self._get(path="/ccapi/ver100/functions/registeredname/ownername").json()['ownername']
        return r

    @owner.setter
    def owner(self, _owner):
        r = self._put(path="/ccapi/ver100/functions/registeredname/ownername",
                      json={"ownername": _owner})
        return r

    @property
    def nickname(self):
        r = self._get(path="/ccapi/ver100/functions/registeredname/nickname").json()['nickname']
        return r

    @nickname.setter
    def nickname(self, _nickname):
        r = self._put(path="/ccapi/ver100/functions/registeredname/nickname",
                      json={"nickname": _nickname})
        return r

    def _get(self, path=None):
        url = f'http://{self.ip}:{self.port}{path}'
        if debug:
            print(f"GET: {url}")
        r = requests.get(url)
        return r

    def _put(self, path=None, json=None):
        url = f'http://{self.ip}:{self.port}{path}'
        if debug:
            print(f"PUT: {url} <- {json}")
        r = requests.put(url, json=json)
        return r

    def _post(self, path=None, json=None):
        url = f'http://{self.ip}:{self.port}{path}'
        if debug:
            print(f"POST: {url} <- {json}")
        r = requests.post(url, json=json)
        return r

    def ccapi(self, output="table"):
        result = []
        r = self._get(path="/ccapi")
        d = r.json()
        if output == "native":
            r = d
        else:
            for version in d.keys():
                api = d[version]
                for entry in api:
                    entry["version"] = version
                    result.append(entry)
                r = Printer.write(result,
                                  max_width=128,
                                  order=["version", "path", "get", "put", "post", "delete"],
                                  output=output)
        return r

    def get_storage(self, output="table"):
        r = self._get(path="/ccapi/ver110/devicestatus/storage").json()["storagelist"]
        for entry in r:
            entry["maxsize"] = humanize.naturalsize(entry["maxsize"])
            entry["spacesize"] = humanize.naturalsize(entry["spacesize"])
            entry["name"] = entry["name"].replace("card", "Card ")
            # entry["path"] = os.path.basename(entry["path"])
            #    .replace("card", "Card ")
        r = Printer.write(r,
                          max_width=128,
                          order=["name", "maxsize", "spacesize", "contentsnumber", "accesscapability"],
                          header=["Name", "Total", "Free", "Images", "Accesscapability"],
                          output=output)

        return r

    @property
    def charge(self):
        b = self.get_battery(output=None)["level"]
        return b

    def get_battery(self, output="table"):
        # /ccapi/ver100/devicestatus/battery
        # /ccapi/ver110/devicestatus/batterylist

        # for R7 we have one battery

        # The ver100 call needs to be done first to get accurate level information
        no_percent = self._get(path="/ccapi/ver100/devicestatus/battery")
        result = self._get(path="/ccapi/ver110/devicestatus/batterylist")
        r = result.json()["batterylist"][0]
        if output in ["json", None]:
            return r
        else:
            r = Printer.attribute(r, output=output)
        return r

    def get_settings(self):
        a = self._get(path="/ccapi/ver110/shooting/settings").json()
        b = self._get(path="/ccapi/ver100/shooting/settings").json()
        c = a.update(b)
        # r = result.json()["batterylist"][0]
        # r = Printer.attribute(r, output=output)
        return [a, b]

    def contents(self):

        cards = self._get(path="/ccapi/ver110/contents").json()["path"]
        images = []
        for path in cards:
            directory = self._get(path=path).json()["path"]
            for d in directory:
                files = self._get(path=d).json()["path"]
                for f in files:
                    images.append(f)
        return images

        # r = result.json()["batterylist"][0]
        # r = Printer.attribute(r, output=output)
        # return r.json()

    @property
    def exposuresmoothing(self):
        r = self._get(path="/ccapi/ver100/shooting/settings/focusbracketing/exposuresmoothing").json()
        return r

    @exposuresmoothing.setter
    def exposuresmoothing(self, on):
        value = self._get_enable(on)
        r = self._put(path="/ccapi/ver100/shooting/settings/focusbracketing/exposuresmoothing",
                      json={"value": value})
        return r

    def get_numberofshots(self):
        r = self._get(path="/ccapi/ver100/shooting/settings/focusbracketing/numberofshots").json()
        return r

    @property
    def numberofshots(self):
        r = self.get_numberofshots()
        return r

    @numberofshots.setter
    def numberofshots(self, n):
        ability = self.get_numberofshots()["ability"]
        print("AAA", ability)
        if ability["min"] <= n <= ability["max"]:
            r = self._put(path="/ccapi/ver100/shooting/settings/focusbracketing/numberofshots",
                          json={"value": n})
        return r

    def get_focusincrement(self):
        r = self._get(path="/ccapi/ver100/shooting/settings/focusbracketing/focusincrement").json()
        return r

    @property
    def focusincrement(self):
        r = self.get_focusincrement()
        return r

    @focusincrement.setter
    def focusincrement(self, n):
        ability = self.get_focusincrement()["ability"]
        print("AAA", ability)
        if ability["min"] <= n <= ability["max"]:
            r = self._put(path="/ccapi/ver100/shooting/settings/focusbracketing/focusincrement",
                          json={"value": n})
        return r

    def _get_enable(self, on):
        value = False
        if on in ["1", "on", True]:
            value = "enable"
        else:
            value = "disable"
        return value

    def _get_bool(self, on):
        value = False
        if on in ["1", "on", True, "true", "True"]:
            value = True
        else:
            value = False
        return value

    @property
    def focusbracketing(self):
        r = self._get(path="/ccapi/ver100/shooting/settings/focusbracketing").json()
        return r

    @focusbracketing.setter
    def focusbracketing(self, on):
        value = self._get_enable(on)
        r = self._put(path="/ccapi/ver100/shooting/settings/focusbracketing",
                      json={"value": value})
        return r

    def liveview(self, display="on", size="medium"):
        if display not in ["on", "off", "keep"]:
            print("p error")
            return None
        if size not in ["small", "off", "medium"]:
            print("p error")
            return None

        r = self._post(path="/ccapi/ver100/shooting/liveview",
                       json={"cameradisplay": display,
                             "liveviewsize": size
                             })

        return r

    def get_image(self, name):

        url = "http://192.168.50.210:8080/ccapi/ver100/shooting/liveview/flipdetail?kind=image"
        url = "http://192.168.50.210:8080/ccapi/ver100/shooting/liveview/flip"

        response = requests.get(url, stream=True)
        with open(name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        # del response
        return response

    def preview(self, name):
        os.system(f" open /Applications/Google\ Chrome.app {name}")

    def shoot(self, af=True):
        af = self._get_bool(af)
        r = self._post(path="/ccapi/ver100/shooting/control/shutterbutton",
                       json={
                           "af": af
                       })
        return r

    def shoot_control(self, af=True, action="full_press"):
        af = self._get_bool(af)
        if action not in ["full_press", "half_press", "release"]:
            return
        r = self._post(path="/ccapi/ver100/shooting/control/shutterbutton/manual",
                       json={
                           "af": af,
                           "action": action
                       })
        return r

    def focus(self):
        r = camera.shoot_control(af=True, action="half_press")
        return r

    def release(self):
        r = camera.shoot_control(af=False, action="release")
        return r


#
# | ver100  | /ccapi/ver100/shooting/settings/focusbracketing                        | True  | True  | False | False  |
# | ver100  | /ccapi/ver100/shooting/settings/focusbracketing/numberofshots          | True  | True  | False | False  |
# | ver100  | /ccapi/ver100/shooting/settings/focusbracketing/focusincrement         | True  | True  | False | False  |
# | ver100  | /ccapi/ver100/shooting/settings/focusbracketing/exposuresmoothing      | True  | True  | False | False  |

def beep():
    sys.stdout.write('\a')


if __name__ == '__main__':

    camera = CCAPI("192.168.50.210")
    r = camera.ccapi(output="table")
    print(r)
    # r = camera.ccapi(output="json")
    # print(r)

    # camera.author = "Gregor von Laszewski"

    # author = camera.author
    # owner = camera.owner
    # copyright = camera.copyright
    # nickname = camera.nickname
    #
    # print(f"Author: {author}")
    # print(f"Owner: {owner}")
    # print(f"Copyright: {copyright}")
    # print(f"Nickname: {nickname}")

    # r = camera.ccapi(output="table")
    # print (r)
    #
    # r = camera.get_battery(output="json")
    # print(r)
    # r = camera.get_battery()
    # print (r)
    #
    # r = camera.settings(output="table")
    # pprint (r)
    #
    # # r = camera.contents()
    # # pprint(r)
    #
    # # r = camera.contents()
    # # pprint(r)
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

    print("SUPER")

    # print(camera.author)
    # print(camera.nickname)
    # print(camera.owner)
    # print(camera.copyright)

    print(camera.charge)

    # print (camera.focusbracketing)
    # camera.focusbracketing = True
    # print (camera.focusbracketing)

    # camera.exposuresmoothing = True
    # print (camera.exposuresmoothing)
    #
    # print(camera.numberofshots)
    #
    # camera.numberofshots = 13
    #
    # print(camera.numberofshots)
    #
    # camera.focusincrement = 4
    # print (camera.focusincrement)

    # print(camera.get_storage())

    # pprint(camera.get_settings())

    camera.release()
    r = camera.liveview(display="on", size="medium")
    print(r.text)

    for i in range(3):
        name = f"img{i}.jpeg"
        r = camera.get_image(name)
        camera.preview(name)
        print(r)
        print(r.headers)

    # r = camera.shoot(af=1)
    # r = camera.shoot_control(af=True, action="full_press")
    # r = camera.shoot_control(af=True, action="release")
    # r = camera.shoot_control(af=True, action="half_press")
    # r = camera.focus()

    # url = "https://192.168.50.210:8080/ccapi/ver100/shooting/liveview/flip"

    # r = requests.get(url)

    # print(dir(r))
    # print(r)
    #
    # print(r.text)
    # print(r.content)
    # print(r.reason)
    # print(r.raw)
    # print (r._content)
