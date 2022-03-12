from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

inner_texts_for_game_row = []

EVALUATION = "evaluation"
LETTER = "letter"

def tryWord(html_body, word):
     html_body.click()
     html_body.send_keys(word)
     html_body.send_keys(Keys.ENTER)

def checkStatus(text_in_row):
    for inner_text in text_in_row:
        print(inner_text)

def getRowsAttribute(driver, row, attribute):
    return [my_elem.get_attribute(attribute) for my_elem in driver.execute_script(
        """return document
        .querySelector('game-app')
        .shadowRoot
        .querySelectorAll('game-row')[{}]
        .shadowRoot
        .querySelectorAll('game-tile')
        """.format(row))]

def main():
    url = "https://www.nytimes.com/games/wordle/index.html"
    row = 0

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    #print(driver.title)
    #print(driver.page_source)
    html_body = driver.find_element(by = By.XPATH, value="/html/body")

    tryWord(html_body, "crane")
    text_in_row = getRowsAttribute(driver, row, EVALUATION)
    checkStatus(text_in_row)
    row += row
    sleep(5)

    tryWord(html_body, "freak")
    text_in_row = getRowsAttribute(driver, row, EVALUATION)
    checkStatus(text_in_row)
    row += row
    sleep(5)

if __name__ == "__main__":
    main()