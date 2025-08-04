import requests
import pandas as pd
from io import StringIO

# URL of the CSV file
url_abundance = 'https://wegan.ca/resources/data/aravo_taxon.csv'

# Download the content
response = requests.get(url_abundance)
response.raise_for_status()  # Raises an error for bad status codes

# Read CSV into a DataFrame
df_abundance = pd.read_csv(StringIO(response.text))

# Optional: Save to local file
df_abundance.to_csv('tax_data_example.csv', index=False)