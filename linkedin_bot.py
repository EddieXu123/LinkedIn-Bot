# Intro: I was scrolling through my LinkedIn feed and saw tons of posts of people whose internships
# got canceled due to COVID-19, but fortunately landed another remote internship. I knew that the recruiters
# helping these people were working extremely hard behind the scenes and wanted to acknowledge them in some way
# As a result, I built a LinkedIn bot that would log on, search a company's recruiters, and send them a
# note expressing gratitude for their hard work during these times. It was a short letter and only a few
# recruiters were actually accepting connection requests/messages, but many of the ones who did replied with
# thanks, making the whole experience worth it!


# Plan
# Log into my LinkedIn
# Go to search bar, at the start of the day, put in 3 companies.
# The bot will search company #1-3 + recruiters, connect with any recruiter by sending a message
# If it is possible to message them, then write them the same message. close, and continue
#
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password


# Button to go to next page
# '/html/body/div[8]/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]'
class LinkedInBot:
    def __init__(self):
        # Create a browser we can play on
        self.driver = webdriver.Chrome()

    def message_recruiter(self):
        """First, we must log into our LinkedIn account"""
        # Go to LinkedIn
        self.driver.get(
            'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        sleep(3)
        # Enter email
        self.driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input').send_keys(email)
        sleep(2)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys(password + Keys.RETURN)
        sleep(5)

        # Go to search bar and enter your company name
        search = self.driver.find_element_by_xpath('/html/body/header/div/form/div/div/div/div/div[1]/div[1]/input')
        search.click()
        search.send_keys("Microsoft Recruiter" + Keys.RETURN)  # change this with whichever company you want


    def click_connect(self):
        self.driver.find_element_by_xpath('/html/body/div[9]/div[4]/div/div[2]/div/div[2]/div/div/div/div/ul/li[13]/div/div/div[3]/div/button').click()
"""/html/body/div[9]/div[4]/div/div[2]/div/div[2]/div/div/div/div/ul/li[13]/div/div/div[3]/div/button'
'/html/body/div[9]/div[4]/div/div[2]/div/div[2]/div/div/div/div/ul/li[6]/div/div/div[3]/div/button'"""


bot = LinkedInBot()
#bot.message_recruiter()

#finite state machine check if I finished everyone first

# inner HTML have button
# if inner HTML has a button, click that button
# member = recruiter[i].get_attribute('innerHTML')
# if 'button' in member:
#     click.button
# matches[i].get_attribute('innerHTML')
#self.driver.find_elements_by_class_name('search-entity') Gives all people on screen
#search-results__list
