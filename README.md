# synthea_NLM_api_demo
Using Synthea's synthetic patient data and the National Library of Medicine's (NLM) Drug Interaction API to determine drug-drug interactions.

## Summary of approach

Per the instructions provided, I first downloaded the 1000 patient sample set (https://synthea.mitre.org/downloads). I looked through each CSV file and identified the medications.csv and patients.csv files would be the primary files to use. Within the medications.csv file, I assumed (and later determined) the "CODE" column represented the RxNorm code/identifier. I noticed for each unique patient in medications.csv, there were multiple medications that were prescribed at varying start and end points. For data corroboration purposes, I compared a handul of patient IDs in medications.csv to patient IDs in patients.csv, to ensure patients appeared in both data sets. 

Next, I navigated to the National Library of Medicine (NLM) Drug Interaction API (https://rxnav.nlm.nih.gov/InteractionAPIREST.html#uLink=Interaction_REST_findInteractionsFromList). I determined that using the "/list" REST resource would be the best way to find the interactions between multiple drugs, given a patient could be prescribed multiple medications. After reviewing an example API GET call for a list of drugs, I proceeded to develop my program.

I decided on using Python (via the PyCharm IDE) to develop my application, given the ease of using third-party libraries for data manipulation and the faster time-to-write code. I installed the following third-party libraries:



## List of assumptions

In the medications.csv file:
1) Assumed the "CODE" column represented the RxNorm code used to encode medications.
