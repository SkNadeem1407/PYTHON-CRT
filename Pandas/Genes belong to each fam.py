import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}
df = pd.DataFrame(data)
family_counts = df["Family"].value_counts()
plt.figure(figsize=(8, 5))
family_counts.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title("Number of Genes per Family")
plt.xlabel("Family")
plt.ylabel("Gene Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
