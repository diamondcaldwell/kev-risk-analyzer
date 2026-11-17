# CISA KEV Risk Analyzer

Analyzes CISA's Known Exploited Vulnerabilities (KEV) catalog to find which
vendors have the most entries on the federal remediation list.

## Background
Federal agencies are required to remediate vulnerabilities listed in CISA's
KEV catalog by their due dates. This project uses Python to analyze that
public dataset and identify which vendors appear most often.

## Tech
Python, pandas, matplotlib

## How it works
1. Loads the KEV catalog CSV (downloaded from CISA on Nov 17, 2026).
2. Groups entries by vendor (`vendorProject`) and counts them.
3. Plots the top 5 vendors as a bar chart.

## Results

| Vendor    | KEV Entries |
|-----------|-------------|
| Microsoft | 391         |
| Cisco     | 103         |
| Apple     | 96          |
| Adobe     | 83          |
| Google    | 77          |
<img width="359" height="264" alt="Screenshot 2026-11-17 175323" src="https://github.com/user-attachments/assets/4794a363-60d4-4749-979a-0c3f74c3fc43" />


Microsoft has about 3.8 times as many KEV entries as the next vendor, Cisco.

## Limitations
- Counts reflect the catalog snapshot from Nov 17, 2026 and change as CISA
  adds entries.
- Vendor names are free text chosen by CISA and may be inconsistent.
- Entry count shows how often a vendor's products appear in the catalog. It
  does not measure how secure a vendor is, and vendors with larger product
  footprints naturally appear more often.

## How to run
```
pip install pandas matplotlib
python kev_analyzer.py
```
