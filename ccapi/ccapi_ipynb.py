import ipywidgets as widgets
from IPython.display import display
from cloudmesh.common.util import readfile

#
# TODO: EVENT HANDLER DOES NOT YET WORK
#
def camera_eventhandler(change):
    print(change)
    print(change.new)

def choice(camera=None, key=None):
    settings = camera.settings
    version = camera.get_settings_version(key=key)
    data = settings[version][key]
    value = camera.get_settings_value(key=key)["value"]
    ability = data["ability"]
    w = widgets.RadioButtons(
        options=ability,
        value=value,
        description=f"{key}:",
        disabled=False,
        orientation='horizontal'
    )
    # TODO: this does not work yet
    camera.set_settings_value(key=key, value=w.value)
    w.observe(camera_eventhandler, names='value')
    ###
    display(w)
    return w

def slider(camera=None, key=None):
    settings = camera.settings
    version = camera.get_settings_version(key=key)
    data = settings[version][key]
    value = camera.get_settings_value(key=key)["value"]
    ability = data["ability"]
    minimum = ability["min"]
    maximum = ability["max"]
    step = ability["step"]
    w = widgets.IntSlider(
        value=value,
        min=minimum,
        max=maximum,
        step=step,
        description=f'{key}:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )
    # TODO: this does not work yet
    w.observe(camera_eventhandler, names='value')
    camera.set_settings_value(key=key, value=w.value)
    ###
    display(w)
    return w

def gui(camera=None, key=None):
    settings = camera.settings
    version = camera.get_settings_version(key=key)
    kind = settings[version][key]["kind"]
    if kind == "choice":
        return choice(camera=camera, key=key)
    elif kind =="slider":
        return slider(camera=camera, key=key)
    else:
        print (f"kind is not supported. Found: {kind}")
        return None


