import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define paths
file_path = '../data/2025_trees_steglitz.csv'
save_path = '../results/analysis_age_dist.png'

print("Loading data...")
try:
    df = pd.read_csv(file_path, sep=';')
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

# Fix: Convert 'pflanzjahr' to integer to avoid "2020.5" issues
print("Processing data...")
df = df.dropna(subset=['pflanzjahr'])
df['pflanzjahr'] = df['pflanzjahr'].astype(int)

# Plot
print("Generating plot...")
plt.figure(figsize=(10, 6))

# Fix: Use discrete histogram/countplot, NO KDE
sns.countplot(x=df['pflanzjahr'], color='green')

plt.title('Tree Plantings per Year (Count)', fontsize=16)
plt.xlabel('Year Planted', fontsize=12)
plt.ylabel('Number of Trees', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Save
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
