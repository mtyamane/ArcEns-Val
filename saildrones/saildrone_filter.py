import os
import xarray as xr

INPATH = 'D:/saildrone/all/'
OUTPATH = 'D:/saildrone/filtered/'
SDVARS = ['TEMP_AIR_MEAN','BARO_PRES_MEAN','UWND_MEAN', 'VWND_MEAN','TEMP_SBE37_MEAN','RH_MEAN']

saildrone_files = os.listdir(INPATH)

for filename in saildrone_files:
    saildrone = xr.open_dataset(INPATH+filename)
    filtered = saildrone[SDVARS]
    
    outname = filename.replace('all', 'filtered')
    filtered.to_netcdf(OUTPATH+outname)