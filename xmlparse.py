'''
Created on Sept 14, 2021

Name:  Ben Lamb
Program:  xmlparse.py
Description: Update price of plant in XML file
@author: blamb
'''
import xml.etree.ElementTree as ET
import sys

# input parameters
searchName = sys.argv[2]
percent = float(sys.argv[3]) / 100

# parse XML data file
tree = ET.parse(sys.argv[1])
root = tree.getroot()

plants = root.findall("PLANT")
for plant in plants:
    if plant.findtext("COMMON") == searchName:
        for x in plant.iter("PRICE"):
            plant_price = float(x.text)
            new_plant_price = (plant_price * percent) + plant_price
            x.text = str(new_plant_price)
tree.write(sys.argv[1])