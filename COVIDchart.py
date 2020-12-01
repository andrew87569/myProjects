from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)
soup = BeautifulSoup(r.text, features='html.parser')
table = soup.find('table')

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
tableData = pd.DataFrame(output_rows[8:59])
tableData = pd.DataFrame(tableData,columns=range(0,15))
tableData.columns = pd.Index(['#','Country','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','New Recovered','Active Cases','Critical Cases','Cases/1M pop','Deaths/1M pop','Total Tests','Tests/1M pop','Population'])
tableData.index = pd.Index(['' for i in range(51)])

print(tableData)