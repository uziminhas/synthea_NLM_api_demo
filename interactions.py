import requests
import json
import pandas as pd

# Function for calling NLM API
def get_api_data(drug_list):
    try:
        url = 'https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis=' + drug_list
        response = (requests.get(url).text)
        response_json = json.loads(response)
        return response_json

    except Exception as e:
        raise e

# Read CSV file
df = pd.read_csv("medications.csv")

# Create new DataFrame with relevant columns
df = df[['START','STOP','PATIENT','CODE']]

# Exclude medications rows where the medication has been stopped (i.e. Asssumption that no "current" drug interactions will take place for medications that are stopped)
df = df[df['STOP'].isnull()]

# Create groups of drugs for each patient
groups_by_patient = df.groupby('PATIENT', sort=False)['CODE'].apply(lambda x: x.values.tolist())

# Declare variables for index counting and sum total of drug interactions
index = 1
count_drug_int = 0

# Iterate through each patient list of medications
for drug_list in groups_by_patient:
    joined_drug_list = "+".join(str(i) for i in drug_list)
    # print(i, " " , drug_list)
    index += 1
    data = get_api_data(joined_drug_list) # returns JSON response
    if 'fullInteractionTypeGroup' not in data:
        print('No drug interaction: ', joined_drug_list)
        continue
    count_drug_int += 1
    print('Drug interaction: ', joined_drug_list)

print('Total number of drug interactions: ', count_drug_int)