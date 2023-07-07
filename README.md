# autoSkill
Auto key presser
I was sick of rebuffing in Diablo 4 every 13 secs, so here is an auto key presser.

Description

The autoSkill tool is a user-friendly, customizable auto key presser written in Python. It leverages the power of the PyAutoGUI and Tkinter libraries to automate the task of pressing keys at specified intervals.

The tool provides a simple graphical user interface (GUI) where you can specify up to 5 keys to be pressed and their corresponding frequencies. This allows for a versatile range of applications beyond just Diablo 4. You can use it for any task requiring automatic key pressing, from gaming to software testing.

The key-pressing operation can be started or stopped at any time using the Start and Stop buttons on the GUI. There's also a built-in fail-safe: moving the mouse to the upper left corner of the screen will trigger an exception and stop the key pressing.

Usage

Clone the repository to your local machine.
Navigate to the directory and run pip install -r requirements.txt to install the required Python packages.
Run python autoSkill.py to start the program.
Enter the keys to be pressed and their frequencies in the GUI.
Click the Start button to begin auto key pressing.
Note
Please use responsibly and ensure that automating key presses doesn't violate the terms of service of the software you're using. The developer of autoSkill is not responsible for any consequences of misuse.

