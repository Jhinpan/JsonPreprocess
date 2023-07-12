import os
import json
import sqlite3
from collections import defaultdict

# Load the JSON data
with open('model_info_VR.json', 'r') as openfile:
    json_data = json.load(openfile)

# Access the list of entries
data = json_data['data']

# Group the data by "superCategory"
grouped_data = defaultdict(list)
for entry in data:
    grouped_data[entry['superCategory']].append(entry)

# Create a directory for the output files
os.makedirs('output', exist_ok=True)

# Write each group to a separate JSON file
for superCategory, entries in grouped_data.items():
    file_name = superCategory.replace('/', '_') + '.json'
    with open(os.path.join('output', file_name), 'w') as f:
        json.dump(entries, f, indent=4)

# Create a new SQLite database and establish a connection to it
conn = sqlite3.connect('model_info.db')

# Create a cursor object
c = conn.cursor()

# Create a new table
c.execute('''
    CREATE TABLE model_info (
        model_id text,
        superCategory text,
        category text,
        style text,
        theme text,
        material text
    )
''')

# Insert the entries into the table
for entry in data:
    c.execute('''
        INSERT INTO model_info VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        entry['model_id'],
        entry['superCategory'],
        entry['category'],
        entry['style'],
        entry['theme'],
        entry['material']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
