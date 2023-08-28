"""

[Filename]   : userInformation.py
[Author]     : Abhijit Dasgupta
[Date]       : 25-8-2023
[Description]: This script contains the configuration related Function sucg as
                login, get access token etc
"""

class userInformation:
  def __init__(self):
    print(self)

  # Print User Information
  def printUserInfo(self,kite):
    # Example: Fetch the user's profile details
    user_profile = kite.profile()
    print("User Profile:")
    print(user_profile)