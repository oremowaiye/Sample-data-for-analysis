import pandas as pd 
import matplotlib.pyplot as plt

# Load the data from CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Display basic information about the dataset
print("Basic information about the dataset:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())


numeric_column = 'duration'  
print("\nBasic statistics for '{}' column:".format(numeric_column))
print("Mean:", df[numeric_column].mean())
print("Median:", df[numeric_column].median())
print("Standard Deviation:", df[numeric_column].std())

# Generate a histogram to visualize the distribution of a numerical column
plt.figure(figsize=(8, 6))
plt.hist(df[numeric_column], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of '{}' column".format(numeric_column))
plt.xlabel(numeric_column)
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Generate a bar chart to visualize the frequency of categorical values
categorical_column = 'rating'  
plt.figure(figsize=(8, 6))
df[categorical_column].value_counts().plot(kind='bar', color='lightgreen')
plt.title("Bar chart of '{}' column".format(categorical_column))
plt.xlabel(categorical_column)
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

