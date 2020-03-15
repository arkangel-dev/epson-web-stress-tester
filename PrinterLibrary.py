from escpos.printer import Network
from random import randrange, choice
import qrcode
import time
import re


class Printer:
	printer = None

	def __init__(self, ip):
		self.printer = Network(ip)

	def Test(self):
		return True

	def Print(self, text, convertesc, cutprint, selfont):
		if self.ConvertBool(convertesc):
			text = text.replace("\\n", "\n")
			text = text.replace("\\t", "\t")
			text = text.replace("\\\\", chr(92))
			# text = text.replace("\\", "***")

		self.printer.set(font=selfont)
		self.printer.text(text)
		self.printer.set(font='a')

		if self.ConvertBool(cutprint):
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
		for y in range(line_count):
			string = ""
			for x in range(42):
				string += chararr[randrange(0, len(chararr) - 1)]
			self.printer.text(string)
		self.printer.text("\n\n")
		self.printer.cut()

	def AdvancedStressTest(self, line_count, infont, alphabet, numbers, specialChars, CutAfterPrint):

		alphabet = self.ConvertBool(alphabet)
		numbers = self.ConvertBool(numbers)
		specialChars = self.ConvertBool(specialChars)
		CutAfterPrint = self.ConvertBool(CutAfterPrint)

		finalArray = []

		alphabetArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		numberArray = ["1","2","3","4","5","6","7","8","9","0"]
		specialCharsArray = ["!","@","#","$","%","^","&","*","(",")","_","-", "=","+","\\","/","<",">",".",",",'"',"'",";",":","[","]","|"]

		if numbers:
			finalArray.extend(numberArray)

		if alphabet:
			finalArray.extend(alphabetArray)

		if specialChars:
			finalArray.extend(specialCharsArray)

		self.printer.set(font=infont)

		for y in range(int(line_count)):
			string = ""
			for x in range(42):
				string += choice(finalArray)
			self.printer.text(string)

		if CutAfterPrint:
			self.printer.text("\n\n")
			self.printer.cut()

		self.printer.set(font='a')

	def ConvertBool(self, instr):
		if (instr.__eq__("false")):
			return False
		return True