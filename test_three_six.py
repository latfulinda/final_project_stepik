from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait
import math

def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])    
def test_lessons_three (browser, link):
    browser.implicitly_wait(60)
    browser.get(link)
    answer = math.log(int(time.time()))
    print(answer)
    input = browser.find_element_by_class_name("ember-text-area").send_keys(str(answer))
    #browser.implicitly_wait(10)
    button = browser.find_element_by_class_name('submit-submission')
    button.click()
    time.sleep(50)