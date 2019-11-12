# Disaster Relief Call Center

# Run this script after (say) 100 calls but for demonstration purposes running it after 10 calls for testing
# severity 1 and number of calls data will bet trained to find the final urgency of disaster in a city

# All imports start

import pandas as pd
import numpy as np
from sklearn import preprocessing, neighbors

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

from sklearn.model_selection import cross_validate
# from sklearn import preprocessing,neighbors,cross_validation

# All imports end

# Read Severity1
severity1_df = pd.read_csv('processed_data/city_sev1.csv')
# Read number of calls
city_frequency = pd.read_csv('processed_data/indian_cities.csv')
average_sev_list = []
index = 0

# Training on city_sev2 to find the final severity2

final_severity = pd.read_csv("data sources/training/sev2_training.csv")
final_severity.replace('?', -99999, inplace=True)
X = np.array(final_severity[['Number_of_calls', 'Severity1']])
# print(X)
y = np.array(final_severity['Severity2'])

# KNN Algorithm implementation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Accuracy while finding the Final Severity of the place is : " +
      str(accuracy*100) + "%")

for i in range(len(city_frequency)):
    if (city_frequency['number'][i] != 0):  # If calls were made from a city
        c = city_frequency['City'][i]  # Store number of calls
        sev_sum = 0
        avg_sev = 0
        for k in range(len(severity1_df)):
            if(severity1_df['City'][k] == c):
                sev_sum = sev_sum + severity1_df['Severity1'][k]
        total_calls = list(severity1_df['City']).count(c)
        print("Total calls made from : " + str(c) +
              " till now : " + str(total_calls))
        # Calculate average
        avg_sev = sev_sum/total_calls
        city_sev2_df = pd.read_csv('processed_data/city_sev2.csv')

        city_sev2_df.loc[index, 'City'] = c
        city_sev2_df.loc[index,
                         'Number_of_calls'] = city_frequency['number'][i]
        city_sev2_df.loc[index, 'Severity1'] = avg_sev

        city_sev2_df.to_csv('processed_data/city_sev2.csv', index=False)

        index = index + 1
        average_sev_list.append(avg_sev)

# Predicting final severity2 and adding it into new csv file with city

final_prediction = pd.read_csv('processed_data/city_sev2.csv')
analysis_df = pd.read_csv('processed_data/analysis.csv')
index = 0
# print("Final prediction of the cities ")

for j in range(len(final_prediction)):
    num = final_prediction['Number_of_calls'][j]
    sev = final_prediction['Severity1'][j]
    values = np.array([[num, sev]])
    values = values.reshape(len(values), -1)
    severity2 = (clf.predict(values))[0]
    # print(final_prediction['City'][j])
    # print(severity2)

    analysis_df.loc[index, 'City'] = final_prediction['City'][j]
    analysis_df.loc[index, 'Urgency'] = severity2
    analysis_df.to_csv('processed_data/analysis.csv', index=False)
    index = index + 1

print("\nRefer to analysis.csv to find the Urgency of places after all the calls are made. ")
