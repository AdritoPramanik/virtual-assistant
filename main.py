import sys

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import pywhatkit
import pyttsx3
import requests
from bs4 import BeautifulSoup
import re
from googlesearch import search
import selenium
from selenium import webdriver
import wolframalpha

warnings.filterwarnings('ignore')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 178)
engine.say("I am your soma")
engine.say("What can I do for you?")
engine.runAndWait()



def talk(text):
    engine.say(text)
    engine.runAndWait()


# Record it and return it as a string
def recordaudio():
    # Record audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something')
        audio = r.listen(source)

    # Use Google's speech recognition
    data = ' '
    try:
        data = r.recognize_google(audio)
        print('You said:' + data)
    except sr.UnknownValueError:
        print('google speech recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from google speech recognition service error' + e)

    return data

def open_application():
    text = recordaudio()
    if 'firefox' in text:
        os.open('firefox')

    if 'chrome' in text:
        os.open('chrome')

    if 'microsoft word' in text:
        os.open('microsoft word')

    else:
        talk("application not available")

# A function to get the virtual assistant response
def assistantresponse(text):
    print(text)

    # Convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # Save the converted audio to a file
    myobj.save('assistant_assistant.mp3')

    # Play the converted file
    os.system('start assistant_assistant.mp3')


def wakeFord(text):
    WAKE_WORDS = ['soma', 'piku', 'adi', 'ok computer', 'hey computer']  # A list of wake words

    text = text.lower()  # Converting the text to all lower cases

    # Check to see if the users command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # If the wake word isn't found in the text from the loop and so it returns false
    return False


# A function to get the current date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.now()
    weekday = calendar.day_name[my_date.weekday()]  # e.g.Friday
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    # A list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                      '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '. '


# A function to return a random greeting response

def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hello', 'greetings', 'hola', 'hey', ]

    # Greeting Responses
    greeting_responses = ['whats up?', 'hello', 'hey there', 'howdy']

    # If the users input is a greeting , then return a randomly chosen greeting

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(greeting_responses) + ' .'

    # If no greetings was detected then return an empty string
    return ''


# A function to get a persons first and last name from the text
def getperson(text):
    wordList = text.split()  # Splitting the text into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


def getthing(text):
    thingList = text.split()  # Splitting the text into a list of words

    for j in range(0, len(thingList)):
        if j + 2 <= len(thingList) - 1 and thingList[j].lower() == 'what' and thingList[j + 1].lower() == 'is':
            return thingList[j + 2]


def process_text():
    # Record the audio
    while True:
        text = recordaudio()

        # Check for wake words/phrases
        if wakeFord(text):

            # Check for greeting by the user
            talk(greeting(text) + ', ')

            # Check to see if the user said anything having to do with the date

            if 'date' in text:
                get_date = getDate()
                talk(get_date + '. ')

            # Check to see if the user said who is
            elif 'who is' in text:
                person = getperson(text)

                wiki = wikipedia.summary(person, sentences=2)
                talk(wiki + '. ')

            elif 'who are you' in text:
                talk('I am Soma. I am here to make your life easier. I can search the web for you')

            elif 'who made you' in text or 'created you' in text:
                talk('I have been created by Adrito Pramanik')

            # elif 'what is' in text:
            #     thing = getthing(text)
            #     print(thing)
            #     wikip = wikipedia.summary(thing, sentences=2)
            #     talk(wikip + '. ')

            elif 'play' in text:
                play1 = "play"
                song = text[text.index(play1) + len(play1):]
                print(song)
                talk('playing' + ' ' + song)
                pywhatkit.playonyt(song)

            elif 'weather' in text:
                in1 = "in"
                afterin = input("Enter:")  # text[text.index(in1)+ len(in1):]
                print(afterin)

                # city = afterin
                # search = "Weather in {}".format(city)
                # url = f"https://www.google.com/search?&q ={search}"
                # req = requests.get(url)
                # sor = BeautifulSoup(req.text, "html.parser")
                # temp = sor.find("div", class_='BNeawe').text
                # print(temp)
                talk('The temperature today is')
                pywhatkit.search(afterin)
                
            elif 'which is' in text:
                app_id = "L3Y2YJ-ATT484KU5W"
                client = wolframalpha.Client(app_id)

                indx = text.split().index('computer')
                query = text.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                talk("The answer is " + answer)
                print("The answer is " + answer)


            elif 'open' in text:
                open_application()

            elif 'calculate' in text:

                # write your wolframalpha app_id here
                app_id = "L3Y2YJ-ATT484KU5W"
                client = wolframalpha.Client(app_id)

                indx = text.split().index('calculate')
                query = text.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                talk("The answer is " + answer)
                print("The answer is " + answer)


            else:


                computer = "computer"
                after = text[text.index(computer) + len(computer):]
                print(after)
                try:

                    research_later = after
                    google_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw" \
                                    "=1366&bih=648&noj=1&q=" + research_later

                    page = requests.get(google_search)
                    soup = BeautifulSoup(page.content)
                    result = soup.get_text()
                    # if 'resultsVerbatim' in result:
                    res = "resultsVerbatim"

                    result1 = result[result.index(res) + len(res):]

                    punc = '''!()-[]{};:'"\/?@#$%^&*_<>~'''

                    for ele in result1:
                        if ele in punc:
                            result1 = result1.replace(ele, "")

                    if 'www' in result1:
                        result1 = result1.replace("www", ". According to www")
                        print(result1)
                        talk(result1)

                        # elif 'ans' in result1:
                        #     b = result1.replace("Ans", "Answer")
                        #     print(b)
                        #     talk(b)
                        #
                        # elif 'wikipedia' in result1:
                        #     c = result1.replace("wikipediaen.wikipedia.org", "According to wikipedia.wikipedia.org")
                        #     print(c)
                        #     talk(c)

                    else:
                        print(result1)
                        talk(result1)

                except:
                    pass
                    talk("cannot understand what you are searching for")
            # Have the assistant response back using audio and the the text from response


process_text()


