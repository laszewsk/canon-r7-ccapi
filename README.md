# canon-r7-ccapi

## The problem

Many people noticed that the regular EOS Utility program has issues
on some Macs. This happens only via WiFi. The USB connection works fine.
However, we like to be able to access the Cannon cameras via WiFi read-on.
Furthermore, not all features are supported on Android apps interfacing with 
the canon camera so this is unfortunately yet not an option.
I use it to control focus bracketing from a computer.

Please note this only works for the models as documented at
* https://developers.canon-europe.com/developers/s/article/Latest-CCAPI
* Version: 1.3.0 (Released on 12th December 2022)

This includes:

* EOS R6 Mark II,
  EOS R7,	
  EOS R10,	
  EOS R3,
  EOS M50 Mark II,	
  EOS R5,
  EOS R6,
  EOS 850D,	
  EOS-1D X Mark III, 
  EOS M200,
  EOS 90D,
  EOS M6 Mark II,
  PowerShot G5 X Mark II,
  PowerShot G7 X Mark III,
  EOS 250D,
  EOS RP,
  PowerShot SX70 HS

Note that you need to likely update your firmware. Firmware update is rather simple on the Canon cameras, you download it, put it on your SD card, select firmware update then wait patiently when done. Make sure you have a fully charged battery. Do not power down during firmware upgrade. Read the canon instructions for this,

## The solution

The method chosen here uses the official CCAPI that relies on a REST service
calls in the network shared between the camera and the computer. The following
features are available:

* Elementary Python library to control many of the camera
* Elementary GUI interface to run the program from a GUI
* Ability to run the GUI on Linux, macOS, Windows 10, Windows 11
* Expandable
* demonstration on how to use the library in jupyter notebooks so you can create easily interactive workflows.

For example, With this GUI it is possible to conduct focus bracketing remotely. Many
features of the camera can be controlled remotely.

As the program uses CCAPI it can be likely used for other cameras also.
Make sure your camera is compatible

... more will be added here

## Install

```bash
$ git clone https://github.com/laszewsk/canon-r7-ccapi.git
$ cd canon-r7-ccapi
$ pip install -r requirements.txt
$ export CANON_IP=<Your canon camera ip address>
$ make
```

Those will install and run the program using a GUI.

## Plan

* manual
* documentation of the API
* writing an article for a hacker magazine/web site
* showcasing the macro stand
* evaluate integration with WeMacro

