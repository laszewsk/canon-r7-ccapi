import eel
from random import randint

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def random_python():
    print("Random function running")
    return randint(1, 100)


# Start the index.html file
eel.start("index.html")