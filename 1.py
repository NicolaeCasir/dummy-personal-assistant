import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr
from os import path
import re

wikipedia.set_lang("ro")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.aif")

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Listening.....")
		audio = r.listen(source)
		try:
			print("Regognizing....")
			text = r.recognize_google(audio, language="ro")
			print('You said: ' + text)
			if text == "stop":
				print("Program will exit.")
				break
			elif text == 'citește din fișier':
				with sr.AudioFile(AUDIO_FILE) as source:
					print("Please wait... reading from file...")
					audio = r.record(source)
					text = r.recognize_google(audio, language="ro")
					print('Text from your FILE:\n ' + text + "\n")
			else:
				window = Tk()
				window.geometry("700x600")
				try:
					app_id = "V67GTV-29YYGUQ2GX"
					client = wolframalpha.Client(app_id)
					res = client.query(text)
					answer = next(res.results).text
					print("Answer from Wolfram|Alpha:")
					print(answer)
				except Exception as e:
					print("No results from Wolfram|Alpha. Trying wikipedia...")
					answer = wikipedia.summary(text)
					print("Answer from Wikipedia:")
					print(answer)
		except Exception as e:
			print(e)
			print("Searching similar pages close to your request....")
			answer = wikipedia.search(text)
			print(answer)
