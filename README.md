# Arctic Weather Ensemble Validation

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