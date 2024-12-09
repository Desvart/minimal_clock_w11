I like to hide my task bar in Windows because it takes too much place and I don't need to see it that often. The problem is that I would also like to always have the time displayed somewhere. The task bar has time and date displayed in it but since I hide it, I cannot see it at any moment without moving my mouse to the bottom part of the screen to unhide the task bar and display the clock. This small project create a discrete clock that automatically launch itself at Windows startup, without having the need to unhide the taskbar.

* Install Python 3+ with the tcl/tk and IDLE environment.
* Save the launch_clock.bat and clock.py in the same directory.
* Add the launch_clock.bat to the startup folder:
  ** Press Windows + R to open the Run dialog
  ** Type shell:startup and press Enter
  ** This opens the Startup folder
  ** Create a shortcut to your launch_clock.bat file in this folder:
    *** Right-click in the Startup folder
    *** Choose "New" → "Shortcut"
    *** Browse to your launch_clock.bat file
    *** Click "Next" and give it a name like "Minimal Clock"
    *** Click "Finish"

Note: Make sure to update the path in the batch file to match where you actually saved your clock.py file.

NB: This solution has been generated in a few minutes with Claude AI. To my knowledge, it works very well for my needs. Don't hesitate to improve it if needed.
