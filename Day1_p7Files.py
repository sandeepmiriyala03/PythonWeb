import json
from pathlib import Path

# File path
file_path = Path("employee.json")

# Read file as text
json_text = file_path.read_text()

# Convert JSON text -> Python Dictionary
employee = json.loads(json_text)

print("Before Update")
print(employee)

# Modify data
employee["salary"] += 5000

# Convert Dictionary -> JSON Text
updated_json = json.dumps(employee, indent=4)

# Write back to file
file_path.write_text(updated_json)

print("\nAfter Update")
print(employee)