import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = 'log_file.txt'
target_file = 'transformed_data.csv'

#Check number of file
list_csv = glob.glob('*.csv')
list_json = glob.glob('*.json')
list_xml = glob.glob('*.xml')
#Extract
def extract_from_csv(file_to_process):
    dataframe=pd.read_csv(file_to_process)
    return dataframe
def extract_from_json(file_to_process):
    dataframe=pd.read_json(file_to_process, lines=True)
    return dataframe
def extract_from_xml(file_to_process):
    dataframe=pd.DataFrame(columns=['name','height','weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find('name').text
        height = float(person.find('height').text)
        weight = float(person.find('weight').text)
        dataframe = pd.concat([dataframe, pd.DataFrame([{'name':name,'height':height,'weight':weight}])], ignore_index = True)
    return dataframe
def extract():
    #created an blank dataframe to hold the data
    extracted_data = pd.DataFrame(columns=['name','height','weight'])
    for csvfile in list_csv: # get all csv file
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)
    for jsonfile in list_json:
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)
    for xmlfile in list_xml:
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)
    return extracted_data
# Transform
def transform(data):
    data['height'] = round(data.height*0.0254,2)
    data['weight'] = round(data.weight*0.45359237,2)
    return data
print(transform(extract()))
# Loading
def load_data(target_file,transformed_data):
    transformed_data.to_csv(target_file)
#logging
def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 
#final Execute
#Execute time for extracted data
log_progress('Extract phase End')
log_progress('Extact phase Strated')
extracted_data = extract()
log_progress('Extract phase End')
#Execute time for transformation data
log_progress('Transform phase Started')
transformed_data = transform(extracted_data)
print('Transformed Data')
print(transformed_data)
log_progress("Transform phase Ended")
#Execute time for Loading Data
log_progress('Load phase Stated')
load_data(target_file,transformed_data)
log_progress('Load phase Ended')
log_progress("ETL Job Ended")
