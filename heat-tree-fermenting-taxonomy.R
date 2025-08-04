library(metacoder)

# Load the taxonomy data in csv format
taxonomy_data <- read.csv("taxonomy_table.csv")

# Inspect first few rows of the data
head(taxonomy_data)


# --- Parse taxonomy data
tax_data <- parse_tax_data(
    taxonomy_data, 
    class_cols = 2:7,
    named_by_rank = TRUE
)

class(tax_data)

# --- Draw heat tree
heat_tree(
    tax_data,
    node_label = taxon_names,
    node_color = n_obs,
    node_color_axis_label = "Number of Fermented Foods",
    node_size_range = c(0.03, 0.04),
    node_label_size_range = c(0.02, 0.03),
    node_size_interval = c(10, 100),
    layout = "davidson-harel")


