# Disaster-relief-call-center

A disaster relief call center project using KNN algorithm and some NLP tools

## How to set up virtual environment

    >python -m venv env

To activate the environment

    >env\Scripts\Activate

To deactivate the environment

    >Deactivate

## What all to set up before

    >pip install pandas
    >pip install numpy
    >pip install scikit-learn
    >pip install PyAudio
    >pip install SpeechRecognition
    >pip install textblob
    >python -m textblob.download_corpora
    >pip install selenium

You can download [chrome driver from here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Check which version of chrome you are running (help -> about Google Chrome) and download corresponding driver and copy it to your repository.

At the time of developing, Chrome version 78 was utilised.

## How to run the project

There are two methods to convert audio from microphone to text:

1. Python SpeechRecognition module
2. Web Scraping using Selenium of [speechnotes](https://speechnotes.co/)

I have commented Method 1 in severity1.py as it wasn't giving accurate enough result for my particular accent. You can use that also if you wish so.

If proceeding with Method 2, then step to follow:

1. First of all run speechtotext.py
2. Then run severity1.py file
3. Then run severity2.py file

## Assumed call parameters

1. The caller should specify from which city he/she is calling

2. The caller should specify his/her problem clearly

3. The caller should tell what he/she needs

## How this works

### How speechtotext.py works

Using Selenium, a chrome instance (version 78) is created by python and taken to [speechnotes](https://speechnotes.co/). You have to manually select to allow Chrome to record audio in the prompt. After that my program takes care to itself click on "Start Recording" button and you just have to speak what you wanted to convert to text.

#### Why use Selenium instead of BeautifulSoup

As converting recorded voice to text is done and appended to the website using Javasript, we can't directly scrape the contents using BeautifulSoup. Thus we need to mimic the environment in which javascript can be run using Selenium.

#### How long does it listen to convert what i spoke to text

Currently, speechtotext.py listens for 10 seconds. You may want to increase this duration if you are on slow internet.
Alternatively, in the Method 1 (using SpeechRecognition library), it is programmed to listen as long as someone is speaking.

### What is Severity 1

This is the severity of each call received at the call center.

### What is Severity 2

This is the severity per city of combined calls received at the call center.

### What all NLP tools have been utilised

1. Part of Speech Tagging
2. Noun Phrase Extraction
3. Lemmatization of Verbs and Adjectives

[![ForTheBadge built-by-developers](https://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/pranshupranjal)
