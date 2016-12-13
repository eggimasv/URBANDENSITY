# This file generates Folders and data for then executing the Urban Block Generator


import arcpy
import os


# Inputs
#pathToGenerateFolderStructure = "C:\P4_CH_NEU"   
#pathToGenerateFolderStructure = "F:\P4_GEMEINDEN" #GEMEINDEN         
pathToGenerateFolderStructure = "F:\P4_FISHNET_NEU" #GEMEINDEN     

inputShapeCHPaths = "Q:\\Abteilungsprojekte\\eng\\SWWData\\Eggimann_Sven\\07-Fallbeispiele\\04-finalCH"  # Path with WWTP Catchements

inputShapeWithWWTP = inputShapeCHPaths + "\\" + "WWTP_catchements2014_ALLDATA.shp"  # Path with WWTP Catchements 
#inputShapeWithWWTPNEwGeometry = inputShapeCHPaths + "\\" + "01GemeindeCalculations" + "\\" + "Gemeinden_GeometrieCH.shp"  # Path with WWTP Catchements #GEMEINDEN
inputShapeWithWWTPNEwGeometry = inputShapeCHPaths + "\\" + "02RasterCalculations" + "\\" + "fisnhet7200_data_selection.shp"  # Path with WWTP Catchements #GEMEINDEN


# Create Main Folder
os.mkdir(pathToGenerateFolderStructure)                         # Create Main Folder
#rows = arcpy.da.SearchCursor(inputShapeWithWWTP, ["ARA_Nr"])    # Read WWTP numbers
#rows = arcpy.da.SearchCursor(inputShapeWithWWTPNEwGeometry, ["BFS_NUMMER"])    # Read WWTP numbers #GEMEINDEN       
rows = arcpy.da.SearchCursor(inputShapeWithWWTPNEwGeometry, ["FISH_ID"])    # Read WWTP numbers #GEMEINDEN       

# ------------------------
# Assign Coordinages of CH shapefiles
# ------------------------
SwisscordSys = arcpy.SpatialReference(21781) # EPSG:21781 ,CH1903 / LV03 # Swiss Coordinate System
scrapcnt= 0

'''cnt = 0
for i in rows:
    #print i
    if i[0] == 406:
        print("CNT: FOUND; " + str(cnt))
    cnt += 1
prnt(":..")
'''

ccc = 0
for row in rows:
    
    # scrap
    '''if ccc < 322: #fishnet 72, 73
        ccc += 1
        continue
    '''
        
    
    # Create Folder
    Ara_ID = row[0]
    print("Ara_ID: " + str(Ara_ID))
    folderARAID = pathToGenerateFolderStructure + "\\" + str(int(Ara_ID))
    
    #os.mkdir(folderARAID)
    exit = False
    while exit == False:
        newFolderID = 1
        try:
            print("Created Gemeinde Enklave NR: " + str(Ara_ID))
            os.mkdir(folderARAID)
            exit = True
        except:
            print("Already created Gemeinde: " + str(Ara_ID))
            folderARAID = str(folderARAID) + str(1000) + str(newFolderID)
            newFolderID += 1
    
    print("-------------------------------------------")
    print("Made Folder with AraID: " + str(folderARAID))
    print("-------------------------------------------")
    
    # CH datasetz
    #WWTPgeometry = inputShapeWithWWTP + "\\" + "WWTP_catchements2014.shp" #
    WWTPgeometry = inputShapeWithWWTPNEwGeometry #Gemeinden
    
    DEM_CH = inputShapeWithWWTP + "\\" + "CH_dem100.shp"
    street_CH = inputShapeWithWWTP + "\\" + "CH_Street25_NEU_simplified_Clip.shp"
    geb_CH = inputShapeWithWWTP + "\\" + "CH_buildings_data_ARA_pt_inhabited.shp"
    railroad_CH = inputShapeWithWWTP + "\\" + "CH_railroad.shp"
    settlement_CH = inputShapeWithWWTP + "\\" + "CH_settlementArea.shp"
    
    #Out datasetz
    street_clip = folderARAID + "\\" + "street_simplified_split.shp"
    geb_inhab = folderARAID + "\\" + "buildings_inhabited.shp"
    dem_clip = folderARAID + "\\" + "dem_point.shp"
    railway_clip = folderARAID + "\\" + "railwayNetwork.shp"
    extent_r = folderARAID + "\\" + "extentPoly.shp"
    extent_f = folderARAID + "\\" + "extent_gem.shp"
    settlement_clip = folderARAID + "\\" + "settlementArea.shp"
       
    # Select ARA Catchement
    arcpy.MakeFeatureLayer_management(WWTPgeometry, "lyr") 
    #selectionCatchement = arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "ARA_NR = " + str(Ara_ID))
    #selectionCatchement = arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "BFS_NUMMER = " + str(Ara_ID)) #GEmeinden
    selectionCatchement = arcpy.SelectLayerByAttribute_management("lyr", "NEW_SELECTION", "FISH_ID = " + str(Ara_ID)) #GEmeinden
    arcpy.CopyFeatures_management("lyr", extent_f)              # Export catchment extent
    
    #For DEM, create a rectangle around extent for clip
    ext = arcpy.Describe(extent_f).extent
    array = arcpy.Array()
    array.add(ext.lowerLeft)
    array.add(ext.lowerRight)
    array.add(ext.upperRight)
    array.add(ext.upperLeft)
    array.add(ext.lowerLeft)
    polygon = arcpy.Polygon(array) 
    arcpy.CopyFeatures_management(polygon, extent_r)
    del array
    del polygon
    
    # Clip datasets
    arcpy.Clip_analysis(street_CH, selectionCatchement, street_clip)    # Clip street
    arcpy.Clip_analysis(railroad_CH, selectionCatchement, railway_clip)    # Clip street
    arcpy.Clip_analysis(geb_CH, selectionCatchement, geb_inhab)          # Clip Buildings
    arcpy.Clip_analysis(DEM_CH, extent_r, dem_clip)                     # Clip DEM
    arcpy.Clip_analysis(settlement_CH, selectionCatchement, settlement_clip)  # Clip settlement area
    
    # Define Coordinate System
    arcpy.DefineProjection_management(street_CH, SwisscordSys)
    arcpy.DefineProjection_management(railroad_CH, SwisscordSys)
    arcpy.DefineProjection_management(geb_CH, SwisscordSys)
    arcpy.DefineProjection_management(DEM_CH, SwisscordSys)
    arcpy.DefineProjection_management(settlement_clip, SwisscordSys)
    
    # Delete Layer Field
    arcpy.Delete_management("lyr")