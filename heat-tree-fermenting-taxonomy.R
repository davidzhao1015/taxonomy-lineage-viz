library(metacoder)
library(ggplot2)
library(tibble)

# Load the taxonomy data in csv format
taxonomy_data <- read.csv("taxonomy_table.csv")

# Inspect first few rows of the data
head(taxonomy_data)




#--- Integrate count data to taxonomy data ---------------------------
# Load fermented foods count data
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

# Rename Fermented foods1 to count
colnames(count_data3)[1] <- "count"

# Merge taxonomy data into count data by the column Species_label
count_data4 <- merge(count_data3, taxonomy_data, by = "Species_label", all.x = TRUE)
print(count_data4)

# --- Parse taxonomy data
tax_data <- parse_tax_data(
    count_data4, 
    class_cols = 3:8,
    named_by_rank = TRUE
)

class(tax_data)
print(tax_data)

# tax_data <- calc_taxon_abund(
#   tax_data,
#   data = "tax_data",    # your abundance data table name
#   cols = "count"        # the column to roll up
# )

# print(tax_data)

# --- End of the session -----------------------------------------------



tax_data <- parse_tax_data(
    taxonomy_data, 
    class_cols = 2:7,
    named_by_rank = TRUE
)

class(tax_data)
print(tax_data)

# --- Draw heat tree
# ht_plot <- heat_tree(
#     tax_data,
#     node_label = taxon_names,
#     node_color = n_obs,
#     node_color_axis_label = "Number of \nObservations",
#     node_color_digits = 0,
#     node_size_range = c(0.01, 0.015),
#     node_color_range = c("yellow", "green", "cyan"),  # better perceptibility
#     node_label_size_range = c(0.01, 0.03),
#     node_size_interval = c(1, 50),
#     background_color = "white",
#     overlap_avoidance = 5,
#     initial_layout = "reingold-tilford",
#     layout = "davidson-harel",
#     repel_labels = TRUE,
#     title_size = 0.8
# )


print(tax_data$data$tax_data$count)

# --- Simple heat tree ---
set.seed(123)
ht_plot_simple <- heat_tree(
    tax_data,
    node_label = taxon_names,
    node_color = tax_data$data$tax_data$count,
    # node_size = tax_data$data$tax_data$count,
    node_color_range = c("yellow", "green", "cyan"),
    initial_layout = "reingold-tilford",
    layout = "davidson-harel",
    node_color_axis_label = "Number of \nObservations"
)

ht_plot_simple <- heat_tree(
    tax_data,
    node_label = taxon_names,
    node_color = n_obs,
    # node_size = tax_data$data$tax_data$count,
    node_color_range = c("yellow", "green", "cyan"),
    initial_layout = "reingold-tilford",
    layout = "davidson-harel",
    node_color_axis_label = "Number of \nObservations"
)

ht_plot_simple

# Save the plot
# Finding: the legend's position is not adjustable; and tile size of legend is hard to manage.
ggsave("heat_tree_plot_count.pdf", plot = ht_plot_simple, width = 12, height = 8)




#--- Example data ---
# load("filtered_data.RData")
