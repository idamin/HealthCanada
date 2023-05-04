import requests
import json
import cred
from openpyxl import Workbook, load_workbook

wb = load_workbook('test_file1.xlsx')
ws = wb.active

din_list = []
for dins in ws['A']: 
    din_list.append(dins.value)

print(din_list)

#response = requests.get('https://node.hres.ca/drug/product?key=' + cred.API_KEY + '&search=drug_identification_number:' + '02537648' )
