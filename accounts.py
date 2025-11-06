from time import time, sleep
import webbrowser
import boto3
from botocore.exceptions import UnauthorizedSSOTokenError, EndpointConnectionError, ClientError
#from dotenv import load_dotenv
import os
import logging
#load_dotenv()
import json
import boto3


org = boto3.client('organizations')

# Set up paginator
paginator = org.get_paginator('list_accounts') # Just prepares the paginator
# print(paginator)
# print("\n")

page_iterator = paginator.paginate() # Starts retrieving results
# print(page_iterator)
# print("\n")

# List to store filtered account IDs
account_ids = []

# Iterate over all pages
for page in page_iterator:
    # print(page)
    # print("\n")
    # Iterate over each account in the page
    for acct in page['Accounts']:
        # print(acct)
        # Skip unwanted accounts by Name
        if acct["Name"] in ["test","db","sandbox","test2","Dev","prod","test3","cosmos","rew3he"]:
            continue
        #print(acct)

        # Extract the account ID and append to the list
        account_ids.append(acct['Id'])

# Print the final list of account IDs
# print("\n")
# print(account_ids)
# print("\n")
#json_str = json.dumps(account_ids)
#print(json_str)

# print("\n")
result = ', '.join(account_ids)
output = {"account_ids": result}
print(json.dumps(output))

        



