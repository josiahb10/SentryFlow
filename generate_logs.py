import csv
import random
import datetime

departments = [
    "Engineering", "HR", "Finance", "Marketing", "Sales", "IT", "Operations"
]
actions = [
    "login", "logout", "view", "edit", "delete", "download", "upload"
]
resources = [
    "intranet", "payroll", "customer_db", "email", "crm", "vpn", "fileserver"
]
business_texts = [
    "Quarterly report reviewed.",
    "Accessed employee handbook.",
    "Updated project documentation.",
    "Checked meeting schedule.",
    "Downloaded team roster.",
    "Viewed company policy.",
    "Uploaded expense receipts.",
    "Edited client contact info.",
    "Logged system activity.",
    "Submitted timesheet."
]

def random_ssn():
    return f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"

def random_cc():
    return ''.join(str(random.randint(0,9)) for _ in range(16))

def random_timestamp():
    start = datetime.datetime.now() - datetime.timedelta(days=30)
    random_seconds = random.randint(0, 30*24*60*60)
    return (start + datetime.timedelta(seconds=random_seconds)).strftime("%Y-%m-%d %H:%M:%S")

rows = []
for i in range(500):
    row = {
        "timestamp": random_timestamp(),
        "employee_id": f"E{random.randint(1000,9999)}",
        "department": random.choice(departments),
        "action": random.choice(actions),
        "resource_accessed": random.choice(resources),
        "data_payload": random.choice(business_texts)
    }
    rows.append(row)

# Insert SSNs and CCs
ssn_indices = set(random.sample(range(500), 25))
cc_indices = set(random.sample([i for i in range(500) if i not in ssn_indices], 25))

for idx in ssn_indices:
    rows[idx]["data_payload"] = f"SSN: {random_ssn()}"

for idx in cc_indices:
    cc = random_cc()
    formatted_cc = f"{cc[:4]}-{cc[4:8]}-{cc[8:12]}-{cc[12:]}"
    rows[idx]["data_payload"] = f"Credit Card: {formatted_cc}"

with open("enterprise_access_logs.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "timestamp", "employee_id", "department", "action", "resource_accessed", "data_payload"
    ])
    writer.writeheader()
    writer.writerows(rows)

print("enterprise_access_logs.csv successfully created with 500 rows.")