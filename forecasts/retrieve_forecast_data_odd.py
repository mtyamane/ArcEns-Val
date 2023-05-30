"""
Retrieve forecast data for odd days. Requests are made for each day in the input month and the
API call is formed in REQUESTS.py

NOTE: Requests are currently fixed for 2019!

Author: Mark Yamane, 05/29/2023
"""

from ecmwfapi import ECMWFDataServer
from REQUESTS import *
import time

if __name__ == '__main__':
    monthnum = input("What month? (number): ")
    month_int = int(monthnum)

    server = ECMWFDataServer()
    count = 0
    if month_int < 10:
        month = '0'+monthnum
    else:
        month = monthnum
    
    if month_int != 2:
        # for months that aren't February
        for day in range(1,31):
            if day%2 == 1:
                # odd day
                day = str(day)
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
    else:
        for day in range(1,29):
            if day%2 == 1:
                # odd day
                day = str(day)
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
                
    extradate = '2019-'+ month +'-31'
    if month_int < 8 and month_int%2 == 1:
        # odd months before august need an extra request
        start = time.time()

        # perform the API call
        reqWithTimes(server, extradate)
        count += 1

        # update the terminal
        end = time.time()
        print(f'{date} processed in {end - start} s.')
    elif month_int > 7 and month_int%2 == 0:
        # even months after august need an extra request
        start = time.time()
        
        # perform the API call
        reqWithTimes(server, extradate)
        count += 1

        # update the terminal
        end = time.time()
        print(f'{date} processed in {end - start} s.')
    
    print(f'{count} files processed. Forecast data can be found at ./forecasts/full/')