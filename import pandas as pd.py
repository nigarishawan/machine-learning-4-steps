import pandas as pd
# Step 1: Data Collection
data = {
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'William'],
    'Marks': [85, 90, 78, 92, 88],
    'CGPA': [8.5, 9.0, 7.8, 9.2, 8.8],
    'Percentage': [85.0, 90.0, 78.0, 92.0, 88.0]
}

students_df = pd.DataFrame(data)

# Step 2: Data Preprocessing (No preprocessing required in this example)

# Step 3: Exploratory Data Analysis
# Summary statistics
print("Summary Statistics:")
print(students_df.describe())

# Data Visualization (example: histogram of Marks)
import matplotlib.pyplot as plt
plt.hist(students_df['Marks'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()


