"""
[Filename]   : ConfigureKiteConnect.py
[Author]     : Abhijit Dasgupta
[Date]       : 25-8-2023
[Description]: This script contains the configuration related Function sucg as
                login, get access token etc
"""
# Import necessary libraries/modules if needed
from kiteconnect import KiteConnect
from selenium import webdriver
import webbrowser
import requests
import time
import os
from pyotp import TOTP
from selenium.webdriver.support.wait import WebDriverWait

class ConfigureKiteConnect:
  def __init__(self, api_key, api_secret,usrId,pwd):
    self.api_key = api_key
    self.api_secret = api_secret
    self.kite = KiteConnect(api_key=api_key)
    self.userid = usrId
    self.pwd = pwd

  def automaticLogin(self):
    #setup the chrome browser
    driver = webdriver.Chrome()

    # Open the login URL in a browser
    driver.get(self.kite.login_url())
    driver.implicitly_wait(5)
 
    # provide user name and password
    username = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
    password = driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')

    username.send_keys(self.userid)
    password.send_keys(self.pwd)

    #click the login button
    driver.find_element('xpath','/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    time.sleep(2)

    pin = driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/input')
    #totp = TOTP(totp_key)
    #token = totp.now()
    #pin.send_keys(token)

    #Required just once to get url. Save the URL in your Bookmarks before you hit Enter key
    r = requests.get(self.login_url)
    print(r.url)

  # Set the access token for future API calls
  def setAccessToken(self):
    # After successful login and obtaining the request token
    request_token = input("Enter the request token: ")
    #data=session object
    data = self.kite.generate_session(request_token, api_secret=self.api_secret)
    # Exchange request token for an access token
    access_token = data["access_token"]
    self.kite.set_access_token(access_token)
    return access_token
 


