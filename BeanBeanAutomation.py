from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pyautogui
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://beanbeanbean.com/html/category/math/addition.html")

difficultyButton = driver.find_element(By.ID, 'imgDifficulty2')
difficultyButton.click()
difficultyButton.click()

numField1 = driver.find_element(By.ID, 'pFirstNumber')
numField2 = driver.find_element(By.ID, 'pSecondNumber')
ansField = driver.find_element(By.ID, 'pAnswerNumber')
submitButton = driver.find_elements(By.CLASS_NAME, 'pKey')[0]
continueButton = driver.find_element(By.ID, 'buttonContinue')

while True:
    try:
        num1 = int(numField1.text)
        num2 = int(numField2.text)
        pyautogui.write('{0}'.format(num1 + num2), interval=0.25)
        pyautogui.press('enter')
        print('{0}'.format(num1 + num2))
    except:
        continueButton.click()
    finally:
        time.sleep(1)
        
