# Arctic Weather Ensemble Validation

Code and figures from model validation of [ECMWF](https://www.ecmwf.int/en/forecasts) [ensemble forecasts](https://confluence.ecmwf.int/display/FUG/ENS+-+Ensemble+Forecasts) against [NOAA Arctic Saildrone data](https://data.pmel.noaa.gov/pmel/erddap/search/index.html?page=1&itemsPerPage=1000&searchFor=NOAA%2FPMEL+2019+Arctic+Saildrone+Mission) documented in:

Yamane MT, Zhang C  
[*Validation of ECMWF Ensemble Forecasts Against Saildrone Observations in the Arctic*](https://ui.adsabs.harvard.edu/abs/2021AGUFM.C35D0915Y/abstract)

which was presented at [AGU](https://www.agu.org/) Fall Meeting 2021 and is a product of Yamane's 2021 [NOAA Hollings](https://www.noaa.gov/office-education/hollings-scholarship) summer internship.

**figures** stores example figures used for the research poster

**forecasts** stores ECMWF ensemble forecast data with data retrieval, EDA, and processing scripts

**saildrones** stores saildrone data with EDA and processing scripts

## Dependencies
* ecmwfapi
* matplotlib
* numpy
* xarray

## Directory Structure
```
.
|-- figures
|   |-- err_oneday
|   |   `-- .gitignore
|   |-- err_onemonth
|   |   `-- .gitignore
|   |-- err_fulltime
|   |   `-- .gitignore
|   `-- .gitignore
|-- forecasts
|   |-- combined
|   |   |-- .gitignore
|   |-- filtered
|   |   `-- .gitignore
|   |-- full
|   |   `-- .gitignore
|   |-- REQUESTS.py
|   |-- retrieve_forecast_data_even.py
|   |-- retrieve_forecast_data_odd.py
|   |-- retrieve_forecast_data_oneday.py
|   `-- retrieve_forecast_data.ipynb
|-- saildrones
|   |-- all
|   |   |-- Arctic2019_sd1034_all.nc
|   |   |-- Arctic2019_sd1035_all.nc
|   |   |-- Arctic2019_sd1036_all.nc
|   |   `-- Arctic2019_sd1037_all.nc
|   |-- filtered
|   |   |-- Arctic2019_sd1034_filtered.nc
|   |   |-- Arctic2019_sd1035_filtered.nc
|   |   |-- Arctic2019_sd1036_filtered.nc
|   |   `-- Arctic2019_sd1037_filtered.nc
|   |-- saildrone_eda.ipynb
|   |-- saildrone_filter.ipynb
|   |-- saildrone_filter.py
|   |-- saildrone_filter_figures.ipynb
|   `-- saildrone_path.ipynb
`-- README.md
```
