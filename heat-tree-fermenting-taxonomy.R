library(metacoder)
library(ggplot2)
library(tibble)

# Load the taxonomy data in csv format
taxonomy_data <- read.csv("taxonomy_table.csv")

# Inspect first few rows of the data
head(taxonomy_data)

# Count unique Species_label
# length(unique(taxonomy_data$Species_label)) # 36 spp.





#--- Integrate count data to taxonomy data ---------------------------
# --- Preprocess abundance data and taxonomy data ---
count_data <- read.csv("abundance_table.csv", row.names = 1)
head(count_data)
count_data2 <- count_data[1,]
head(count_data2)

# Transpose count_data2
count_data3 <- t(count_data2)
head(count_data3)

# Make row name as a column, Species_label
count_data3 <- as.data.frame(count_data3)
count_data3$Species_label <- rownames(count_data3)
rownames(count_data3) <- NULL
head(count_data3)

# length(unique(count_data3$Species_label)) # 36 spp.


# Normalize freq data into relative proportions
count_data3$normalized_prop <- count_data3$"Fermented foods1" / 115

range(count_data3$normalized_prop)

# Rename Fermented foods1 to count
colnames(count_data3)[1] <- "fermented_food_freq"

# Merge taxonomy data into count data by the column Species_label
count_data4 <- merge(count_data3, taxonomy_data, by = "Species_label", all.x = TRUE)
print(count_data4)

# Show column names
# colnames(count_data4)



# --- Parse taxonomy data ---
obj <- parse_tax_data(count_data4, class_cols = 4:9, named_by_rank = TRUE)

class(obj)
print(obj)


# Get per-taxon information
obj$data$tax_abund <- calc_taxon_abund(obj, "tax_data", cols = "normalized_prop")
print(obj)


# --- Draw heat tree ---
set.seed(123)

ht_plot_abund <- heat_tree(obj,
    node_label = obj$taxon_names(),
    node_size = obj$data$tax_abund$normalized_prop,
    node_color = obj$data$tax_abund$normalized_prop,
    node_color_range = c("yellow", "green", "cyan"),
    initial_layout = "reingold-tilford",
    layout = "davidson-harel",
    node_color_axis_label = "Number of \nObservations"
)

ht_plot_abund
ggsave("heat_tree_plot_abund.pdf", plot = ht_plot_abund, width = 12, height = 8)


# --- End of the session -----------------------------------------------




# --- Alternative: Parse only taxonomy data for plotting ---------------

tax_data <- parse_tax_data(
    taxonomy_data, 
    class_cols = 2:7,
    named_by_rank = TRUE
)

class(tax_data)
print(tax_data)

# --- Simple heat tree ---
set.seed(123)

ht_plot_simple <- heat_tree(
    tax_data,
    node_label = taxon_names,
    node_color = n_obs,
    node_color_range = c("yellow", "green", "cyan"),
    initial_layout = "reingold-tilford",
    layout = "davidson-harel",
    node_color_axis_label = "Number of \nObservations"
)

ht_plot_simple

# Save the plot
ggsave("heat_tree_plot_taxonomy_only.pdf", plot = ht_plot_simple, width = 12, height = 8)

# --- Ending ---