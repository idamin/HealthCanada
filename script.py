import requests
import json
import cred
import pandas as pd
from openpyxl import Workbook, load_workbook


#-------------------Helper Functions-------------------
'''
Obtains Manufacturer, Product, Notice of Compliance Date, and the Medical Ingridients
from the Health Canada API given the Drug Information Number (DIN).

Note that the NOC Database and the DGD database have different nomenclature
for the above terms, the code below follows the NOC database. 
'''

def get_data(din):
   response =  requests.get('https://node.hres.ca/drug/product?key=' + cred.API_KEY + '&search=drug_identification_number:' + din).json()
   manufacturer = response['results'][0]['_source']['company']['company_name']  
   product = response['results'][0]['_source']['brand_name']
   NOCDate = response['results'][0]['_source']['status_approved_date'][0][:10]
   MedicalIngredients = response['results'][0]['_source']['active_ingredients']
   return[product,manufacturer,NOCDate,MedicalIngredients]
#------------------------------------------------------
#get_test = get_data('02537532')

wb = load_workbook('test_file1.xlsx')
ws = wb.active

din_list = []
for dins in ws['A']: 
    din_list.append(dins.value)

din_list = din_list[1:]


