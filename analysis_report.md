# Analysis Report: Berlin Steglitz-Zehlendorf Trees

## Overview
This report analyzes the `2025_trees_steglitz.csv` dataset.
**Important Note**: The dataset appears to consist exclusively of **recently planted trees** (younger than 6 years), likely representing a specific planting cohort or a subset of the full tree cadastre.

## Key Findings

### 1. A Young Forest
- **Average Age**: 3.6 years
- **Oldest Tree**: 5 years
- **Conclusion**: This dataset tracks recent urban greening efforts, not the historical tree stock.

### 2. Species Selection
The most common species planted in recent years are:
1.  **Tilia cordata 'Greenspire'** (Small-leaved Lime) - 92 trees
2.  **Prunus avium 'Plena'** (Double-flowered Wild Cherry) - 52 trees
3.  **Tilia tomentosa 'Brabant'** (Silver Lime) - 52 trees

There is a clear preference for **Limes (Tilia)** and **Cherries (Prunus)**, which are hardy urban trees.

### 3. Spatial Distribution
**Zehlendorf** is the "greenest" district in this dataset with **368** new trees, followed by other districts.

## Visualizations

### Species Diversity
![Top Species](results/analysis_top_species.png)

### Planting Years
![Age Distribution](results/analysis_age_dist.png)

### District Distribution
![District Distribution](results/analysis_district_dist.png)

## Recommendations
- **Diversification**: While Tilia is popular, increasing diversity could protect against specific pests.
- **Monitoring**: These young trees require watering and care. The dataset could be augmented with "health status" columns for future monitoring.
