# MPL115A2
You can find my code to acquire data from a MPL115A2 I2C Barometer with a rpi 3 model B.

![MPL115A2](MPL115A2.png)

## Installation
Before using this code run these commands lines to download and install smbus library on your Raspberry pi.
- Download: 
  ```cpp 
  sudo apt-get install build-essential libi2c-dev i2c-tools python-dev libffi-dev
  ```
- Installation: 
  ```cpp
  pip install cffi
  ```
  ```cpp
  pip install smbus-cffi
  ```
  More informations: 
  https://pypi.python.org/pypi/smbus-cffi/0.5.1

## How to use it
- Easy way: 
  - Download the code in your Raspberry pi.
  - Download the launcher.
  - Run the launcher. (Both files must be in the same directory)

- Other way:
  - Download the code in your Raspberry pi.
  - Open a terminal.
  - Go into the directory that contain the downloaded file.
  - Run the command: 
    ```cpp 
    python MPL115A2.py
    ```
    
## Wiring
  ![Wiring](Wiring.png)
  
## Initial code
https://github.com/ControlEverythingCommunity/MPL115A2/blob/master/Python/MPL115A2.py
