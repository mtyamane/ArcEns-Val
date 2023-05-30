"""
Retrieve forecast data for one day. The API call is formed in REQUESTS.py

NOTE: Requests are currently fixed for 2019!

Author: Mark Yamane, 05/29/2023
"""

from ecmwfapi import ECMWFDataServer
from REQUESTS import *
import time

MONTH = '6'
DAY = '1'

if __name__ == '__main__':
    server = ECMWFDataServer()

    # process month
    monthnum = MONTH
    month_int = int(monthnum)

    count = 0
    if month_int < 10:
        month = '0'+monthnum
    else:
        month = monthnum
    
    # process day
    day = DAY
    if int(day) < 10:
        day = '0'+day
    
    # date string
    date = '2019-' + month + '-' + day

    # perform API call
    start = time.time()
    reqWithTimes(server, date)
    count += 1

    # update the terminal
    end = time.time()
    print(f'{date} processed in {end - start} s.')
    
    print(f'{count} files processed. Forecast data can be found at ./forecasts/full/')