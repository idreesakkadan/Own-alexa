# Own-alexa

Just Know These Terms:
Module/Library:
A predefined or prewritten code by someone else that we can use in our project for free.
Class:
An OOP concept that allows us to group a bunch of code and is like a blueprint to create objects. This makes a code reusable.
Object:
An instance of a class that can be used to access the attributes and methods of a class.
Alexa Has Only 2 Tasks:
1. Listening
Listening to your command is the most basic functionality of any virtual assistant, like: “Hey Alexa, play music,” “Hey Alexa, what’s the time?”
Alexa has to listen to your command, understand it, and then do some action.
2. Speaking
Once Alexa listens and understands your command, it performs some action based on it. While doing that, it responds to you by speaking otherwise it’ll be jobless.
Let’s Implement Those Two Features:
To implement the above two features, we’ll need two Python modules:
SpeechRecognition
Python Text-To-Speech (pyttsx3)
1. SpeechRecognition
This library performs speech recognition. It’ll help the assistant listen to our commands, understand them, and act accordingly.
Anything third-party needs some kind of installation. You are the third-party of your mom and dad. They did some kind of installation. Ask them what.
Let’s install this third-party module using the command below, on your terminal:
pip install SpeechRecognition
Once installed, we can use it in our project. While working with this module, there are three important things that we’ll need:
a. The Recognizer class: This is the main class of this module which has all the major functions to help us create a speech recognition application.
Before we can use it, first we’ll need to initialize it and create its object:
r = sr.Recognizer()
Here, ‘r’ is just the name given to the object. It can be any valid Python variable name.
b. Microphone access: As the assistant needs to listen to your command, you’ll need to give it the power to access the microphone of your machine. You can do that with the help of the Microphone class:
# open the microphone and start recording
with Microphone() as source:  
   # do things here - ``source`` is the Microphone instance created above
   pass
c. Listening to user speech: Once it has the microphone access, the final step is to listen to your command. You can do that with the help of the listen() method provided by the Recognizer class:
# Listening to the user speech
# Accepts the audio source as the parameter
r.listen(source)
That’s how you can work with Speech Recognition in Python. With this basic knowledge of this module, let’s move ahead.
2. Python Text-To-Speech (pyttsx3)
This is the Text-to-Speech (TTS) library for Python 2 and Python 3 and works without an internet connection or any delay.
Since it’s a third-party module, first you’ll have to install it:
pip install pyttsx3
Your assistant can finally speak with the help of this module.
Secret: We’re just converting text to speech here.
Everything else is now a piece of cake for you. First, you’ll to initialize the pyttsx3 module using the init() method and create its object. We can then use its various functions to convert text to speech:
engine = pyttsx3.init()
engine.say("Text to Speak Here")
engine.runAndWait()
Here, the say() does the major job of converting text to speech, and the runAndWait() waits for the module to complete speaking a particular sentence before doing some other task.
With the basic knowledge of these two modules, let’s move ahead and finally start the fun part.
