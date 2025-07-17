from Bio import Entrez # Ensure Biopython is installed
import pandas as pd

#=== Define a function to get taxonomy lineage for a given genus ===
def get_taxonomy_lineage(genus):
    Entrez.email = "davidzhao1015@gmail.com"

    handle = Entrez.esearch(db="taxonomy", term=f"{genus}[Genus]")
    record = Entrez.read(handle)

    if not record["IdList"]:
        print(f"No taxonomy ID found for genus: {genus}")
        return None

    taxid = record["IdList"][0]

    handle = Entrez.efetch(db="taxonomy", id=taxid, retmode="xml")
    records = Entrez.read(handle)

    lineage = records[0]["Lineage"]
    if not lineage == None:
        lineage_list = lineage.split("; ")
    
    return lineage_list




#=== Define a list of target genera ===
genera = [
    "Acetobacter",
    "Gluconacetobacter",
    "Bacillus",
    "Lentibacillus",
    "Brevibacterium",
    "Erwinia",
    "Enterobacter",
    "Pantoea",
    "Kosakonia",
    "Lactobacillus",
    "Companilactobacillus",
    "Schleiferilactobacillus",
    "Ligilactobacillus",
    "Lactiplantibacillus",
    "Loigolactobacillus",
    "Paucilactobacillus",
    "Limosilactobacillus",
    "Fructilactobacillus",
    "Acetilactobacillus",
    "Lactilactobacillus",
    "Secundilactobacillus",
    "Lentilactobacillus",
    "Carnobacterium",
    "Weissella",
    "Oenococcus",
    "Enterococcus",
    "Tetragenococcus",
    "Streptococcus",
    "Lactococcus",
    "Pediococcus",
    "Periweissella",
    "Leuconostoc",
    "Marinilactobacillus",
    "Aspergillus",
    "Geotrichum",
    "Monascus",
    "Penicillium",
    "Rhizopus",
    "Alkalibacterium",
    "Eggerthella",
    "Propionibacterium",
    "Staphylococcus",
    "Kocuria",
    "Blastobotrys",
    "Brettanomyces",
    "Debaryomyces",
    "Issatchenkia",
    "Kluyveromyces",
    "Kazachstania",
    "Saccharomyces",
    "Torulaspora",
    "Zygosaccharomyces"
]


# Test case 
get_taxonomy_lineage("Lactobacillus")



#=== Loop through each genus and get the taxonomy lineage ===

# Initialize an empty DataFrame to store all lineages
df_all_lineages = pd.DataFrame()


for genus in genera:
    lineage = get_taxonomy_lineage(genus)
    print(f"Processing genus: {genus}")
    # Create a DataFrame for the current genus
    if lineage is None:
        continue
    if len(lineage) == 7:
        df_genus_lineage = pd.DataFrame([lineage[1:]])
        df_genus_lineage.columns = ['Domain', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family']
        df_genus_lineage['Genus'] = genus
        # print(df_genus_lineage.shape)
        # Append to the main DataFrame
        df_all_lineages = pd.concat([df_all_lineages, df_genus_lineage], ignore_index=True)

# Save the DataFrame to a CSV file
df_all_lineages.to_csv("taxonomy_lineage.csv", index=False)
