import json
from time import sleep
import string
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import wordlesolver
import wordleLangSelector
import wordleParams
import popularWordFinder

#TODO
#add file path for linux system - os.path...
#update dataset to original ones

#FIXME
#turkish letters not work with the script

letters_guessing_word = ["","","","",""]
letters_correct = []
letters_present = []
letters_absent = []
letters_dictionary = dict.fromkeys(string.ascii_lowercase, 0)
tried_words = []

EVALUATION = "evaluation"
LETTER = "letter"
LANG = "ENG"

wordleparams = wordleParams.wordleParamsClass()
df = pd.DataFrame()
filename = wordleparams.word_database

def browserOptions():
    chrome_options = Options()

    if platform.system() == "Windows":
        pass
    elif platform.system() == "Linux":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
    
    return chrome_options

def browserService():
    if platform.system() == "Windows":
        return Service(ChromeDriverManager().install())
    elif platform.system() == "Linux":
        return Service("/usr/lib/chromium-browser/chromedriver")

def init():   
    wordleparams.row = 0
    wordleparams.url, wordleparams.word_database, wordleparams.first_word = wordleLangSelector.chooseLanguage(LANG)

def main():
    driver = webdriver.Chrome(service=browserService(), chrome_options=browserOptions())
    driver.set_window_position(880, 0, windowHandle ='current')
    driver.get(wordleparams.url)
    wordleparams.html_body = driver.find_element(by = By.XPATH, value="/html/body")
    
    filename = wordleparams.word_database
    if filename.endswith(".txt"):
        df = pd.read_csv(filename, names= ['word'])
    elif filename.endswith(".json"):   
        df = pd.read_json(filename)
        df.columns = ["word"]
        df["word"] = df["word"].str.lower()
    print(df.head())
    print(df.size)
    
    wordleSolver = wordlesolver.wordleSolverClass(wordleparams.url, wordleparams.html_body)
    guessed_word = popularWordFinder.findWordsRanks(df)

    while(len(letters_correct)<5):

        popularWordFinder.showLetterStatistics(df, guessed_word)
        sleep(1)

        wordleSolver.tryWord(guessed_word)
        text_in_row = wordleSolver.getRowsAttribute(driver, wordleparams.row, EVALUATION)

        wordleparams.game_state = wordleSolver.getGameState(driver, LANG)
        print(wordleparams.game_state)
        if wordleparams.game_state == 'IN_PROGRESS':
            tried_words.append(guessed_word)
            pass
        elif wordleparams.game_state == 'WIN':
            wordleparams.is_solved = True
            break
        elif wordleparams.game_state == 'FAIL':
            wordleparams.is_solved = False
            break

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
        sleep(1)

        #guessed_word = df["word"].iloc[0]
        df = df.reset_index(drop=True)
        filepath = "./out.csv"
        df["word"].to_csv(filepath)
        guessed_word = popularWordFinder.findWordsRanks(df)
        print("guessed word: ", guessed_word, end="\n")
        sleep(1)

        wordleparams.row += 1
        
    if wordleparams.is_solved == True:
        print("Congratulations! You find the Word: ", guessed_word)
        game_stats = wordleSolver.getGameStats(driver, LANG)
        f = open("result.json", "w")
        f.truncate(0)
        game_stats["guessedWord"] = guessed_word
        game_stats["triedWords"] = tried_words
        result = json.dumps(game_stats)
        f.write(result)
    else:
        print("Word is not found!")

init()
if __name__ == "__main__":
    main()