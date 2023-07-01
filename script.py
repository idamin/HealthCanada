import requests
import json
import pandas as pd
from openpyxl import Workbook, load_workbook


#-------------------Helper Functions-------------------
'''
Obtains Manufacturer, Product, Notice of Compliance Date, and the Medical Ingridients
from the Health Canada API given the Drug Information Number (DIN).

Note that the NOC Database and the DGD database have different nomenclature
for the above terms, the code below follows the NOC database. 
'''

dins = ['02537044', '02537532', '02537648', '02537648']

def get_drug_product_data(din):
   response =  requests.get('https://health-products.canada.ca/api/drug/drugproduct/?din=' + din + '&lang=en&type=json').json()
   #drug_code = response[0]['drug_code']
   return response
#------------------------------------------------------
get_test = get_drug_product_data('02537532')

def get_dosage_form(drug_code):
    response_list = requests.get('https://health-products.canada.ca/api/drug/form/?id='+ str(drug_code) +'&lang=en&type=json').json()
    forms = []
    for response in range(len(response_list)):
        forms.append(response_list[response]['pharmaceutical_form_name'])
    return forms

def get_schedule(drug_code):
    response = requests.get('https://health-products.canada.ca/api/drug/schedule/?id='+ str(drug_code) +'&lang=en&type=json').json()
    return response[0]['schedule_name']

for din in dins:
    dp_data = get_drug_product_data(din)[0]
    drug_code = str(dp_data['drug_code'])
    schedule = get_schedule(drug_code)
    dosage_form = get_dosage_form(drug_code)
    print(schedule)

#---------------------------------------------------------------

'''
wb = load_workbook('test_file1.xlsx')
ws = wb.active

din_list = []
for dins in ws['A']: 
    din_list.append(dins.value)

din_list = din_list[1:]
'''


    


