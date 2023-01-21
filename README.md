# canon-r7-ccapi

## The problem

Many people noticed that the regular EOS Utility program has issues
on some Mac's. This happens only via WiFi. The USB connection works fine.
However we like to be able to access the Cannon cameras via WiFi read on.
Furthermore, not all features are supported on Android apps interfacing with 
the canon camera so this is unfortunatly yet not an option.
I use it to control focusbracketing from a computer.

Please note this only works for the models as documented at
* https://developers.canon-europe.com/developers/s/article/Latest-CCAPI
for Version: 1.3.0 (Released on 12th December 2022)

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

Note that you need to likely update your frmware. Firmware update is rather simple on the Canon cameras, you download it, put it on an your sd card and select firmware update, than you wait paitently when done. Make sure you have fully charde battery. DOw not power down during firmware upgrade. Read the canon instructions for this,

## The solution

The method chosen here uses the official CCAPI that relies on REST service
calls in the network shared between the camera and the compter. The following
features are available:

* Elementary Python library to control many of the camera
* Elementary GUI interface to run the program from a GUI
* Ability to run the GUI on Linux, macOS, Windows 10, Windows11
* Expandable
* demonstration on how to use the library in jupyter notebooks so you can create easily interactive workflows.

For example, With this GUI it is possible to conduct focus brackating remotely. Many
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

## Lens simulator

* Lens Simulator <https://www.samyanglens.com/en/product/simulator/lens.php>

## Common less expensive lenses

[RF 100=400mm f5.6-8](https://www.usa.canon.com/shop/p/rf100-400mm-f5-6-8-is-usm?color=Black&type=New)
$500

| Focal length      | Minimum focusing distance | Magnification
|-------------------|---------------------------|---------------|
| 100mm            | 1.2 m / 3.94 ft.          | 0.09x         |
| 200mm            | 0.88 m / 2.89 ft.         | 0.24x         |           
| 300mm            | 0.95 m / 3.12 ft.         | 0.34x         |          
| 400mm            | 1.05 m / 3.44 ft.         | 0.41x         |         

[RF-S18-150mm F3.5-6.3](https://www.usa.canon.com/shop/p/rf-s18-150mm-f3-5-6-3-is-stm?color=Black&type=New)
$500
[Instructions](https://sg.canon/en/support/0304424001?model=5564C)

| **AF
Mode**            |                     |                |                |                   |
|------------------------|---------------------|----------------|----------------|-------------------|
| Focal Length           | 18mm               | 35mm          | 50mm          | 150mm            |
| Min. Focusing Distance | 0.17 m              | 0.17 m         | 0.18 m         | 0.45 m/1.48 ft.   |
| ...                    | 0.56 ft.            | 0.56 ft.       | 0.59 ft.       | 0.45 m/1.48 ft.   |
| Max. Magnification     | 0.20x               | 0.36x          | 0.44x          | 0.31x             |
| Field of View          | ~118x76mm       | ~64x42mm   | ~51x34mm   | ~72x48mm       | 
| ...                    | ~5.12x2.99 in.   | ~2.21x1.65 in. | ~2.01x1.34 in. | ~2.83x1.89 in. | 
| **MF
Mode**            |                     |                |                |                   | 
| Focal Length           | 18mm               | 35mm          | 50mm          | 150mm            |                    
| Min. Focusing Distance | 0.12 m              | 0.13 m         | 0.18 m         | 0.45 m/1.48 ft.   |      
| ...                    | 0.39 ft.            | 0.43 ft.       | 0.59 ft.       | 0.45 m/1.48 ft.   |      
| Max. Magnification     | 0.44x               | 0.59x          | 0.44x          | 0.31x             |     
| Field of View          | ~54x35mm        | ~39x26mm      | ~51x34mm      | ~72x48mm       |
| ...                    | ~2.13x1.38 in.   | ~1.54x1.02 in. | ~2.01x1.34 in. | ~2.83x1.89 in. |

[RF800mm F11 IS STM](https://www.usa.canon.com/shop/p/rf800mm-f11-is-stm?color=Black&type=New)
$900

[Instructions](https://www.usa.canon.com/support/p/rf800mm-f11-is-stm#idReference%3Dmanuals)

Focus settings -- Full (6m-∞) -- 20m-∞ (does faster focus if set)

| Attributes             | RF600mm F11 IS STM       | RF800mm F11 IS STM       |
|------------------------|--------------------------|--------------------------|
| Focal Length/Aperture  | 600mm f/11               | 800mm f/11               |                        |                         |                          |
| Lens Construction      | 7 groups, 10 elements    | 8 groups, 11 elements    |                                 
| Minimum Aperture       | f/11                     | f/11                     |             
| Angle of View          |                          |                          |
| ... Horizontal         | 3° 30’                   | 2° 35’                   |     
| ... Vertical           | 2° 20’                   | 1° 40’                   |    
| ... Diagonal           | 4° 10’                   | 3° 5’                    |   
| Min. Focusing Distance | 4.5 m                    | 6.0 m                    |    
| ...                    | 14.76 ft.                | 19.69 ft.                |     
| Max. Magnification     | 0.14×                    | 0.14×                    |            
| Field of View          | ~254 × 169mm             | ~261 × 174mm             |                    
| Filter Diameter        | 82mm                     | 95mm                     |          
| Max. Diameter          | ~93mm                    | ~101.6mm                 |
| Length                 | ~199.5mm (retracted)     | ~281.8mm (retracted)     |
| Length                 | ~269.5mm (shooting)      | ~351.8mm (shooting)      |
| Weight                 | ~930 g/32.8 oz.          | ~1260 g/44.4 oz.         |
| Hood                   | ET-88B (sold separately) | ET-101 (sold separately) |
| Lens Cap               | E-82 II                  | E-95                     |
| Case                   | LZ1328 (sold separately) | LZ1435 (sold separately) |

[14MM F2.8 FULL FRAME ULTRA WIDE ANGLE](https://samyangus.com/collections/manual-focus/products/14mm-f2-8-full-frame-ultra-wide-angle)

| Attribute       | Value                    | 
|-----------------|--------------------------|
| Focal Length    | 14mm                     |
| Aperture        | F2.8 ~ 22                |
| View Angle APS- | 1:1.5 93.9° diagonal     |
| View Angle APS- | 1:1.6 89.9° diagonal     |
| Focus range     | infinity to 0.28m(0.9ft) |
