from escpos.printer import Network
from random import randrange
import qrcode
import time
import re

class Printer:
	printer = None

	def __init__(self, ip):
		self.printer = Network(ip)

	def Test(self):
		return True

	def Print(self, text):
		text = text.replace("\\n", "\n")
		# self.printer.set(font='b')
		self.printer.text(text)
		self.printer.cut()

	def PrintBoxTag(self, caseNumbers, Organisation, inDate, outDate, Contents, Serials):
		img = qrcode.make("ID" + str(caseNumbers), box_size=8)
		img.save("out.png")
		self.printer.set(align=u'center', font='a')
		self.printer.text("Hospitality Technology\n")
		self.printer.text("Hardware Department\n")
		self.printer.image("out.png")
		self.printer.set(align=u'left')

		caseNumberString = ""
		for caseNo in caseNumbers:
			caseNumberString += "   " + caseNo + "\n"

		contentString = ""
		for hardware in Contents:
			contentString += "   " + hardware + "\n"

		serialString = ""
		for serial in Serials:
			serialString += "   " + serial + "\n"

		self.printer.text("Property : " + Organisation + "\n")
		self.printer.text("Received Date  : " + inDate + "\n")
		self.printer.text("Released Date  : " + outDate + "\n")
		self.printer.text("Case No		:\n")
		self.printer.text(caseNumberString + "\n")
		self.printer.text("Contents	   :\n")
		self.printer.text(contentString + "\n")
		self.printer.text("Serials		:\n")
		self.printer.text(serialString + "\n")
		self.printer.cut()

	def StressTest(self, line_count):
		chararr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
		self.printer.text("Running Random Character Print Test : \n")
		self.printer.text("--------------------------------------\n\n\n")
		for y in range(line_count):
			string = ""
			for x in range(42):
				string += chararr[randrange(0, len(chararr) - 1)]
			self.printer.text(string)
		self.printer.text("\n\n")
		self.printer.cut()