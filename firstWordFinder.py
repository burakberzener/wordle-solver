import string

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

import wordleDatabases

figure(figsize=(16, 10), dpi=80)
colors_1 = []
colors_2 = []
colors_3 = []
colors_4 = []
colors_5 = []

filename = wordleDatabases.DATABASE_TR_JSON_1

if filename.endswith(".txt"):
    df = pd.read_csv(filename, names= ['word'])
elif filename.endswith(".json"):   
    df = pd.read_json(filename)
    df.columns = ["word"]
    df["word"] = df["word"].str.lower()
    print(df.head())

letters_dictionary_1 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_2 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_3 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_4 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_5 = dict.fromkeys(string.ascii_lowercase, 0)

for word in df["word"]:
    #print(word)
    letters_dictionary_1[word[0]] += 1
    letters_dictionary_2[word[1]] += 1
    letters_dictionary_3[word[2]] += 1
    letters_dictionary_4[word[3]] += 1
    letters_dictionary_5[word[4]] += 1

print("First Letter Statistics: ", letters_dictionary_1)
max_key_1 = max(letters_dictionary_1, key=letters_dictionary_1.get)
for value in letters_dictionary_1.keys():
    if max_key_1 == value:
        colors_1.append("g")
    else:
        colors_1.append("b")
names_1 = list(letters_dictionary_1.keys())
values_1 = list(letters_dictionary_1.values())
plt.subplot(3, 2, 1)
plt.title("First Letter Statistics")
plt.bar(range(len(letters_dictionary_1)), values_1, tick_label=names_1, color= colors_1)


print("Second Letter Statistics: ", letters_dictionary_2)
max_key_2 = max(letters_dictionary_2, key=letters_dictionary_2.get)
for value in letters_dictionary_2.keys():
    if max_key_2 == value:
        colors_2.append("g")
    else:
        colors_2.append("b")
names_2 = list(letters_dictionary_2.keys())
values_2 = list(letters_dictionary_2.values())
plt.subplot(3, 2, 2)
plt.title("Second Letter Statistics")
plt.bar(range(len(letters_dictionary_2)), values_2, tick_label=names_2, color= colors_2)

print("Third Letter Statistics: ", letters_dictionary_3)
max_key_3 = max(letters_dictionary_3, key=letters_dictionary_3.get)
for value in letters_dictionary_3.keys():
    if max_key_3 == value:
        colors_3.append("g")
    else:
        colors_3.append("b")
names_3 = list(letters_dictionary_3.keys())
values_3 = list(letters_dictionary_3.values())
plt.subplot(3, 2, 3)
plt.title("Third Letter Statistics")
plt.bar(range(len(letters_dictionary_3)), values_3, tick_label=names_3, color= colors_3)

print("Fourth Letter Statistics: ", letters_dictionary_4)
max_key_4 = max(letters_dictionary_4, key=letters_dictionary_4.get)
for value in letters_dictionary_4.keys():
    if max_key_4 == value:
        colors_4.append("g")
    else:
        colors_4.append("b")
names_4 = list(letters_dictionary_4.keys())
values_4 = list(letters_dictionary_4.values())
plt.subplot(3, 2, 4)
plt.title("Fourth Letter Statistics")
plt.bar(range(len(letters_dictionary_4)), values_4, tick_label=names_4, color= colors_4)

print("Fifth Letter Statistics: ", letters_dictionary_5)
max_key_5 = max(letters_dictionary_5, key=letters_dictionary_5.get)
for value in letters_dictionary_5.keys():
    if max_key_5 == value:
        colors_5.append("g")
    else:
        colors_5.append("b")
names_5 = list(letters_dictionary_5.keys())
values_5 = list(letters_dictionary_5.values())
plt.subplot(3, 2, 5)
plt.title("Fifth Letter Statistics")
plt.bar(range(len(letters_dictionary_5)), values_5, tick_label=names_5, color= colors_5)

print("Highest First Letter Using: ", max_key_1)
print("Highest Second Letter Using: ", max_key_2)
print("Highest Third Letter Using: ", max_key_3)
print("Highest Fourth Letter Using: ", max_key_4)
print("Highest Fifth Letter Using: ", max_key_5)

plt.show()