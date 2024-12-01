import pandas as pd

# Load the Excel file
file_path = 'ComplianceCaseData1.xlsx'  # Replace with the correct file path
data = pd.ExcelFile(file_path)

# Display available sheets to understand the file structure
print("Available Sheets:", data.sheet_names)

# Load the relevant sheets (adjust names as necessary)
transactions = data.parse('transactions')  # Replace 'transactions' with the actual sheet name
merchants = data.parse('merchants')  # Replace 'merchants' with the actual sheet name if applicable

# Merge data if necessary (e.g., adding merchant details to transactions)
merged_df = pd.merge(transactions, merchants, on='merchant_id', how='left')

# Identify patterns: Transactions with similar amounts
high_frequency_values = merged_df.groupby(['merchant_id', 'amount']).size().reset_index(name='count')
suspicious_merchants = high_frequency_values[high_frequency_values['count'] > 10]  # Adjust threshold as needed

# Identify high-value transactions (e.g., above R$9,990)
high_value_transactions = merged_df[merged_df['amount'] > 9990]
high_value_summary = high_value_transactions.groupby('merchant_id').agg(
    transaction_count=('transaction_id', 'count'),
    total_amount=('amount', 'sum')
).reset_index()

# Combine results for further insights
suspicious_summary = suspicious_merchants.merge(
    high_value_summary, on='merchant_id', how='outer'
).fillna(0)

# Output the merchants with suspicious patterns
print("Merchants with suspicious patterns:")
print(suspicious_summary)

# Save the analysis to a file for review
suspicious_summary.to_csv('suspicious_merchants_analysis.csv', index=False)
print("Analysis saved to 'suspicious_merchants_analysis.csv'")
