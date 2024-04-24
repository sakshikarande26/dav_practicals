# Load the dataset
rainfall_data <- read.csv("rainfall.csv")

# Calculate average rainfall per month
avg_rainfall <- aggregate(rainfall ~ Month, data = rainfall_data, FUN = mean)

# Sort the data by month
avg_rainfall <- avg_rainfall[order(match(avg_rainfall$Month, month.name)), ]

# Create a bar plot
barplot(avg_rainfall$Rainfall, 
        names.arg = avg_rainfall$Month,
        main = "Average Rainfall per Month",
        xlab = "Month",
        ylab = "Average Rainfall (mm)",
        col = "lightblue",
        ylim = c(0, max(avg_rainfall$rainfall) * 1.1))

# Add a legend
legend("topright", 
       legend = c("Average Rainfall"), 
       fill = "lightblue")
