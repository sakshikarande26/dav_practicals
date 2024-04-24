import matplotlib.pyplot as plt

# Data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
values = [10, 20, 15, 25, 30]

# Create bar plot
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show plot
plt.show()
