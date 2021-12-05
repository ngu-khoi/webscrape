# web-s41

web-s41 webscrapes data from greatschools.org in a semi-automated process.

## Installation

You must use Python 3.8 for the program to function and install the packages as described in imports. 3.7 does not work (otherwise you need to install appropriate packages).

You must use Google Chrome. You must also install the ChromeDriver for the appropriate version of chrome.
To find the appropriate version of chrome:
	Click on the Menu icon in the upper right corner of the screen.
	Click on Help, and then About Google Chrome.
	Your Chrome browser version number can be found here.
	
Place the .exe in the directory in your C:
/usr/bin/chromium/chromedriver.exe

This path is specifically used in the program. Change the path appropriately if you would like.

Do not change output write location.


## Usage

Run the program, and the automated web browser should pop up immediately. In the same folder as the program, a .csv file should appear. Use Notepad++ if you would like to observe live updates of the data.

Currently, the program is not truly self controlled due to an error that the program will run into approximately 4 times during runtime randomly. The program will quit; however, rerunning will continue updating the data file where it crashed.


## Issues

1) Several entries are messed up since when addresses are scrapped, there appears to be duplicated charateristics (which will appear on the .csv).
2) Runtime errors. I need to create a try except so user input is not required. In the meantime, the user will be required to manually run the program when an error is encountered.