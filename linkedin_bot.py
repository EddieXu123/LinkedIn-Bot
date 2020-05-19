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
from contact import email, password, company, search_entry


class LinkedInBot:
    def __init__(self):
        # Create a browser we can play on
        self.driver = webdriver.Chrome()

    def log_on(self):
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

    def daily_post(self):
        start_post = self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div[1]/div/div[1]/button[1]')
        # Click on Start a Past
        start_post.click()
        # Select text to enter post
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/p').send_keys(message)
        # Post the message
        self.driver.find_element_by_xpath('//*[@id="ember462"]').click()

    def like_other_posts(self):
        # post is the array that stores every single 'like button' in your feed
        # which you can then click as you go on
        post = bot.driver.find_elements_by_class_name('react-button__text')
        # If the post has been liked already, it will have in the outerHTML:"like"
        has_been_liked = "like"
        i = 0 # Starting with the first post in your feed
        while i < 10:  # replace 10 with how ever many posts you want to like in your feed
            # If the post you are on has NOT been liked already,
            if not has_been_liked in post[i].get_attribute('outerHTML'):
                # like the post
                post[i].click()
                sleep(1)
                # Posts that are further down in your feed are hidden from the driver.
                # To access them, every time you like a post (which causes the driver to scroll
                # down more into your feed), reset the 'post' array with all the possible elements
                post = bot.driver.find_elements_by_class_name('react-button__text')
                i += 1
                sleep(1)
            else:
                # Otherwise, keep scrolling down as if we had liked it to get more elements
                i += 1
                sleep(1)

    def connect_and_message(self):
        # Go to search bar and enter your company name
        search = self.driver.find_element_by_xpath('/html/body/header/div/form/div/div/div/div/div[1]/div[1]/input')
        search.click()
        search.send_keys(search_entry + Keys.RETURN)

    def click_connect(self):
        # Sometimes, you will get company results for what you have searched,
        # in the form of 'cards' you can 'follow'. These have the same name as the
        # 'connect' button. However, they also have an additional "mb2" to distinguish them
        # from an actual person. So, to ignore these, just choose the buttons without "mb2"

        # variable to store all the 'connects' (and cards) on a page
        connect = self.driver.find_elements_by_class_name('search-result__action-button')
        message = self.driver.find_elements_by_class_name('message-anywhere-button')

        page_count = 0
        while page_count < 5:  # Connect/Message recruiters on as many pages as you want
            for i in range(0, len(connect)):  # For every connect/follow button on the page
                if not "mb2" in connect[i]:  # If the button I am on is not a 'card'
                    connect[i].click()  # connect with the person
            # Now, I have connected with everyone on the page
            # Time to send messages to those who allow me to do so!
            for j in range(0, len(message)):
                message[j].click()
                compose_message = bot.driver.find_element_by_class_name('ember-text-field')
                subject = "Thank you!"  # Change to whatever you want!
                message_body = "Hi! I was scrolling through LinkedIn and just wanted to tell you" \
                               "that you are amazing! Keep up the good work - your efforts " \
                               " to thank you for all the amazing work you've been" \
                               "doing lately! It definitely ! Have an amazing day! :)" \
                compose_message.send_keys(subject + Key.tab + message_body)





        # Go to next page
        driver.find_element_by_xpath('//*[@id="ember7512"]/span').click()


"""
# Calling the functions to run the program
bot = YouTubeBot()
bot.log_on_and_like()
"""


#bot = LinkedInBot()
#bot.message_recruiter()

#finite state machine check if I finished everyone first


# inner HTML have button
# if inner HTML has a button, click that button
# member = recruiter[i].get_attribute('innerHTML')
# if 'button' in member:
#     click.button
# matches[i].get_attribute('innerHTML')
# Scroll down 2 times, so hit space bar 2 times on keyboard to get 10 entities
#self.driver.find_elements_by_class_name('search-entity') Gives all people on screen
#search-results__list
# Also need to take care of when you send too many connections and need to enter email


'/html/body/div[7]/div[3]/div/div/div/div/div[3]/div[2]/div/div/div[5]/div/div[2]/span[1]/button[1]/span/span'


# Button to go to next page
'/html/body/div[8]/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]'


post = bot.driver.find_elements_by_class_name('react-button__text')

'//*[@id="ember7512"]/span'
'//*[@id="ember7512"]/span'


# If they have mb2, then they are a card, not a person
# Connect
search-result__action-button
# Message
message-anywhere-button



 visually-hidden
'//*[@id="a11y-ember790"]'


text = bot.driver.find_element_by_class_name('ember-text-field')
msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 notranslate
contenteditable
