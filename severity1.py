# Disaster Relief Call Center

# this script runs whenever we receive a call

# All imports start

import speech_recognition as sr
import pandas as pd
import numpy as np
from sklearn import preprocessing, neighbors

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.model_selection import cross_validate

# All imports end

# Read names of all(most of them anyways) cities of India
city_freq = pd.read_csv('data.csv')

# list of all the cities present in the database
city_list = list(city_freq.City)

# List of all words related to food, medicine, rescue
food_words = ['food', 'hungry', 'apples', 'samples',
              'eat', 'drink', 'bread', 'refreshments']
medical_words = ['medicine', 'hospital', 'bandages', 'dead', 'splint',
                 'dose', 'doctor', 'nurse', 'bleeding', 'cut', 'injury', 'amputate', 'drug','inflammation']
rescue_words = ['rescue', 'stuck', 'flood', 'take', 'save',
                'emergency', 'injury', 'survivor', 'dead', 'wreck']

# Speech to Text portion

# r = sr.Recognizer()
# r.energy_threshold = 1000
# mic = sr.Microphone()
# with mic as source:
#     print("Say something...")
#     audio = r.listen(source)
#     print("Sound Processed")

# isaid = r.recognize_google(audio)

# take care of commas after the words
isaid = "I am from vellore please i need medicine and want to go to the hospital . Please I'm hungry i need food please rescue"

list_of_words = isaid.split(" ")
said_cities = []

print("Call converted to text : "+isaid)

# Just for Check:
# print("list of word",list_of_words)
# print("city list",city_list)

# Find from where the call has been recieved
for word in list_of_words:
    if word.lower() in city_list:
        said_cities.append(word)

# This is for the case user keeps repeating the city name due to stress
# like help needed at ghaziabad. I am from ghaziabad. this problem happened....

said_cities = set(said_cities)

print("Location of the Victim : " + str(said_cities))

# Updating city numbers in csv file to calculate severity 2
for city in said_cities:
    # Finding index of the city in the csv file data.csv
    index_city = city_list.index(city.lower())
    city_freq.loc[index_city,
                  'number'] = city_freq.loc[index_city, 'number'] + 1
city_freq.to_csv('data.csv', index=False)

# Calculating severity1 for every call and adding in another dataset , for that we have to train for severity 1

help_dataset = pd.read_csv("sev1_training.csv")
help_dataset.replace('?', -99999, inplace=True)

# Drop rightmost column for calculating x values and consider the rest of the columns
X = np.array(help_dataset.drop(['Severity1'], 1))
# Consider only the rightmost column for calculating y values
y = np.array(help_dataset['Severity1'])


# KNN Algorithm implementation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Accuracy in finding the Severity of the call is : " + str(accuracy*100) + "%")

# Considering the values in binary
f = 0  # food
m = 0  # medicine
r = 0  # rescue
n = 1  # not known
for word in list_of_words:
    if word.lower() in food_words:
        f = 1
    elif word.lower() in medical_words:
        m = 1
    elif word.lower() in rescue_words:
        r = 1
# Just for checking
# print(f,m,r,n)
parameters = np.array([[f, m, r, n]])
parameters = parameters.reshape(len(parameters), -1)
severity1 = (clf.predict(parameters))[0]

# Print severity of this particular call
print("Severity of this call : " + str(severity1))

# Append this call details (city, severity) to the city_sev1 file
city_sev1_df = pd.read_csv('city_sev1.csv')
index = len(city_sev1_df)

# Considering that the first city mentioned by the user is where he/she resides
city_sev1_df.loc[index, 'City'] = list(said_cities)[0]
city_sev1_df.loc[index, 'Severity1'] = severity1

# Push to csv file
city_sev1_df.to_csv('city_sev1.csv', index=False)
