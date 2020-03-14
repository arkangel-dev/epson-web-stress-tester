from flask import Flask, json, abort, request, render_template, jsonify
import json
import random
import requests
from lxml import html
from flask import jsonify
import PrinterLibrary

api = Flask(__name__)

@api.route('/')
def mainPage():
	return render_template('index.html')

@api.route('/randomt')
def randomt():
	infile = open('random-text.json')
	data = json.load(infile)
	return jsonify(random.choice(data))


@api.route('/printer')
def getPrinter():
	
	printerip = request.args.get('ipaddress')
	action = request.args.get('action')
	
	try:
		printer = PrinterLibrary.Printer(printerip)
		if action:
			# Print Content
			if action == "PrintContent":
				content = request.args.get('content')
				if content:
					printer.Print(content)
					return "Done"
				else:
					return abort(500, description="Needs Argument 'content' : Has to be stirng")

			# Run Stress Test
			if action == "StressTest":
				lines = request.args.get('lines')
				if lines:
					printer.StressTest(int(lines))
					return "Done"
				else:
					return abort(500, description="Needs argument lines : Has to be of type 'Integer'")

		else:
			return abort(500, description="Needs argument action : Can be 'PrintContent' | 'StressTest'")

	except Exception as e:
		return abort(500, description="Shit Went Wrong : " + str(e))

@api.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

api.run(host="0.0.0.0", port=80)

