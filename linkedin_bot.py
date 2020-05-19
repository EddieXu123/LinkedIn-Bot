from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
        sleep(2)
        # Enter email
        self.driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input').send_keys(email)
        sleep(1)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys(password + Keys.RETURN)
        sleep(4)

    def daily_post(self):
        start_post = self.driver.find_element_by_class_name('share-box-feed-entry__trigger')
        # Click on Start a Past
        start_post.click()
        sleep(1)
        # Whatever you want to post on your profile
        message = "Hi everyone! I'm new to this site but it reminds me of MySpace, let's connect!"
        # Select text to enter post
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/p').send_keys(message)
        # Post the message
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button').click()
        sleep(3)

    def like_other_posts(self):
        # post is the array that stores every single 'like button' in your feed
        # which you can then click as you go on
        post = self.driver.find_elements_by_class_name('react-button__text')
        # If the post has been liked already, it will have in the outerHTML:"like"
        has_been_liked = "like"
        i = 0  # Starting with the first post in your feed
        while i < 10:  # replace 10 with how ever many posts you want to like in your feed
            # If the post you are on has NOT been liked already,
            if not has_been_liked in post[i].get_attribute('outerHTML'):
                # like the post
                post[i].click()
                # Posts that are further down in your feed are hidden from the driver.
                # To access them, every time you like a post (which causes the driver to scroll
                # down more into your feed), reset the 'post' array with all the possible elements
                post = self.driver.find_elements_by_class_name('react-button__text')
                i += 1
            else:
                # Otherwise, keep scrolling down as if we had liked it to get more elements
                i += 1
                sleep(1)
        sleep(4)

    def search_company(self):
        # Go to search bar and enter your company name
        search = self.driver.find_element_by_xpath('/html/body/header/div/form/div/div/div/div/div[1]/div[1]/input')
        search.click()
        search.send_keys(search_entry + Keys.RETURN)
        sleep(4)

    def click_connect(self):
        # Sometimes, you will get company results for what you have searched in the form of 'cards' you can 'follow'.
        # These cards have the same class_name as the 'connect' button. However, they also have an additional
        # "Follow/Unfollow" attribute in their outerHTML to distinguish them from an actual person.
        # So, to ignore these, just choose the buttons without "ollow"

        page_count = 0
        while page_count < 5:  # Connect/Message recruiters on as many pages as you want
            # variable to store all the 'connect' buttons (and cards) on a page
            connect = self.driver.find_elements_by_class_name('search-result__action-button')

            for i in range(0, len(connect)):  # For every connect/follow button on the page
                connect = self.driver.find_elements_by_class_name('search-result__action-button')  # Need to reset connect counter
                if not "ollow" in connect[i].get_attribute('outerHTML'):  # If the button I am on is not a 'card'
                    connect[i].click()  # connect with the person
                    sleep(2)

                    # We could be at a place where we've already connected with this person, so see if
                    # we get the same popup after clicking 'connect'
                    try:
                        self.driver.find_element_by_class_name('flex-1').get_attribute('innerHTML')
                    except NoSuchElementException:
                        continue
                    # When you connect with someone, a popup appears, saying your invitation is on the way
                    # The class_name for this text is flex-1 and the innerHTML is 'your invite to ____ is on the way...'
                    # invite_message holds the innerHTML of little paragraph that pops up when you send a connection
                    invite_message = self.driver.find_element_by_class_name('flex-1').get_attribute('innerHTML')
                    name_of_connection = ""  # Set an empty name variable we will append the connections name into
                    # Their name starts at the 44th index position of the innerHTML and ends when there is a space (to denote first name)
                    # or when there is a '<' (if you want their full name: '<' denotes the end of the 'bold' HTML tag their name is in)
                    for character in range(44, len(invite_message)):
                        if not ' ' in invite_message[character]:
                            name_of_connection += invite_message[character]
                        else:  # once we reach the space (or closing HTML tag), we have the person's first/full name so we can break
                            break
                    # Now, name_of_connection gives you the name of the person you sent a connection to

                    # Now, we can add a nice note :)

                    # mr1 is one of 3 buttons that we can click when we get the 'your invite is on the way' popup
                    add_note = self.driver.find_elements_by_class_name('mr1')
                    add_note[1].click()  # The second webElement is the one that clicks 'Add a note'

                    # Write your note here (Note I have already set up a template with "Hi 'name of person'!")
                    connect_message = "I was scrolling through LinkedIn and just wanted to tell you that you are amazing! " \
                                      "I know your job is tough but what you do genuinely helps so many people and I just wanted to recognize that! " \
                                      "Keep up the great work and have an amazing day!"
                    connect_invite = "Hi " + name_of_connection + "! " + connect_message
                    self.driver.find_element_by_xpath('//*[@id="custom-message"]').send_keys(connect_invite)  # Send your message
                    done_with_message = self.driver.find_elements_by_class_name('artdeco-button__text')  # Get all the buttons you can press
                    done_with_message[5].click()  # The 'Done' or send button is the 6th one

                    # Now, I have sent the message to my connection and can keep going
                    sleep(3)

            # variable to store all the 'message' buttons on a page
            message = self.driver.find_elements_by_class_name('message-anywhere-button')
            # Now, I have connected with everyone on the page
            # Time to send messages to those who allow me to do so!
            for j in range(0, len(message)):
                message[j].click()
                compose_message = self.driver.find_element_by_class_name('ember-text-field')
                subject = "Thank you!"  # Change to whatever you want!
                message_body = "Hi! I was scrolling through LinkedIn and just wanted to tell you" \
                               "that you are amazing! I know your job is tough but what you do genuinely helps so many people" \
                               "and I just wanted to recognize that! Keep up the great work and have an amazing day!"
                compose_message.send_keys(subject + Key.tab + message_body)
                # Send the message
                self.driver.find_elements_by_class_name('msg-form__send-button').click()
        # Go to next page
        driver.find_element_by_xpath('//*[@id="ember7512"]/span').click()
        page_count += 1


# Calling the functions to run the program
bot = LinkedInBot()
bot.log_on()
bot.daily_post()
bot.like_other_posts()
bot.search_company()
bot.click_connect()
