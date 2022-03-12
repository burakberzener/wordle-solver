from time import sleep
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import wordlesolver
import wordleDatabases

url_eng = "https://www.nytimes.com/games/wordle/index.html"
url_tr = "https://www.bundle.app/wordle-tr/"
first_word_eng = "cares"
first_word_tr = "sakin"

guessing_word = ["","","","",""]
letters_correct = []
letters_present = []
letters_absent = []
letters_dictionary = dict.fromkeys(string.ascii_lowercase, 0)

EVALUATION = "evaluation"
LETTER = "letter"

def chooseLanguage(lang):
    if lang == "TR":
        url = url_tr
        word_database = wordleDatabases.DATABASE_TR_JSON_1
        first_word = first_word_tr
    elif lang == "ENG":
        url = url_eng
        word_database = wordleDatabases.DATABASE_ENG_TXT_2
        first_word = first_word_eng
    return url, word_database, first_word

def main():
    row = 0

    url, word_database, first_word = chooseLanguage("TR")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    #print(driver.title)
    #print(driver.page_source)
    html_body = driver.find_element(by = By.XPATH, value="/html/body")
    
    filename = word_database

    if filename.endswith(".txt"):
        df = pd.read_csv(filename, names= ['word'])
    elif filename.endswith(".json"):   
        df = pd.read_json(filename)
        df.columns = ["word"]
        df["word"] = df["word"].str.lower()
    print(df.head())
    print(df.size)

    wordleSolver = wordlesolver.wordleSolverClass(url, html_body)
    guessed_word = first_word
    while(1):
        wordleSolver.tryWord(guessed_word)
        text_in_row = wordleSolver.getRowsAttribute(driver, row, EVALUATION)
        
        for letter, text, index in zip(guessed_word, text_in_row, range(5)):
            print("letter: ", letter, "text: ", text, "index: ", index)
            if text == "correct":
                letters_correct.append(letter)
                df = df[df["word"].str[index] == letter]
                #df = df[df["word"].str.contains(letter)]
                #df = df[df["word"].str.index(letter, index, 1)]
            elif text == "present":
                letters_present.append(letter)
                df = df[df["word"].str[index] != letter]
                df = df[df["word"].str.contains(letter)]
            elif text == "absent":
                if letters_dictionary[letter] == "present" or letters_dictionary[letter] == "correct" or guessed_word.count(letter)>1:
                    letters_absent.append(letter)
                    df = df[df["word"].str[index] != letter]
                else:
                    letters_absent.append(letter)
                    df = df[~df["word"].str.contains(letter)]
            letters_dictionary[letter] = text

        print(letters_dictionary)
        print("Corrects: ", letters_correct)
        print("Presents: ", letters_present)
        print("Absents: ", letters_absent)
        letters_absent.clear()
        letters_present.clear()
        letters_correct.clear()
        #wordleSolver.checkStatus(text_in_row)
        print(df.head(10))
        print(df.size)
        sleep(2)
        guessed_word = df["word"].iloc[0]
        print("guessed word: ", guessed_word)
        sleep(2)
        row = row + 1     

if __name__ == "__main__":
    main()