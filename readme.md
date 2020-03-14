# EPSON Printer Stress Tester

This is a web based stress tester for EPSON printers with ethernet interface cards. This is written with Python and Flask.

## Installation

Install the following libraries :

```shell
pip install flask
pip install lxml
pip install python-escpos
```

Replace the IP address with the server IP address in the `templates\index.html` line 125.

Now run main and the  server should be up and running on port 80