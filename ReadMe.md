AUTO CAMERA VIEWER FOR UBUNTU

This project creates a startup script that automatically opens the first camera in your system
and shows the output frames in a window. You can close the window by 'q' key.

To set the startup script in your system follow the following guide.

1- GUI(Tested in Ubuntu 20.04.6 LTS)

run gnome-session-properties on terminal, a gui window will be opened.

Click Add button to add new action.

Name: Enter a name for your script. Ex: Lolo

Command: Enter the full command to run your Python script. For example, if your script is located in the ~/Documents directory and is named auto_cam.py, enter python3 /home/your_username/Documents/auto_cam.py

Comment: Enter a brief description of what your script does (optional).


2- Command line(Experimental)

If you prefer to use the command line instead of the GUI, you can add your script to the ~/.config/autostart/ directory by creating a .desktop file with the following contents:

	[Desktop Entry]
	Type=Application
	Exec= python3 /home/your_username/Documents/auto_cam.py
	Hidden=false
	NoDisplay=false
	X-GNOME-Autostart-enabled=true
	NameEnter a name for your script. Ex: Lolo
	Comment=Description of your script (optional)

Save the file with a .desktop extension in the ~/.config/autostart/ directory.
Ex: auto_cam.desktop


