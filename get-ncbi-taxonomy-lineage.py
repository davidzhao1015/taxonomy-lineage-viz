from Bio import Entrez # Ensure Biopython is installed
import pandas as pd



#--- Define a function to get taxonomy lineage for a given genus ---

def get_taxonomy_lineage(genus):
    """Fetches the taxonomy lineage at genus level from the NCBI taxonomy database.

    Args:
        genus (str): The genus name to search for in the NCBI taxonomy database.

    Returns:
        list: A list containing the lineage of the genus, or None if not found.
    """
    Entrez.email = "davidzhao1015@gmail.com" # Replace with your email address

    handle = Entrez.esearch(db="taxonomy", term=f"{genus}[Genus]") # Search for the genus in the NCBI taxonomy database
    record = Entrez.read(handle) # Read the search results
    handle.close() # Close the handle to free resources

    if not record["IdList"]:
        print(f"No taxonomy ID found for genus: {genus}") # If no ID is found, print a message
        return None

    taxid = record["IdList"][0] # Get the first taxonomy ID from the search results
    print(f"Taxonomy ID for {genus}: {taxid}") # Print the taxonomy ID

    handle = Entrez.efetch(db="taxonomy", id=taxid, retmode="xml") # Fetch the taxonomy record using the ID
    records = Entrez.read(handle) # Read the fetched record
    handle.close() # Close the handle to free resources

    lineage = records[0]["Lineage"] # Extract the lineage from the record, including domain, kingdom (or clade), phylum, class, order, and family
    print(f"Lineage for {genus}: {lineage}") # Print the lineage
    if not lineage == None:
        lineage_list = lineage.split("; ") # Split the lineage into a list
    
    return lineage_list


# Test case 
get_taxonomy_lineage("Lactobacillus")



#=== Define a list of target genera: Fermenting bacteria ===
genera = ['Acetobacter', 'Gluconacetobacter', 'Lentibacillus', 'Brevibacterium', 'Erwinia', 'Enterobacter', 'Pantoea', 
          'Kosakonia', 'Lactobacillus', 'Companilactobacillus', 'Schleiferilactobacillus', 'Ligilactobacillus', 
          'Lactiplantibacillus', 'Loigolactobacillus', 'Paucilactobacillus', 'Limosilactobacillus', 'Fructilactobacillus', 
          'Acetilactobacillus', 'Secundilactobacillus', 'Lentilactobacillus', 'Carnobacterium', 'Weissella', 'Oenococcus', 
          'Enterococcus', 'Tetragenococcus', 'Streptococcus', 'Lactococcus', 'Pediococcus', 'Periweissella', 'Leuconostoc', 
          'Marinilactobacillus', 'Alkalibacterium', 'Eggerthella', 'Propionibacterium', 'Staphylococcus', 'Kocuria']

len(genera) # Count the number of genera in the list




#--- Loop through each genus and get the taxonomy lineage ---

# Initialize an empty DataFrame to store all lineages
df_all_lineages = pd.DataFrame()


for genus in genera:
    lineage = get_taxonomy_lineage(genus)
    print(f"Processing genus: {genus}")
    # Create a DataFrame for the current genus
    if lineage is None:
        continue
    if lineage[1] == "Bacteria":
        df_genus_lineage = pd.DataFrame([lineage[1:]])
        df_genus_lineage.columns = ['Domain', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family']
        df_genus_lineage['Genus'] = genus
        
        # Append to the main DataFrame
        df_all_lineages = pd.concat([df_all_lineages, df_genus_lineage], ignore_index=True)

genus_successful = df_all_lineages["Genus"].to_list() # Get the list of successful genus entries
print(f"{len(genus_successful)} out of {len(genera)} genera was successful retrieved.") # Print the number of successful genus entries



# Save the DataFrame to a CSV file
df_all_lineages.to_csv("taxonomy_lineage.csv", index=False)
