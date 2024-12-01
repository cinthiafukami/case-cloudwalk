import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker instance for generating random data
fake = Faker()

# Define the number of records
num_records = 1000

# Generate Fictional Data
def generate_data(num_records):
    data = []
    
    for _ in range(num_records):
        transaction_id = fake.uuid4()
        customer_id = fake.uuid4()
        merchant_id = random.choice(['M001', 'M002', 'M003', 'M004'])
        transaction_amount = random.randint(10, 20000)  # Transaction between $10 and $20,000
        transaction_date = fake.date_this_year()
        transaction_type = random.choice(['withdrawal', 'deposit', 'payment'])
        
        alert_status = random.choice([True, False])  # Randomly assign an alert (True = suspicious)
        alert_resolution = alert_status and random.choice([True, False])  # Alert is resolved if flagged
        risk_level = random.choice(['High', 'Medium', 'Low'])
        flagged_reason = random.choice(['Large transaction', 'Rapid transactions', 'Unusual merchant', 'No red flag'])

        # Append record to list
        data.append([transaction_id, customer_id, merchant_id, transaction_amount, transaction_date,
                     transaction_type, alert_status, alert_resolution, risk_level, flagged_reason])
    
    # Convert list of records into DataFrame
    df = pd.DataFrame(data, columns=['Transaction ID', 'Customer ID', 'Merchant ID', 'Transaction Amount', 
                                     'Transaction Date', 'Transaction Type', 'Alert Status', 
                                     'Alert Resolution', 'Risk Level', 'Flagged Reason'])
    return df

# Generate fictional AML data
aml_data = generate_data(num_records)

# Save to CSV or view the data
aml_data.to_csv("aml_data.csv", index=False)
print(aml_data.head())  # Display first 5 rows
