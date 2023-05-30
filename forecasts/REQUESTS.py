"""
Helper functions for TIGGE Data Retrieval

Set the request based on the GUI at: https://apps.ecmwf.int/datasets/data/tigge/levtype=sfc/type=pf/
Request efficiency is based on: https://confluence.ecmwf.int/display/WEBAPI/TIGGE+retrieval+efficiency

Author: Mark Yamane, 05/29/2023
"""

from ecmwfapi import ECMWFDataServer

OUTDIR = './full/'

def tigge_request(server, date, time, target):
    """
    Perform the API request to retrieve data. Info for all request options can be found at:
    https://confluence.ecmwf.int/display/WEBAPI/Brief+request+syntax

    in-depth descriptions can be found at:
    https://confluence.ecmwf.int/display/UDOC/Keywords+in+MARS+and+Dissemination+requests

    Parameters
    ----------
    server : ECMWFDataServer
        server to make the API request
    date : str
        year-month-day string
    time : str
        starting time of the forecast (00 -> 12 AM; 12 -> noon)
    target : str
        output filename
    """
    server.retrieve({
        "class": "ti",                               # MARS classification (ti = tigge)
        "dataset": "tigge",                          # ECMWF dataset
        "date": date,                                # date of forecast start
        "expver": "prod",                            # model version (prod = production)
        "grid": "0.5/0.5",                           # target grid (Gaussian or lat/lng)
        "area": "80/180/50/215",                     # target sub-area (requires grid; N/W/S/E) https://confluence.ecmwf.int/pages/viewpage.action?pageId=151520973
        "levtype": "sfc",                            # type of level (sfc = surface)
        "number": "1/to/50",                         # ensemble members to retrieve (can be any of 1-50)
        "origin": "ecmf",                            # WMO identifier (ecmf = ECMWF)
        "param": "134/146/147/165/166/167/168/235",  # meteorological parameters https://codes.ecmwf.int/grib/param-db/
        "step": "0/to/360/by/6",                     # forecast timestep (in hours) from base time
        "time": time,                                # base time of the forecast for each date
        "type": "pf",                                # type of forecast (pf = perturbed (ensemble) forecasts)
        "format":"netcdf",                           # output file format
        "target": OUTDIR+target,                     # output file
    })

def reqWithTimes(server, date, times=['00']):
    """
    Specify the starting times used in data retrieval and perform the data API request.

    Parameters
    ----------
    date : str
        year-month-day string
    times : array_like, optional {['00'], ['00', '12'], ['12']}
        list containing start times of the forecast
    """
    for time in times:
        target = f'ecmwf_sfc_{date}_{time}.nc'
        tigge_request(server, date, time, target)