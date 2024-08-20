# PicoSDSave

An extremely basic program to send files to an SD card via a Pi Pico.

## Setup

1. Get MicroPython onto your pi.
2. Place [base64.py](https://github.com/micropython/micropython-lib/blob/master/python-stdlib/base64/base64.py) in this folder and rename to `b64.py`.
3. Rename `private.py.example` to `private.py` and fill in the relevant details.
4. Copy everything onto your pi, and either run `app.py` or rename it to `main.py` to run on every boot.

## Pins

First, you need an SD Card reader. Get one like this: 

![image of a micro sd card reader with SPI interface and 5v input](https://m.media-amazon.com/images/I/71MyX+yo7oL._AC_SX450_.jpg)

The exact design and brand is ireelevant, but make sure it's 5v in and SPI.

- Connect Pico VBUS to Reader VCC.
- Connect Pico Ground to Reader Ground.
- Connect Pico pin 2 (GP1) to Reader CS.
- Connect Pico pin 4 (GP2) to Reader SCK.
- Connect Pico pin 5 (GP3) to Reader MOSI.
- Connect Pico pin 6 (GP4) to Reader MISO.

## Usage

1. Give the Pi Power, and let it connect to the network you put in the `private.py` file.
2. Obtain its IP, either through router settings, or a similar route.
3. Open this IP in a browser and upload your files.
4. Find your files on the SD card when you remove it from a powered off Pico.
   - The filename of it will be `[timestamp of upload].bin` - the `.bin` extension is due to the file type being unknown.

## License/Attribution

PicoSDSave is licensed under the terms of GNU AGPL 3.0.

`sdcard.py` is a very slightly modified version of [micropython's `sdcard.py`](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/storage/sdcard/sdcard.py) which seems to be MIT Licensed.

