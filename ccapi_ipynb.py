import ipywidgets as widgets

def selector(camera, key=None):
    data = camera.get_settings_value(key=key)
    w = widgets.RadioButtons(
        options=data['ability'],
        value=data["value"],
        description=f"{key}:",
        disabled=False,
        orientation='horizontal'
    )
    return w



def slider(camera, key=None):
    settings = camera.get_settings_value(key=key)
    version = camera.get_settings_version(key=key)
    value = settings["value"]
    ability = settings["ability"]
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
    return w


