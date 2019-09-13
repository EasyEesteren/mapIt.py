#!/usr/bin/env python3
#Program takes command line arguments as the input for the address finder
#Else if no command line args given then the user is prompted for input
#Else if no input is given the program checks the clipboard

import webbrowser, sys, pyperclip

if (len(sys.argv) > 1):
	address = "".join(sys.argv[1:])
elif (len(sys.argv) == 1):
	address = input("Please input an address for Google Maps:")
else:
	address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+ address)