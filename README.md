# Arctic Weather Ensemble Validation

**saildrone_eda.ipynb** (START HERE!): Exploratory data analysis of saildrone data

**saildrone_filter.ipynb** tests how to make saildrone data only store variables of interest

**saildrone_filter.py** creates filtered saildrone .nc files with variables of interest

**saildrone_filter_figures.ipynb** stores timeseries plots of saildrone variables


## Dependencies
* ecmwfapi
* numpy
* xarray
* matplotlib (for figures)
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