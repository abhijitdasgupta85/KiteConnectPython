"""
[Filename]   : main.py
[Author]     : Abhijit Dasgupta
[Date]       : 25-8-2023
[Description]: This script contains the main program
"""
# Import necessary libraries/modules if needed
from ConfigureKiteConnect import *
from userInformation import *
from tradingFunctions import *

# Replace with your API key and secret
api_key = "0c8reefngx00853h"
api_secret = "hogpzlapsof992dxa5xjyihp3zv2jrve"
userID='XXXXXXX'
pwd = 'XXXXXXXX'
access_token = ""

#main program starts here
if __name__ == "__main__":
  print(f"Welcome to my first algorithm ")
  print(f"***********************************************")
  
  #Get Login Url
  configobj = ConfigureKiteConnect(api_key,api_secret,userID,pwd)
  configobj.automaticLogin()
  token = configobj.setAccessToken()
  print("Access Token: " + token )

  #create a text file in python and store the access token
  #file = open("config.txt", "w")
  #file.write("token:"+token)
  #file.close()
  
  #Print User Info
  objUserInfo = userInformation()
  objUserInfo.printUserInfo(configobj.kite)

  #Get LTP
  trdFunctions = tradingFunctions()
  print(" TCS LTP IS: " + str(trdFunctions.get_ltp(configobj.kite)))

  #Export minutes historical data
  sdate = '2023-08-23'
  edate = '2023-08-23'
  #exportMinuteHistoricalDataByDate

