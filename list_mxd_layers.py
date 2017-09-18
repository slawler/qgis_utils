# -*- coding: utf-8 -*-
"""
list_mxd_layers.py

Quick and Dirty script to check out contents of esri mxd

slawler@dewberry.com
9.18.2017
"""
from __future__ import print_function # arc-gis requires python2

import os
from collections import OrderedDict
import arcpy
                       
mxd = r"P:\Temp\slawler\NYC\CLIMATE_Basemap_10.1.mxd"                                
fout = r'C:\Users\slawler\Desktop\contents.tsv'                               

def print_mxd_contents(mxd, fout):
	from arcpy import mapping 
	mapDoc = mxd
	mxd = mapping.MapDocument(mapDoc) 
	lyrs = mapping.ListLayers(mxd) 
	shapes = {}
	features = {}
	errors, duplicates, total = 0, 0, 0

	for i, lyr in enumerate(lyrs):
	    #print(i, lyr)
	    total +=1     
	    try:
	        layer = lyr.dataSource
	        ext = os.path.basename(layer)[-4:]
	        
	        if ext =='.shp' and layer not in shapes:
	            shapes[i] = layer 
	            
	        elif '.gdb' in layer and layer not in features:
	            features[i] = layer 
	                        
	        else:
	            duplicates +=1

	    except:
	        print('Error on', i, lyr)
	        errors+=1 
	        
	shapes = OrderedDict(sorted(shapes.items()))
	features = OrderedDict(sorted(features.items()))
	    
	with open(fout, 'w') as f:
	    for key in shapes:        
	        f.write(str(key) + '\t' + shapes[key] + '\n')
	   
	    f.write('\n')
	    
	    for key in features:        
	        f.write(str(key) + '\t' + features[key] + '\n')
	        
	print('errors=' , errors)
	print('duplicates=' , duplicates)
	print('total = ', total)


    