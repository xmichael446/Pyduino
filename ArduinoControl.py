# for UI:
import PySimpleGUI as sg

# for working with arduino:
import pyfirmata as pf

# any preferred appearance of the UI:
theme = 'DarkBlack1'

# set the theme:
sg.theme(theme)

# Your Operating System. You can skip this, coz it's just for determining corect serial port

OS = "Unix"
port_annot = " "

if OS == "Unix":
	port_annot = "/dev/ttyACM0"
elif OS == "Windows":
	port_annot = "COM"
else:
	port_annot = "/dev/tty.usbserial"

# 12 ports to be contolled:
digital_ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Window elements' position, type and values, where needed:
window_layout = [  
		[sg.T('Arduino Control using Python!!!')],
		[sg.T("Serial Port"), sg.In(port_annot, size=(20, 1), key='port'), sg.Button("Connect")],
		[sg.CBox("Port 2", size=(8, 1)), sg.CBox("Port 3", size=(8, 1)), sg.CBox("Port 4", size=(8, 1))],
		[sg.CBox("Port 5", size=(8, 1)), sg.CBox("Port 6", size=(8, 1)), sg.CBox("Port 7", size=(8, 1))],
		[sg.CBox("Port 8", size=(8, 1)), sg.CBox("Port 9", size=(8, 1)), sg.CBox("Port 10", size=(8, 1))],
		[sg.CBox("Port 11", size=(8, 1)), sg.CBox("Port 12", size=(8, 1)), sg.CBox("Port 13", size=(8, 1))],
		[sg.Button("Send"), sg.Button("Exit"), sg.T(" ", size=(24, 1), key="error", text_color="red")]
]

# create a window object:
window = sg.Window('Arduino Control', window_layout) 

# keep the window open:
while True:
	event, values = window.read()
	# untill it's closed manually:
	if event in (None, 'Exit'):
		break

	# setup the serial port:
	elif event == "Connect":

		board = pf.Arduino(values["port"])

	# change states of pins, according to checkboxes:
	elif event == "Send":
		for i in digital_ports:
			j = 0
			while j < 12:
				board.digital[i].write(values[j])
				j += 1


window.close() # when done, close.