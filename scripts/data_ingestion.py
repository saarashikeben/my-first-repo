# Data ingestion script
import requests
import json
import os

# URL for Helsinki Open Data API to fetch HUS procurements data
url = "https://hri.fi/data/dataset/ea56e1a3-5c1c-4a68-b7aa-4b4e14c1d43f/resource/a1c1e690-1205-4ae7-8f67-1488c3edc57f/download/hus_hankinnat.json"

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # Save the data to a JSON file
    with open("data/hus_procurements.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data ingestion complete. Data saved to data/hus_procurements.json.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
