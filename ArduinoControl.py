# for UI:
import PySimpleGUI as sg

# for working with arduino:
import pyfirmata as pf

# any preferred appearance of the UI:
theme = 'DarkBlack1'

# set the theme:
sg.theme(theme)

# 12 ports to be contolled:
digital_ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Window elements' position, type and values, where needed:
window_layout = [  
		[sg.T('Arduino Control using Python!!!')],
		[sg.T("Serial Port"), sg.In("COM", size=(20, 1)), sg.Button("Connect")],
		[sg.CBox("Port 2", size=(8, 1)), sg.CBox("Port 3", size=(8, 1)), sg.CBox("Port 4", size=(8, 1))],
		[sg.CBox("Port 5", size=(8, 1)), sg.CBox("Port 6", size=(8, 1)), sg.CBox("Port 7", size=(8, 1))],
		[sg.CBox("Port 8", size=(8, 1)), sg.CBox("Port 9", size=(8, 1)), sg.CBox("Port 10", size=(8, 1))],
		[sg.CBox("Port 11", size=(8, 1)), sg.CBox("Port 12", size=(8, 1)), sg.CBox("Port 13", size=(8, 1))],
		[sg.Button("Send"), sg.Button("Exit")]
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
		board = pyfirmata.Arduino(values[0])

	# change states of pins, according to checkboxes:
	elif event == "Send":

		for i in digital_ports:
			for j in values:
				board.digital[i].write(values[j + 1])


window.close() # when done, close.