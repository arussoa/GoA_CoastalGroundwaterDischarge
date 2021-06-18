#!Following performed in ESRI ArcPy environment
#Coding: utf-8

#Extracting coastal catchment CGD and attributes

import arcpy
from arcpy.ia import *
from arcpy.ia import *

def CGD_GRL_3():  # CGD_GRL_3


    arcpy.env.overwriteOutput = False

    
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

    #Input data
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx")
    AKStategeol_poly = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\AKStategeol_poly"
    q_yearly = "q_yearly"
    dem_GoA = arcpy.Raster("dem_GoA")
    goa_wtrshd = arcpy.Raster("goa_wtrshd")
    Kodiac_Shekilof = "Kodiac_Shekilof"
    CookInlet = "CookInlet"
    PWS_CR = "PWS_CR"
    CentralCoast = "CentralCoast"
    Southeast = "Southeast"
    NLCD_2001_Land_Cover_AK_20200724_img = arcpy.Raster("C:\\Users\\arussoa\\Desktop\\CGD_GRL\\NLCD_2001_Land_Cover_AK_20200724.img")
    Kodiac_Shekilof_3_ = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Kodiac_Shekilof"
    CookInlet_3_ = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CookInlet"
    PWS_CR_3_ = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\PWS_CR"
    CentralCoast_3_ = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CentralCoast"
    Southeast_3_ = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Southeast"
    AK_Glaciers = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\AK_Glaciers"

   
    AKStategeol_poly_Layer, Count = arcpy.management.SelectLayerByAttribute(in_layer_or_view=AKStategeol_poly, selection_type="NEW_SELECTION", where_clause="STATE_LABE = 'Qs'", invert_where_clause="")

    
    q_yearly_2_, Output_Layer_Names, Count_2_ = arcpy.management.SelectLayerByLocation(in_layer=[q_yearly], overlap_type="WITHIN_A_DISTANCE", select_features=AKStategeol_poly_Layer, search_distance="500 Meters", selection_type="NEW_SELECTION", invert_spatial_relationship="NOT_INVERT")

   
    FlowDir = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\FlowDir"
    Flow_Direction = FlowDir
    Output_drop_raster = ""
    with arcpy.EnvManager(mask="goa_wtrshd"):
        FlowDir = arcpy.sa.FlowDirection(in_surface_raster=dem_GoA, force_flow="NORMAL", out_drop_raster=Output_drop_raster, flow_direction_type="D8")
        FlowDir.save(Flow_Direction)


   
    FlowAcc = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\FlowAcc"
    Flow_Accumulation = FlowAcc
    FlowAcc = arcpy.sa.FlowAccumulation(in_flow_direction_raster=FlowDir, in_weight_raster="", data_type="INTEGER", flow_direction_type="D8")
    FlowAcc.save(Flow_Accumulation)


    
    streamnet = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\streamnet"
    Raster_Calculator_2_ = streamnet
    streamnet =  SetNull(FlowAcc < 20, FlowAcc)
    streamnet.save(Raster_Calculator_2_)


   
    goa_hillshade = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\goa_hillshade"
    Hillshade = goa_hillshade
    with arcpy.EnvManager(mask="goa_wtrshd"):
        goa_hillshade = arcpy.sa.HillShade(in_raster=dem_GoA, azimuth=315, altitude=45, model_shadows="NO_SHADOWS", z_factor=1.5)
        goa_hillshade.save(Hillshade)


    
    wtrshd_poly = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\wtrshd_poly"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=goa_wtrshd, out_polygon_features=wtrshd_poly, simplify="NO_SIMPLIFY", raster_field="VALUE", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature=None)

    
    q_wtrshd = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\q_wtrshd"
    arcpy.analysis.SpatialJoin(target_features=wtrshd_poly, join_features=q_yearly_2_, out_feature_class=q_wtrshd, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_COMMON", field_mapping="Shape_Area \"Shape_Area\" false false true 0 Double 0 0,First,#,C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\wtrshd_poly,Shape_Area,-1,-1;ID_1 \"ID\" true true false 8 Double 0 0,First,#,q_yearly,ID,-1,-1;lon \"lon\" true true false 8 Double 0 0,First,#,q_yearly,lon,-1,-1;lat \"lat\" true true false 8 Double 0 0,First,#,q_yearly,lat,-1,-1;qmean7913 \"qmean7913\" true true false 8 Double 0 0,First,#,q_yearly,qmean7913,-1,-1;q79 \"q79\" true true false 8 Double 0 0,First,#,q_yearly,q79,-1,-1;q80 \"q80\" true true false 8 Double 0 0,First,#,q_yearly,q80,-1,-1;q81 \"q81\" true true false 8 Double 0 0,First,#,q_yearly,q81,-1,-1;q82 \"q82\" true true false 8 Double 0 0,First,#,q_yearly,q82,-1,-1;q83 \"q83\" true true false 8 Double 0 0,First,#,q_yearly,q83,-1,-1;q84 \"q84\" true true false 8 Double 0 0,First,#,q_yearly,q84,-1,-1;q85 \"q85\" true true false 8 Double 0 0,First,#,q_yearly,q85,-1,-1;q86 \"q86\" true true false 8 Double 0 0,First,#,q_yearly,q86,-1,-1;q87 \"q87\" true true false 8 Double 0 0,First,#,q_yearly,q87,-1,-1;q88 \"q88\" true true false 8 Double 0 0,First,#,q_yearly,q88,-1,-1;q89 \"q89\" true true false 8 Double 0 0,First,#,q_yearly,q89,-1,-1;q90 \"q90\" true true false 8 Double 0 0,First,#,q_yearly,q90,-1,-1;q91 \"q91\" true true false 8 Double 0 0,First,#,q_yearly,q91,-1,-1;q92 \"q92\" true true false 8 Double 0 0,First,#,q_yearly,q92,-1,-1;q93 \"q93\" true true false 8 Double 0 0,First,#,q_yearly,q93,-1,-1;q94 \"q94\" true true false 8 Double 0 0,First,#,q_yearly,q94,-1,-1;q95 \"q95\" true true false 8 Double 0 0,First,#,q_yearly,q95,-1,-1;q96 \"q96\" true true false 8 Double 0 0,First,#,q_yearly,q96,-1,-1;q97 \"q97\" true true false 8 Double 0 0,First,#,q_yearly,q97,-1,-1;q98 \"q98\" true true false 8 Double 0 0,First,#,q_yearly,q98,-1,-1;q99 \"q99\" true true false 8 Double 0 0,First,#,q_yearly,q99,-1,-1;q00 \"q00\" true true false 8 Double 0 0,First,#,q_yearly,q00,-1,-1;q01 \"q01\" true true false 8 Double 0 0,First,#,q_yearly,q01,-1,-1;q02 \"q02\" true true false 8 Double 0 0,First,#,q_yearly,q02,-1,-1;q03 \"q03\" true true false 8 Double 0 0,First,#,q_yearly,q03,-1,-1;q04 \"q04\" true true false 8 Double 0 0,First,#,q_yearly,q04,-1,-1;q05 \"q05\" true true false 8 Double 0 0,First,#,q_yearly,q05,-1,-1;q06 \"q06\" true true false 8 Double 0 0,First,#,q_yearly,q06,-1,-1;q07 \"q07\" true true false 8 Double 0 0,First,#,q_yearly,q07,-1,-1;q08 \"q08\" true true false 8 Double 0 0,First,#,q_yearly,q08,-1,-1;q09 \"q09\" true true false 8 Double 0 0,First,#,q_yearly,q09,-1,-1;q10 \"q10\" true true false 8 Double 0 0,First,#,q_yearly,q10,-1,-1;q11 \"q11\" true true false 8 Double 0 0,First,#,q_yearly,q11,-1,-1;q12 \"q12\" true true false 8 Double 0 0,First,#,q_yearly,q12,-1,-1;q13 \"q13\" true true false 8 Double 0 0,First,#,q_yearly,q13,-1,-1", match_option="INTERSECT", search_radius="", distance_field_name="")

    
    q_wtrshd_2_ = arcpy.management.AddFields(in_table=q_wtrshd, field_description=[["CC_Area_km2", "LONG", "", "", "", ""]])[0]

    
    q_wtrshd_3_ = arcpy.management.CalculateField(in_table=q_wtrshd_2_, field="CC_Area_km2", expression="(!Shape_Area! / 1000000) -1", expression_type="PYTHON3", code_block="", field_type="TEXT")[0]

    q_wtrshd_Layer, Count_3_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=q_wtrshd_3_, selection_type="NEW_SELECTION", where_clause="CC_Area_km2 <= 20", invert_where_clause="NON_INVERT")

    
    Qs_goa = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_goa"
    arcpy.analysis.Clip(in_features=AKStategeol_poly_Layer, clip_features=wtrshd_poly, out_feature_class=Qs_goa, cluster_tolerance="")

    
    bg_hillshade = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\bg_hillshade"
    Hillshade_2_ = bg_hillshade
    bg_hillshade = arcpy.sa.HillShade(in_raster=dem_GoA, azimuth=315, altitude=45, model_shadows="NO_SHADOWS", z_factor=1)
    bg_hillshade.save(Hillshade_2_)


   
    Q_CGD = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Q_CGD"
    arcpy.analysis.Clip(in_features=q_wtrshd_Layer, clip_features=q_wtrshd_2_, out_feature_class=Q_CGD, cluster_tolerance="")

    
    Q_CGD_xls = "G:\\My Drive\\Research\\Manuscripts\\GoA_CGD\\Excel\\Q_CGD.xls"
    arcpy.conversion.TableToExcel(Input_Table=Q_CGD, Output_Excel_File=Q_CGD_xls, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

    
    CGD_KIS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CGD_KIS"
    arcpy.analysis.Clip(in_features=Q_CGD, clip_features=Kodiac_Shekilof, out_feature_class=CGD_KIS, cluster_tolerance="")

   
    CGD_Kodiak_Shek_xlsx = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_Kodiak_Shek.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=CGD_KIS, Output_Excel_File=CGD_Kodiak_Shek_xlsx, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

    
    CGD_CI = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CGD_CI"
    arcpy.analysis.Clip(in_features=Q_CGD, clip_features=CookInlet, out_feature_class=CGD_CI, cluster_tolerance="")

    
    CGD_CookInlet_xlsx = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_CookInlet.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=CGD_CI, Output_Excel_File=CGD_CookInlet_xlsx, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

   
    CGD_PWS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CGD_PWS"
    arcpy.analysis.Clip(in_features=Q_CGD, clip_features=PWS_CR, out_feature_class=CGD_PWS, cluster_tolerance="")

    
    CGD_PWS_xlsx = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_PWS.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=CGD_PWS, Output_Excel_File=CGD_PWS_xlsx, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

    
    CGD_Central = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CGD_Central"
    arcpy.analysis.Clip(in_features=Q_CGD, clip_features=CentralCoast, out_feature_class=CGD_Central, cluster_tolerance="")

    
    CGD_Central_xlsx = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_Central.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=CGD_Central, Output_Excel_File=CGD_Central_xlsx, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

    
    CGD_Southeast = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CGD_Southeast"
    arcpy.analysis.Clip(in_features=Q_CGD, clip_features=Southeast, out_feature_class=CGD_Southeast, cluster_tolerance="")

    
    CGD_Southeast_xlsx = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_Southeast.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=CGD_Southeast, Output_Excel_File=CGD_Southeast_xlsx, Use_field_alias_as_column_header="ALIAS", Use_domain_and_subtype_description="CODE")

    
    AKStategeol_poly_Layer_2_, Count_4_ = arcpy.management.SelectLayerByAttribute(in_layer_or_view=AKStategeol_poly, selection_type="NEW_SELECTION", where_clause="AGE_RANGE = 'Holocene' Or AGE_RANGE = 'Quaternary'", invert_where_clause="INVERT")

   
    bedrock = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\bedrock"
    arcpy.management.Dissolve(in_features=AKStategeol_poly_Layer_2_, out_feature_class=bedrock, dissolve_field=[], statistics_fields=[], multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")

    
    GoA_CC_landcover = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\GoA_CC_landcover"
    Extract_by_Mask = GoA_CC_landcover
    GoA_CC_landcover = arcpy.sa.ExtractByMask(in_raster=NLCD_2001_Land_Cover_AK_20200724_img, in_mask_data=Q_CGD)
    GoA_CC_landcover.save(Extract_by_Mask)


    
    KIS_LC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\KIS_LC"
    Extract_by_Mask_3_ = KIS_LC
    KIS_LC = arcpy.sa.ExtractByMask(in_raster=GoA_CC_landcover, in_mask_data=Kodiac_Shekilof_3_)
    KIS_LC.save(Extract_by_Mask_3_)


    
    CI_LC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CI_LC"
    Extract_by_Mask_4_ = CI_LC
    CI_LC = arcpy.sa.ExtractByMask(in_raster=GoA_CC_landcover, in_mask_data=CookInlet_3_)
    CI_LC.save(Extract_by_Mask_4_)


    
    PWS_LC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\PWS_LC"
    Extract_by_Mask_5_ = PWS_LC
    PWS_LC = arcpy.sa.ExtractByMask(in_raster=GoA_CC_landcover, in_mask_data=PWS_CR_3_)
    PWS_LC.save(Extract_by_Mask_5_)


    
    CenCos_LC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CenCos_LC"
    Extract_by_Mask_6_ = CenCos_LC
    CenCos_LC = arcpy.sa.ExtractByMask(in_raster=GoA_CC_landcover, in_mask_data=CentralCoast_3_)
    CenCos_LC.save(Extract_by_Mask_6_)


    
    SE_LC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\SE_LC"
    Extract_by_Mask_7_ = SE_LC
    SE_LC = arcpy.sa.ExtractByMask(in_raster=GoA_CC_landcover, in_mask_data=Southeast_3_)
    SE_LC.save(Extract_by_Mask_7_)


    
    goa_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\goa_slope"
    Slope = goa_slope
    goa_slope = arcpy.sa.Slope(in_raster=dem_GoA, output_measurement="DEGREE", z_factor=1, method="PLANAR", z_unit="METER")
    goa_slope.save(Slope)


    
    GoA_CC_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\GoA_CC_slope"
    Extract_by_Mask_2_ = GoA_CC_slope
    GoA_CC_slope = arcpy.sa.ExtractByMask(in_raster=goa_slope, in_mask_data=Q_CGD)
    GoA_CC_slope.save(Extract_by_Mask_2_)


    
    KIS_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\KIS_slope"
    Extract_by_Mask_8_ = KIS_slope
    KIS_slope = arcpy.sa.ExtractByMask(in_raster=GoA_CC_slope, in_mask_data=Kodiac_Shekilof_3_)
    KIS_slope.save(Extract_by_Mask_8_)


    
    CI_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CI_slope"
    Extract_by_Mask_9_ = CI_slope
    CI_slope = arcpy.sa.ExtractByMask(in_raster=GoA_CC_slope, in_mask_data=CookInlet_3_)
    CI_slope.save(Extract_by_Mask_9_)


    
    PWS_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\PWS_slope"
    Extract_by_Mask_10_ = PWS_slope
    PWS_slope = arcpy.sa.ExtractByMask(in_raster=GoA_CC_slope, in_mask_data=PWS_CR_3_)
    PWS_slope.save(Extract_by_Mask_10_)


    
    CenCoa_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CenCoa_slope"
    Extract_by_Mask_11_ = CenCoa_slope
    CenCoa_slope = arcpy.sa.ExtractByMask(in_raster=GoA_CC_slope, in_mask_data=CentralCoast_3_)
    CenCoa_slope.save(Extract_by_Mask_11_)


    
    SE_slope = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\SE_slope"
    Extract_by_Mask_12_ = SE_slope
    SE_slope = arcpy.sa.ExtractByMask(in_raster=GoA_CC_slope, in_mask_data=Southeast_3_)
    SE_slope.save(Extract_by_Mask_12_)


    
    AK_Glaciers_Dis = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\AK_Glaciers_Dis"
    arcpy.management.Dissolve(in_features=AK_Glaciers, out_feature_class=AK_Glaciers_Dis, dissolve_field=[], statistics_fields=[], multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")

    
    Qs_CC_glaciers = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_CC_glaciers"
    arcpy.analysis.Clip(in_features=AK_Glaciers_Dis, clip_features=Q_CGD, out_feature_class=Qs_CC_glaciers, cluster_tolerance="")

    
    glaciers_KIS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\glaciers_KIS"
    arcpy.analysis.Clip(in_features=Qs_CC_glaciers, clip_features=Kodiac_Shekilof, out_feature_class=glaciers_KIS, cluster_tolerance="")

    
    glaciers_CI = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\glaciers_CI"
    arcpy.analysis.Clip(in_features=Qs_CC_glaciers, clip_features=CookInlet, out_feature_class=glaciers_CI, cluster_tolerance="")

    
    glaciers_PWS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\glaciers_PWS"
    arcpy.analysis.Clip(in_features=Qs_CC_glaciers, clip_features=PWS_CR, out_feature_class=glaciers_PWS, cluster_tolerance="")

    
    glaciers_CC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\glaciers_CC"
    arcpy.analysis.Clip(in_features=Qs_CC_glaciers, clip_features=CentralCoast, out_feature_class=glaciers_CC, cluster_tolerance="")

    
    glaciers_SE = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\glaciers_SE"
    arcpy.analysis.Clip(in_features=Qs_CC_glaciers, clip_features=Southeast, out_feature_class=glaciers_SE, cluster_tolerance="")

    
    ocean = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\ocean"
    Raster_Calculator = ocean
    ocean =   SetNull(dem_GoA > 0, dem_GoA) 
    ocean.save(Raster_Calculator)


    
    ocean_poly = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\ocean_poly"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=ocean, out_polygon_features=ocean_poly, simplify="NO_SIMPLIFY", raster_field="Value", create_multipart_features="MULTIPLE_OUTER_PART", max_vertices_per_feature=None)

    
    ocean_outline = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\ocean_outline"
    arcpy.management.PolygonToLine(in_features=ocean_poly, out_feature_class=ocean_outline, neighbor_option="IGNORE_NEIGHBORS")

    
    goa_coastline = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\goa_coastline"
    arcpy.analysis.Clip(in_features=ocean_outline, clip_features=wtrshd_poly, out_feature_class=goa_coastline, cluster_tolerance="")

    
    Qs_coastline = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=Q_CGD, out_feature_class=Qs_coastline, cluster_tolerance="")

    
    Qs_coastline_KIS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline_KIS"
    arcpy.analysis.Clip(in_features=Qs_coastline, clip_features=Kodiac_Shekilof, out_feature_class=Qs_coastline_KIS, cluster_tolerance="")

    
    Qs_coastline_CI = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline_CI"
    arcpy.analysis.Clip(in_features=Qs_coastline, clip_features=CookInlet, out_feature_class=Qs_coastline_CI, cluster_tolerance="")

    
    Qs_coastline_PWS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline_PWS"
    arcpy.analysis.Clip(in_features=Qs_coastline, clip_features=PWS_CR, out_feature_class=Qs_coastline_PWS, cluster_tolerance="")

    
    Qs_coastline_CC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline_CC"
    arcpy.analysis.Clip(in_features=Qs_coastline, clip_features=CentralCoast, out_feature_class=Qs_coastline_CC, cluster_tolerance="")

    
    Qs_coastline_SE = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\Qs_coastline_SE"
    arcpy.analysis.Clip(in_features=Qs_coastline, clip_features=Southeast, out_feature_class=Qs_coastline_SE, cluster_tolerance="")

    
    CL_KIS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CL_KIS"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=Kodiac_Shekilof, out_feature_class=CL_KIS, cluster_tolerance="")

    
    CL_CI = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CL_CI"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=CookInlet, out_feature_class=CL_CI, cluster_tolerance="")

    
    CL_PWS = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CL_PWS"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=PWS_CR, out_feature_class=CL_PWS, cluster_tolerance="")

    
    CL_CC = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CL_CC"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=CentralCoast, out_feature_class=CL_CC, cluster_tolerance="")

    
    CL_SE = "C:\\Users\\arussoa\\Desktop\\CGD_GRL\\MyProject\\CGD_GRL.gdb\\CL_SE"
    arcpy.analysis.Clip(in_features=goa_coastline, clip_features=Southeast, out_feature_class=CL_SE, cluster_tolerance="")

if __name__ == '__main__':
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\arussoa\Desktop\CGD_GRL\MyProject\CGD_GRL.gdb", workspace=r"C:\Users\arussoa\Desktop\CGD_GRL\MyProject\CGD_GRL.gdb"):
        CGD_GRL_3()
