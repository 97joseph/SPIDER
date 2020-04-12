import webbrowser
import sys

if len(sys.argv)>1:
                address=''.join(sys.argv[1:])
else:
      address=pyperclip.paste()
      print("The address is not defined")

webbrowser.open("https://www.google.com/maps/place"+address)
