# Read in Excel file, abundance_table sheet
import pandas as pd

# Read the Excel file
df_abundance = pd.read_excel("Taxonomy_list_fermented_food_periodic_table.xlsx", sheet_name="abundance_table")

# Save the DataFrame to a CSV file
df_abundance.to_csv("abundance_table.csv", index=False)

# Read in Excel file, genera sheet
df_genera = pd.read_excel("Taxonomy_list_fermented_food_periodic_table.xlsx", sheet_name="taxonomy_table")

# Save the DataFrame to a CSV file
df_genera.to_csv("taxonomy_table.csv", index=False)
