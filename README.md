# Arctic Weather Ensemble Validation

Code and figures for model validation of [ECMWF Arctic weather ensemble forecasts](https://confluence.ecmwf.int/display/FUG/ENS+-+Ensemble+Forecasts) using [NOAA Saildrone data](https://data.pmel.noaa.gov/pmel/erddap/search/index.html?page=1&itemsPerPage=1000&searchFor=NOAA%2FPMEL+2019+Arctic+Saildrone+Mission) data documented in:

Yamane MT, Zhang C
[*Validation of ECMWF Ensemble Forecasts Against Saildrone Observations in the Arctic*](https://ui.adsabs.harvard.edu/abs/2021AGUFM.C35D0915Y/abstract)

which is a product of Yamane's 2021 [NOAA Hollings](https://www.noaa.gov/office-education/hollings-scholarship) summer internship.

**figures** stores example figures used for the research poster

**forecasts** stores ECMWF ensemble forecast data with data retrieval, processing, and analysis scripts

**saildrones** stores saildrone data with relevant processing and analysis scripts

## Dependencies
* ecmwfapi
* matplotlib (for figures)
* numpy
* xarray

## Directory Structure
```
.
|-- figures
|   |-- err_oneday
|   |   `-- temp
|   |-- err_onemonth
|   |   `-- temp
|   |-- err_fulltime
|   |   `-- temp
|   `-- temp
|-- forecasts
|   |-- combined
|   |   |-- temp
|   |-- filtered
|   |   `-- temp
|   |-- full
|   |   |-- temp
|   `-- temp
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
`-- temp
```