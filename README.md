# synthea_NLM_api_demo
Using Synthea's synthetic patient data and the National Library of Medicine's (NLM) Drug Interaction API to determine drug-drug interactions.

## Summary of approach

Per the instructions provided, I first downloaded the 1000 patient sample set (https://synthea.mitre.org/downloads). I looked through each CSV file and identified that the medications.csv and patients.csv files would be the primary files to use. For data corroboration purposes, I compared a handul of patient IDs in medications.csv to patient IDs in patients.csv, to ensure patients appeared in both data sets. Within the medications.csv file, I assumed (and later determined) the "CODE" column represented the RxNorm code/identifier. I also noticed that for each unique patient in medications.csv, there were multiple medications that were prescribed at varying start and stop/end dates. I made the assumption that drug interactions could only occur for medications that were currently in use (i.e. no end/stop end date recorded). 

After reviewing the data sets, I navigated to the National Library of Medicine (NLM) Drug Interaction API (https://rxnav.nlm.nih.gov/InteractionAPIREST.html#uLink=Interaction_REST_findInteractionsFromList). I determined that using the "/list" REST resource would be the best way to find the interactions between multiple drugs, given a patient could be prescribed multiple medications. After reviewing an example API GET call for a list of drugs, I proceeded to develop my program.

I decided on using Python (via the PyCharm IDE) to develop my application, given the ease of using third-party libraries for data manipulation and the faster time-to-write code. I imported the following third-party libraries and Python modules:

- Requests, release v2.22.0
- Pandas (v0.24.2)
- Json (Python Standard Library)

My Python program used Pandas to read the medications.csv file and create a DataFrame object. I trimmed this DataFrame to include only the columns associated with "START", "STOP", "PATIENT", and "CODE". Then, I excluded medication rows where the medication had "NaN" in its "START" column (based on the assumption made earlier to only consider "current" drug interactions). Next, I used Pandas' "groupby" function in conjunction with "apply" to create lists of drugs for each unique patient ID. I iterated through the drug list for each patient and concatenated each drug code with a "+" sign, to create a concatenated drug list to pass as a parameter to the GET API call. For each concatenated drug list, I called my customized API function and performed a search for the attribute "fullInteractionTypeGroup", incrementing a counter if this attribute appeared in the JSON onput for each API call.

As a result, my program yielded a total count of 402 drug interactions for the sample set.

## Summary of assumptions / questions
1) Only assuming drug-to-drug interactions. Drug interactions may occur for other reasons.
2) "CODE" column in medicines.csv represented the RxNorm code/identifier.
3) Assumed that drug interactions could only occur for medications that were currently in use (i.e. no end/stop end date recorded). 

# TODO: Summary of future modifications
1) Reduce search cost for "fullInteractionTypeGroup" attribute in JSON output from API call.
2) Removing duplicate instances of medications for data cleaning. Although duplicates appear to have no impact on the determination of whether the drugs cause interactions with each other.

## Creating a virtual environment and installing dependencies (MacOS/Linux)

Unzip the cloned repository and navigate into the root directory.

First, create a virtual environment. Virtual environments allow you to manage separate package installations for different projects. They create a “virtual” isolated Python installation and allow for easy installation of packages into that virtual installation. Run the following command to create a virtual environment:

``
$ python3 -m venv env
``

Activate a virtual environment:

``
$ source env/bin/activate
``

Install the required packages:

``
$ pip install requests

$ pip install pandas
``
## Running the application (MacOS/Linux)

After the packages have been installed in the virtual environment, run the application:

``
$ python interactions.py
``

