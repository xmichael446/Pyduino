
# for UI:
import PySimpleGUI as sg

# for working with arduino:
import pyfirmata as pf

# any preferred appearance of the UI:
theme = 'DarkAmber'

# set the theme:
sg.theme(theme)

# Boolean to check connection
connected = False

# 12 ports to be contolled:
digital_ports = {2:0, 4:8, 7:9, 8:2, 12:7, 13:11}
pwm_ports = {3:4, 5:1, 6:5, 9:6, 10:10, 11:3}

board_get_pwm = dict()

# Window elements' position, type and values, where needed:
column_one = [

		[sg.CB("Port 2", size=(8, 1))],

		[sg.T("Port ~5", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],

		[sg.CB("Port 8", size=(8, 1))],

		[sg.T("Port ~11", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))]

]
column_two = [
		[sg.T("Port ~3", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
		[sg.T("Port ~6", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
		[sg.T("Port ~9", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],

		[sg.CB("Port 12", size=(8, 1))]

]
column_three = [
		[sg.CB("Port 4", size=(8, 1))],
		[sg.CB("Port 7", size=(8, 1))],

		[sg.T("Port ~10", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],

		[sg.CB("Port 13", size=(8, 1))]
]

gitoverflow = [
		[sg.T("Github: Muhammadrasul446", size=(28, 1))],
		[sg.T("Stackoverflow: user:13490404", size=(28, 1))]
]

twittedin = [
		[sg.T("Twitter: A_M_R_4_4_6", size=(28, 1))],
		[sg.T("Linkedin: 6644821a9", size=(28, 1))]
]

window_layout = [

		[sg.T('Made by Muhammadrasul Abdulhayev')],

		[sg.T("Serial Port"), sg.In("/dev/ttyACM0", size=(20, 1), key='port'), sg.Button("Connect")],
		[sg.Column(column_one),  sg.VerticalSeparator(pad=None), sg.Column(column_two),  sg.VerticalSeparator(pad=None), sg.Column(column_three)],
		[sg.Button("Send"), sg.Button("Exit")],

		[sg.Column(gitoverflow),  sg.VerticalSeparator(pad=None), sg.Column(twittedin)]

]

# create a window object:
window = sg.Window('Pyduino', window_layout) 

# keep the window open:
while True:

	event, values = window()

	# untill it's closed manually:
	if event in (None, 'Exit'):
		break

	# setup the serial port:
	elif event == "Connect":

		if not connected:

			try:

				# define the 'board'-object
				board = pf.Arduino(values["port"])
				sg.popup_ok("Connected")

				for i in pwm_ports.keys():

					# Get pwm pins of the board and fill the dictionary:
					board_get_pwm[i] = board.get_pin("d:" + str(i) + ":p")

				connected = True

			# if serial port is not defined or empty
			except:

				# let the user know
				sg.popup_error("Serial port is invalid!!!", text_color="red")

				connected = False

		else:
			# If already connected:
			sg.popup_ok("Already connected")

	# change states of pins, according to checkboxes:
	elif event == "Send":

		if connected:

			# digital pins:
			for i in digital_ports.keys():

				state = values[digital_ports[i]]
				board.digital[i].write(state)

			# pwm pins:
			for j in pwm_ports.keys():

				state = float((values[pwm_ports[j]])/50)
				board_get_pwm[j].write(state)

		else:

			# If not connected
			sg.popup_error("Connect the serial port first!", text_color="red")


window.close(); del window # when done, close.