import string
from time import sleep
from turtle import color

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import wordleLangSelector

plt.ion()
fig = plt.figure(figsize=(11, 12), dpi=80)
plt.get_current_fig_manager().window.wm_geometry("+0+0")

filename = wordleLangSelector.Database.DATABASE_ENG_TXT_2

if filename.endswith(".txt"):
    df1 = pd.read_csv(filename, names= ['word'])
elif filename.endswith(".json"):   
    df1 = pd.read_json(filename)
    df1.columns = ["word"]
    df1["word"] = df1["word"].str.lower()
    print(df1.head())

letters_dictionary_1 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_2 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_3 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_4 = dict.fromkeys(string.ascii_lowercase, 0)
letters_dictionary_5 = dict.fromkeys(string.ascii_lowercase, 0)

def setGraphColors(letters_dictionary: dict, max_key: int, colors: list):
    for value in letters_dictionary.keys():
        if max_key == value:
            colors.append("g")
        else:
            colors.append("b")
    return colors


def findHiglyUsedLetter(letters_dictionary: dict):
    max_key = max(letters_dictionary, key=letters_dictionary.get)
    return max_key

def findWordsRanks(df: pd.DataFrame):
    df["rank"] = 0

    #print(df.last)
    #print(len(df.index))
    for word,cnt in zip(df["word"], range(len(df.index))):
        #print(word)
        df.at[cnt, "rank"]= letters_dictionary_1[word[0]]+letters_dictionary_2[word[1]]+letters_dictionary_3[word[2]]+letters_dictionary_4[word[3]]+letters_dictionary_5[word[4]]
    
    print(df.head())
    #print(len(df.index))
    print(df.loc[df["rank"].idxmax()])

    highset_rank_word = df.loc[df["rank"].astype(float).idxmax(), "word"]
    #del df["rank"]

    return highset_rank_word

def showLetterStatistics(df: pd.DataFrame, popular_word: string):

    plt.get_current_fig_manager().window.wm_geometry("+0+0")
    plt.clf()
    plt.get_current_fig_manager().window.wm_geometry("+0+0")

    colors_1 = []
    colors_2 = []
    colors_3 = []
    colors_4 = []
    colors_5 = []

    for word in df["word"]:
        #print(word)
        letters_dictionary_1[word[0]] += 1
        letters_dictionary_2[word[1]] += 1
        letters_dictionary_3[word[2]] += 1
        letters_dictionary_4[word[3]] += 1
        letters_dictionary_5[word[4]] += 1

    print("First Letter Statistics: ", letters_dictionary_1)
    max_key_1 = findHiglyUsedLetter(letters_dictionary_1)
    colors_1 = setGraphColors(letters_dictionary_1, max_key_1, colors_1)
    names_1 = list(letters_dictionary_1.keys())
    values_1 = list(letters_dictionary_1.values())
    #plt.subplot(3, 2, 1)
    ax = fig.add_subplot(321)
    #ax.title("First Letter Statistics")
    ax.bar(range(len(letters_dictionary_1)), values_1, tick_label=names_1, color= colors_1)

    print("Second Letter Statistics: ", letters_dictionary_2)
    max_key_2 = findHiglyUsedLetter(letters_dictionary_2)
    colors_2 = setGraphColors(letters_dictionary_2, max_key_2, colors_2)
    names_2 = list(letters_dictionary_2.keys())
    values_2 = list(letters_dictionary_2.values())
    #plt.subplot(3, 2, 2)
    ax = fig.add_subplot(322)
    #ax.title("Second Letter Statistics")
    ax.bar(range(len(letters_dictionary_2)), values_2, tick_label=names_2, color= colors_2)

    print("Third Letter Statistics: ", letters_dictionary_3)
    max_key_3 = findHiglyUsedLetter(letters_dictionary_3)
    colors_3 = setGraphColors(letters_dictionary_3, max_key_3, colors_3)
    names_3 = list(letters_dictionary_3.keys())
    values_3 = list(letters_dictionary_3.values())
    #plt.subplot(3, 2, 3)
    ax = fig.add_subplot(323)
    #ax.title("Third Letter Statistics")
    ax.bar(range(len(letters_dictionary_3)), values_3, tick_label=names_3, color= colors_3)

    print("Fourth Letter Statistics: ", letters_dictionary_4)
    max_key_4 = findHiglyUsedLetter(letters_dictionary_4)
    colors_4 = setGraphColors(letters_dictionary_4, max_key_4, colors_4)
    names_4 = list(letters_dictionary_4.keys())
    values_4 = list(letters_dictionary_4.values())
    #plt.subplot(3, 2, 4)
    ax = fig.add_subplot(324)
    #ax.title("Fourth Letter Statistics")
    ax.bar(range(len(letters_dictionary_4)), values_4, tick_label=names_4, color= colors_4)

    print("Fifth Letter Statistics: ", letters_dictionary_5)
    max_key_5 = findHiglyUsedLetter(letters_dictionary_5)
    colors_5 = setGraphColors(letters_dictionary_5, max_key_5, colors_5)
    names_5 = list(letters_dictionary_5.keys())
    values_5 = list(letters_dictionary_5.values())
    #plt.subplot(3, 2, 5)
    ax = fig.add_subplot(325)
    #ax.title("Fifth Letter Statistics")
    ax.bar(range(len(letters_dictionary_5)), values_5, tick_label=names_5, color= colors_5)

    ax = fig.add_subplot(326)
    plt.text(0.25, 0.4, popular_word, transform=ax.transAxes, fontsize=60)

    print("Highest First Letter Using: ", max_key_1)
    print("Highest Second Letter Using: ", max_key_2)
    print("Highest Third Letter Using: ", max_key_3)
    print("Highest Fourth Letter Using: ", max_key_4)
    print("Highest Fifth Letter Using: ", max_key_5)
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    
showLetterStatistics(df1, " ")

guessed_word = findWordsRanks(df1)

print(guessed_word)
sleep(10)