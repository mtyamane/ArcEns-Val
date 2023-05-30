# forecasts

Ensemble forecasts can be requested from [TIGGE Data Retrieval](https://apps.ecmwf.int/datasets/data/tigge/levtype=sfc/type=pf/) via the ECMWF API. Directions for installing the API package can be found [here](https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets). Test that the API and scripts are running properly by first running retrieve_forecast_data_oneday.py.  
NOTE: The .ecmwfapirc file should be placed in $HOME/.ecmwfapirc (Unix/Linux) or %USERPROFILE%\.ecmwfapirc (Windows)

**REQUESTS.py** holds the API call and helper functions for data retrieval.

**retrieve_forecast_data_even.py** prompts the user for a month to retrieve data for. Makes the forecast data requests for even days in the month.

**retrieve_forecast_data_odd.py** prompts the user for a month to retrieve data for. Makes the forecast data requests for odd days in the month.

**retrieve_forecast_data_oneday.py** makes a forecast data request for the day set in the script.

**retrieve_forecast_data.ipynb** (START HERE!) tests that the ecmwfapi package is installed and contains loops to ensure every day gets requested in a month.

## Dependencies
* ecmwfapi
* matplotlib
* numpy
* xarray
