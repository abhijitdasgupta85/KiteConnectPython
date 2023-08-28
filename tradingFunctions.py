"""

[Filename]   : tradingFunctions.py
[Author]     : Abhijit Dasgupta
[Date]       : 25-8-2023
[Description]: This script contains the configuration related Function sucg as
                login, get access token etc
"""
# Import necessary libraries/modules if needed
from datetime import date
import pandas as pd

class tradingFunctions:
  #get last Traded Price
  def get_ltp(self,kite):
    # Fetch instruments' details
    ltp = kite.ltp('NSE:TCS')
    ltp = ltp['NSE:TCS']['last_price']
    return ltp
  
  #funtion to hi
  def exportMinuteHistoricalDataByDate(self,kite, from_date, to_date, symbol, token):
    if from_date > to_date:
      return

    #token = db.get_instrument_token(symbol)
    #if token == -1:
    #  print('Invalid symbol provided')
    #  return 'None'

    # provide interval as per candle size given above
    interval = 'minute'
    records = kite.historical_data(token, from_date=from_date, to_date=to_date, interval=interval)
    df = pd.DataFrame(records)
    
    if len(df) == 0:
      print('No data returned')
      return
    
    df.drop('volume', inplace=True, axis=1)
    df.set_index('date',inplace=True)
    return df
 