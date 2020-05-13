# for UI:
import PySimpleGUI as sg
# for working with arduino:
import pyfirmata as pf

# any preferred appearance of the UI:
theme = 'DarkAmber'

# set the theme:
sg.theme(theme); del theme

# Boolean to check connection
connected = False

# VAriable to keep board's type and dictionaries for ports
board_type = " "
digital_ports = pwm_ports_values = pwm_ports = dict()


gitoverflow = [
		[sg.T("Github: Muhammadrasul446", size=(28, 1))],
		[sg.T("Stackoverflow: user:13490404", size=(28, 1))]
]

twittedin = [
		[sg.T("Twitter: A_M_R_4_4_6", size=(28, 1))],
		[sg.T("Linkedin: 6644821a9", size=(28, 1))]
]



select_win_lay = [
			[sg.T('Select your board:')],
			[sg.Button("Nano/Uno/Leonardo")],
			[sg.Button("Mega/Mega2560")]
]

window = sg.Window("Select your board", select_win_lay)



# keep the window open:
while True:

	event, values = window()
	if event in ("Nano/Uno/Leonardo", "Mega/Mega2560"):
		window.hide()
		if event == "Nano/Uno/Leonardo":
			digital_ports = {2:0, 4:2, 7:5, 8:6, 12:10, 13:11}
			pwm_ports = {3:1, 5:3, 6:4, 9:7, 10:8, 11:9}

			# Window laout for Arduino nano
			nano_col_1 = [
					[sg.CB("Port 2", size=(8, 1))],
					[sg.T("Port ~3", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
					[sg.CB("Port 4", size=(8, 1))],
					[sg.T("Port ~5", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
			]
			nano_col_2 = [
					[sg.T("Port ~6", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
					[sg.CB("Port 7", size=(8, 1))],
					[sg.CB("Port 8", size=(8, 1))],
					[sg.T("Port ~9", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
			]

			nano_col_3 = [
					[sg.T("Port ~10", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
					[sg.T("Port ~11", size=(8, 1)), sg.Spin([i for i in range(0, 51)], size=(2, 2))],
					[sg.CB("Port 12", size=(8, 1))],
					[sg.CB("Port 13", size=(8, 1))]
			]

			nano_win_layout = [

					[sg.T('Made by Muhammadrasul Abdulhayev')],

					[sg.T("Serial Port"), sg.In("/dev/ttyACM0", size=(20, 1), key='port'), sg.Button("Connect")],
					[sg.Column(nano_col_1),  sg.VerticalSeparator(pad=None), sg.Column(nano_col_2),  sg.VerticalSeparator(pad=None), sg.Column(nano_col_3)],
					[sg.Button("Send"), sg.Button("Exit")],

					[sg.Column(gitoverflow),  sg.VerticalSeparator(pad=None), sg.Column(twittedin)]

			]
			second_window = sg.Window('Pyduino', nano_win_layout)

		else:
			digital_ports = dict(zip([i for i in range(14, 54)], [i for i in range(12, 52)]))
			pwm_ports = dict(zip([i for i in range(2, 14)], [i for i in range(0, 13)]))

			# Window laout for Arduino Mega
			mega_col_1 = [
					[sg.T('Port ~' + str(i), size=(8, 1)), sg.Spin([j for j in range(0, 51)], size=(2, 2))] for i in range(2, 14)
			]
			mega_col_1.append([sg.CB("Port 14", size=(8, 1))])


			mega_col_2 = [
					[sg.CB('Port ' + str(i), size=(8, 1))] for i in range(15, 28)
			]

			mega_col_3 = [
					[sg.CB('Port ' + str(i), size=(8, 1))] for i in range(28, 41)
			]
			mega_col_4 = [
					[sg.CB('Port ' + str(i), size=(8, 1))] for i in range(41, 54)
			]

			mega_win_layout = [

					[sg.T('Made by Muhammadrasul Abdulhayev')],

					[sg.T("Serial Port"), sg.In("/dev/ttyACM0", size=(20, 1), key='port'), sg.Button("Connect")],
					[sg.Column(mega_col_1), sg.VerticalSeparator(pad=None), sg.Column(mega_col_2), sg.VerticalSeparator(pad=None), sg.Column(mega_col_3), sg.VerticalSeparator(pad=None), sg.Column(mega_col_4)],
					[sg.Button("Send"), sg.Button("Exit")],

					[sg.Column(gitoverflow),  sg.VerticalSeparator(pad=None), sg.Column(twittedin)]

			]
			second_window = sg.Window('Pyduino', mega_win_layout)
		# untill it's closed manually:
		while True:
			event, values = second_window.read()
			if event in (None, 'Exit'):
				window.close()
				break
			# setup the serial port:
			elif event == "Connect":

				if not connected:

					try:

						# define the 'board'-object
						if board_type == "nano":
							board = pf.Arduino(values["port"])
						else:
							board = pf.ArduinoMega(values["port"])
						sg.popup_ok("Connected")

						for i in pwm_ports.keys():

							# Get pwm pins of the board and fill the dictionary:
							pwm_ports_values[i] = board.get_pin("d:" + str(i) + ":p")

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
						pwm_ports_values[j].write(state)

				else:

					# If not connected
					sg.popup_error("Connect the serial port first!", text_color="red")


		second_window.close(); del second_window # when done, close.
	break

window.close()