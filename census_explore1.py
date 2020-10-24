#!/usr/bin/env python3
# Copyright October 2020 The Policy Pandas TPP Hackathon

# exploring the data

# import necessary packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

filepath = 'Census_2010/CENSUS2010BLOCKGROUPS_POLY.shp'
railfile = 'Census_2010/CENSUS2010RAIL_ARC.shp'
censusBlocks = gpd.read_file(filepath)
rail = gpd.read_file(railfile)
print('read the files')
# print(censusBlocks.head(10))
# print(type(censusBlocks))
# print(censusBlocks.total_bounds)
# print(censusBlocks.shape)
# censusBlocks.to_csv('censusBlocks_info.csv')
fig, ax = plt.subplots(figsize = (10,10))
censusBlocks.geometry.boundary.plot(color=None, edgecolor='g', ax=ax, linewidth=1)
rail.plot(ax=ax, color='k')
plt.show()