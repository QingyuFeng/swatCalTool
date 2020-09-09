# -*- coding: utf-8 -*-
"""
Created on Tue May 12 2020 

This class is designed to be a collection of GDAL function in python.

@author: Qingyu.Feng
"""

##########################################################################
# Import modules #########################################################
##########################################################################
import os, sys, subprocess
import math

try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/OGR modules')



##########################################################################
# Define classes #########################################################
##########################################################################

def convertraster2ascii(fn_raster,
                        fn_ascii):
    
    """
    Translate the raster file into ascii
    """
    command = 'gdal_translate \
                -of AAIGrid \
                -b 1\
                %s %s' % (fn_raster,
                            fn_ascii)
                
    subprocess.call(command, shell=True)
    
    
    
#        # Open dataset
#        fid_raster = gdal.Open(fn_raster)
#        # Translate
#        fid_raster = gdal.Translate(fn_ascii,
#                                    fid_raster,
#                                    format='AAIGrid')
#        
#        # Close dataset
#        fid_raster = None


def gdalConvertRaster2Shapefile(fn_raster, 
                            fn_shapefile):
    
    # Open dataset
    sourceRaster = gdal.Open(fn_raster)
    hSrcBand = sourceRaster.GetRasterBand(1)
    bandArray = hSrcBand.ReadAsArray()
    outShapefile = fn_shapefile
    driver = ogr.GetDriverByName("ESRI Shapefile")
    if os.path.exists(outShapefile+".shp"):
        driver.DeleteDataSource(outShapefile+".shp")
    outDatasource = driver.CreateDataSource(outShapefile+ ".shp")
    outLayer = outDatasource.CreateLayer(fn_shapefile, srs=None)
    fieldName = "Value"
    """
    GDAL Polygonize(hSrcBand, 
                    hMaskBand,
                    hOutLayer,
                    iPixValueField,
                    papszOptions,
                    pfnProgress,
                    pProgressArg)
    """
    gdal.Polygonize( hSrcBand, None, outLayer, -1, [fieldName], callback=None )
    outDatasource.Destroy()
    sourceRaster = None


def gdalExtractbyMask(fn_srcraster, 
                fn_mask,
                fn_outraster):
    """
    Reference:
    http://erouault.blogspot.it/2015/10/gdal-and-ogr-utilities-as-library.html
    https://svn.osgeo.org/gdal/trunk/autotest/utilities/test_gdalwarp_lib.py
    http://gdal.org/gdalwarp.html
    """
    command = ['gdalwarp \
                -dstnodata 0 \
                -cutline %s \
                -crop_to_cutline \
                %s %s' % (fn_mask,
                            fn_srcraster,
                            fn_outraster)]
                
    subprocess.call(command[0], shell=True)
    


def reprojecttoUTMZone(fin, fout, utmzone):

    srcproj = "-s_srs '+proj=aea +lat_1=15 +lat_2=65 +lat_0=30 +lon_0=95 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'"
    # destproj = "'+proj=utm +zone={} +ellps=WGS84 +datum=WGS84 +units=m +no_defs '".format(utmzone);
    destproj = "EPSG:326{}".format(utmzone)
    """     command = ["gdalwarp {0} -t_srs {1} \
            -tr 30 30 \
            -r near \
            -dstnodata -99999999.0 \
            -of GTiff \
            -co COMPRESS=NONE\
            -co BIGTIFF=IF_NEEDED \
            {2} {3}".format(
            srcproj,  destproj,  fin, fout 
            )] """

    command = ["gdalwarp -t_srs {0} \
            -tr 30 30 \
            -r near \
            -dstnodata -99999999.0 \
            -of GTiff \
            -co COMPRESS=NONE\
            -co BIGTIFF=IF_NEEDED \
            {1} {2}".format(
            destproj,  fin, fout 
            )]
    print(command)

    subprocess.call(command[0], shell=True)



def long2UTMZone(longitude):

    utmzone = (math.floor((float(longitude) + 180)/6) % 60) + 1

    return utmzone








def readShapeAttributes(finshp):

    '''
    Read shapefile and return all values in the
    attritube table.
    '''

    # Check file existence:
    if not os.path.isfile(finshp):
        sys.exit('ERROR: Input file does not exist please check!')
        

    subStrAtt = dict()
    

    driver = ogr.GetDriverByName('ESRI Shapefile')

    dataSource = driver.Open(finshp, 0)
    layer = dataSource.GetLayer()

    # Get the field name
    field_names = [field.name for field in layer.schema]

    # Get the value of each field for all layers
    for feature in layer:
        values_list = [str(feature.GetField(j)) for j in field_names]
        
        subStrAtt[str(values_list[0])] = values_list
    
    

    return field_names, subStrAtt




