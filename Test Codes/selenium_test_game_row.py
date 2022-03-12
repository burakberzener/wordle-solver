from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

inner_texts_for_game_row = []

url = "https://www.nytimes.com/games/wordle/index.html"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

#print(driver.title)
#print(driver.page_source)
html_body = driver.find_element(by = By.XPATH, value="/html/body")
html_body.click()
html_body.send_keys("crane")
html_body.send_keys(Keys.ENTER)
sleep(5)
html_body.send_keys("start")
html_body.send_keys(Keys.ENTER)
inner_texts_for_game_row_0 =  [my_elem.get_attribute("outerHTML") for my_elem in driver.execute_script(
    """return document
    .querySelector('game-app')
    .shadowRoot
    .querySelectorAll('game-row')[0]
    .shadowRoot
    .querySelectorAll('game-tile[letter]')
    """)]

for inner_text in inner_texts_for_game_row_0:
    print(inner_text)

sleep(5)
