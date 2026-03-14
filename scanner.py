import csv
import re

# Regex patterns for SSN and Credit Card
SSN_PATTERN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
CC_PATTERN = re.compile(r'\b(?:\d[ -]*?){16}\b')

input_file = 'enterprise_access_logs.csv'
output_file = 'incident_report.csv'

incidents = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        payload = row.get('data_payload', '')
        violation_types = []
        if SSN_PATTERN.search(payload):
            violation_types.append('SSN Exposed')
        if CC_PATTERN.search(payload):
            violation_types.append('Credit Card Exposed')
        for violation in violation_types:
            incidents.append({
                'timestamp': row.get('timestamp', ''),
                'employee_id': row.get('employee_id', ''),
                'department': row.get('department', ''),
                'violation_type': violation
            })

# Write incidents to output CSV
if incidents:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'employee_id', 'department', 'violation_type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(incidents)

print(f"Total number of incidents found: {len(incidents)}")