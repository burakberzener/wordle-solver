from selenium.webdriver.common.keys import Keys

class wordleSolverClass:
    def __init__(self, url, html_body):
        self.url = url
        self.html_body = html_body
    
    def tryWord(self, word):
        self.html_body.click()
        self.html_body.send_keys(word)
        self.html_body.send_keys(Keys.ENTER)

    def checkStatus(self, text_in_row):
        for inner_text in text_in_row:
            print(inner_text)

    def getRowsAttribute(self, driver, row, attribute):
        return [my_elem.get_attribute(attribute) for my_elem in driver.execute_script(
            """return document
            .querySelector('game-app')
            .shadowRoot
            .querySelectorAll('game-row')[{}]
            .shadowRoot
            .querySelectorAll('game-tile')
            """.format(row))]

    def getGameState(self, driver, LANG):
        if LANG == "ENG":
            return driver.execute_script('return JSON.parse(localStorage.getItem("nyt-wordle-state")).gameStatus')
        elif LANG == "TR":
            return driver.execute_script('return JSON.parse(localStorage.gameState).gameStatus')

    def getGameStats(self, driver, LANG):
        if LANG == "ENG":
            return driver.execute_script('return JSON.parse(localStorage.getItem("nyt-wordle-statistics"))')
        elif LANG == "TR":
            return driver.execute_script('return JSON.parse(localStorage.statistics)')