# Pyduino 

### Arduino Control using Python.

![arduino control](https://user-images.githubusercontent.com/64916997/81459438-5dfc1400-91b9-11ea-9d74-bc46d3f5dc73.png)

## User manual:

* [Download or clone repository](#setup)
* [Install the modules](#modules)
* [Connect and use](#usage)

### Setup

#### Go to a directory, in which you'd like to save it:
> `cd ~/Dir/Dir/dir`

#### Then clone the repository:
> `git clone https://github.com/Muhammadrasul446/Pyduino.git`

#### Or download .zip archive:
![zip](https://user-images.githubusercontent.com/64916997/81459886-62293100-91bb-11ea-8c42-8f355dc8c021.png)

### Modules

This program requires only two modules - [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) and [pyFirmata](https://pypi.org/project/pyFirmata/). You can install them straightly from terminal:

> `python -m pip install PySimpleGUI`

and:

> `python -m pip install pyFirmata`

[PySimpleGUI](https://pypi.org/project/PySimpleGUI/) requires another module, named [tkinter](https://wiki.python.org/moin/TkInter), it comes with python package, but it might be missing. In Windows you just install it like a python-module from the command line:

> `python -m pip install tkinter`

In Unix-like Systems u can install it like a package, from using your package manager:

> `sudo apt-get install python-tk`

### Usage

#### Board config

Before combining a program with your board, you need to upload a `StandardFirmata` sketch to your board. It comes with arduino example-sketches:

![StandardFirmata](https://user-images.githubusercontent.com/64916997/81460364-60ad3800-91be-11ea-9ca0-b596d00c166e.png)

#### Open the program

When you open, you'll see an input field, which is your serial port, a "Connect" button, which you should press after entering the serial port, 12 checkboxes, which are the states of 12 digital pins on your board, "Send" button, which changes the states of the pins according to checkboxes, and "Exit" button, which is the alternative for the red "cross" at the top right corner of the window.

Enjoy using! Hope it'll help you someway!!!


