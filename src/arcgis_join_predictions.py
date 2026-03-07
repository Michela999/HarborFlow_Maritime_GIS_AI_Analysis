import arcpy
import os

project_folder = r"C:\Users\miche\Documents\HarborFlow_Fresh"

output_folder = os.path.join(project_folder, "data", "processed")
output_shapefile = os.path.join(output_folder, "AIS_points_predicted.shp")
predictions_table = os.path.join(output_folder, "predictions_table")

arcpy.env.workspace = output_folder
arcpy.env.overwriteOutput = True

arcpy.management.JoinField(
    in_data=output_shapefile,
    in_field="ShipName",          # <-- corrected
    join_table=predictions_table,
    join_field="shipname"
)

print("✅ Join corrected successfully.")