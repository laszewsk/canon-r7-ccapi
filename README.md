# canon-r7-ccapi

## The problem

Many people noticed that the regular EOS Utility program has issues 
on some Mac's. This happens only via WiFi. The USB connection works fine.
However we like to be able to access the Cannon cameras via WiFi.

## The solution

The method chosen here uses the official CCAPI that relies on REST service 
calls in the network shared between the camera and the compter. The following 
features are available:

* Elementary Python library to control many of the Canon camera
* Elementary GUI interface to run the program from a GUI
* Ability to run the GUI on Linux, macOS, Windows 10, Windows11
* Expandable

With this GUI it is possible to conduct focus brackating remotely. Many 
fetuares of the camera can be controlled remotely.

As the program uses CCAPI it can be likely used for other cameras also. 
Make suer your camera is compatible

... more will be added here

## Install

```bash
$ git clone https://github.com/laszewsk/canon-r7-ccapi.git
$ cd canon-r7-ccapi
$ pip install -r requirements.txt
$ export CANON_IP=<Your canon camera ip address>
$ make
```

Thos will install and run the program using a GUI.

## Plan

* manual
* documentation of the API
* writing an article for a hacker magazine/web site
* showcasing the macro stand
* evaluate integration with WeMacro

## Common less expensive lenses


100=400mm f5.6-???

| Focal length      | Minimum focusing distance | Magnification
|-------------------|---------------------------| --- |
| 100 mm            | 1.2 m / 3.94 ft.          | 0.09x
| 200 mm            | 0.88 m / 2.89 ft.         | 0.24x             
| 300 mm            | 0.95 m / 3.12 ft.         | 0.34x             
| 400 mm            | 1.05 m / 3.44 ft.         | 0.41x             
