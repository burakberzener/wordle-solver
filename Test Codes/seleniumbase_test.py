from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

url = "https://www.nytimes.com/games/wordle/index.html"

BaseCase.open(url)