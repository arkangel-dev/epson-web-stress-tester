# EPSON Printer Stress Tester

This is a web based stress tester for EPSON printers with ethernet interface cards. This is written with Python and Flask.

## Installation

Install the following libraries :

```shell
pip install flask
pip install python-escpos
```

Replace the IP address with the server IP address in the `templates\index.html` JavaScript tag (line 125). Now run main and the  server should be up and running on port 80.

## Usage
### Stress Test
Generates random text on the server side and have it sent to the printer. Can be used to test a printers endurance to long print sessions.

IP Address: IP Address of the server.
Number of Lines: Number of lines to send to the printer
Font: Font of the content sent to the printer. Can be either A or B. A is normal and B is small size
Include Alphabet: Include Alphabet characters in the random data.
Include Numbers: Include Numbers in the random data.
Include Special Characters: Include Special Characters int the random data.
Cut after Print: Cut the paper after printing test data.

### Data Print Test
Sends the printer content from the text area. Can be used to see how a specific content looks.

IP Address: IP Address of the server.
Print Data: Content to be sent to the server.
Font: Font of the content sent to the printer. Can be either A or B. A is normal and B is small size
Cut after Print: Cut the paper after printing test data.
Convert esc characters: Converts escape characters to actual escape characters
Load Random Text: Gets random data from the `random-text.json` file.