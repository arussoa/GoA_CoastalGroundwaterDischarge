#!/usr/bin/env python
# coding: utf-8

#Code to calculate yearly sums of GoA RM and convert to .csv for transfer into GIS

import xarray as xr    
import numpy as np
import pandas as pd

ds = xr.open_dataset("goa_discharge_time_series_cfsr_19790901_20140831.nc", decode_times=False)


import datetime
t = ds.time[0].data
times = [datetime.datetime.fromordinal(int(t)) + datetime.timedelta(days=t%1) - datetime.timedelta(days=366) for t in ds.time.data]


ds2 = ds.set_coords({'time': pd.to_datetime(times)})


q = (xr.DataArray(ds.q.data, dims=('loc', 'time'), coords={'time': pd.to_datetime(times)}))*86400
lat = xr.DataArray(ds.lat.data, dims=('loc',))
lon = xr.DataArray(ds.lon.data, dims=('loc',))
ds2 = xr.Dataset(dict(q=q, lat=lat, lon=lon))
waterYears = [t.year+1 if t.month >= 9 else t.year for t in pd.DatetimeIndex(ds2.time.data)]
wy = xr.DataArray(waterYears, dims=('time'), name='wy')
ds2['wy'] = wy
qsum = xr.DataArray(ds2.swap_dims({'time': 'wy'}).q.groupby('wy').sum().data, dims=('loc', 'year'), coords={'year': range(1980, 2015)})


yearly = xr.Dataset(dict(q=qsum, lat=ds2.lat, lon=ds2.lon))
yrly_df = xr.Dataset.to_dataframe(yearly)
df_yr = yrly_df.pivot_table(index=['loc', 'lat', 'lon'], columns='year', values='q')
df_yr.to_csv('q_yearly.csv')


total = (df_yr.sum())/1000000000
total.name = 'Q_yr'
df_yr = df_yr.append(total.transpose())


FWD_yr = df_yr.loc['Q_yr', '1980':'2014']
FWD_yr.to_csv('Q_FWD.csv')
