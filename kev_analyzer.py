import pandas as pd
import matplotlib.pyplot as plt

# Load the CISA KEV catalog
df = pd.read_csv("known_exploited_vulnerabilities.csv")

# Group by vendor, count vulnerabilities, keep the top 5
top5 = (
    df.groupby("vendorProject")
      .size()
      .sort_values(ascending=False)
      .head(5)
)
print(top5)

# Bar chart
top5.plot(kind="bar")
plt.title("Top 5 Vendors in CISA KEV Catalog")
plt.xlabel("Vendor")
plt.ylabel("Number of KEV Entries")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top5_vendors.png")
plt.show()
