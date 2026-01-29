# Quick Start Guide - NumPy Data Explorer

## Installation Steps

### 1. Install NumPy
Before running the project, you need to install NumPy:

```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install numpy
```

### 2. Running the Python Script

```bash
python happiness_analyzer.py
```

This will display a comprehensive analysis report with:
- Global happiness statistics
- Top 10 happiest countries
- Bottom 10 countries
- Regional comparisons
- Correlation analysis
- Country-specific details (India example)
- Outlier detection

### 3. Running the Jupyter Notebook

First, install Jupyter if you haven't already:
```bash
pip install jupyter
```

Then launch the notebook:
```bash
jupyter notebook happiness_explorer.ipynb
```

## What's Included

| File | Description |
|------|-------------|
| `happiness_analyzer.py` | Complete Python script with HappinessAnalyzer class |
| `happiness_explorer.ipynb` | Interactive Jupyter notebook (13 analysis sections) |
| `WHR20_DataForFigure2.1.csv` | World Happiness Report 2020 dataset |
| `README.md` | Full documentation |
| `QUICKSTART.md` | This file |
| `requirements.txt` | Python dependencies |

## Quick Examples

### Example 1: Get Basic Statistics
```python
from happiness_analyzer import HappinessAnalyzer

analyzer = HappinessAnalyzer('WHR20_DataForFigure2.1.csv')
stats = analyzer.get_basic_statistics('Ladder score')
print(stats)
```

### Example 2: Get Top 10 Countries
```python
top10 = analyzer.get_top_countries('Ladder score', n=10)
for country, score in top10:
    print(f"{country}: {score:.3f}")
```

### Example 3: Compare Regions
```python
regional = analyzer.compare_regions('Ladder score')
for region, stats in regional.items():
    print(f"{region}: {stats['mean']:.2f}")
```

### Example 4: Get Country Data
```python
india = analyzer.get_country_data('India')
print(india)
```

### Example 5: Find Outliers
```python
outliers = analyzer.find_outliers('Logged GDP per capita', threshold=2.0)
for country, value, zscore in outliers:
    print(f"{country}: {value:.2f} (z={zscore:.2f})")
```

## Class Methods Quick Reference

```python
# Statistical Analysis
get_basic_statistics(column_name)        # Mean, median, std, min, max
get_top_countries(column_name, n=10)     # Top N countries
get_bottom_countries(column_name, n=10)  # Bottom N countries

# Regional Analysis
filter_by_region(region)                 # Filter data by region
compare_regions(column_name)             # Compare across regions

# Correlation
get_correlation_matrix(column_names)     # Correlation matrix

# Country Analysis
get_country_data(country_name)           # All data for a country
calculate_percentile_rank(country, col)  # Percentile ranking

# Outliers
find_outliers(column_name, threshold)    # Z-score based outlier detection
```

## Dataset Columns

Key columns in the dataset:
- `Ladder score` - Happiness score (0-10)
- `Logged GDP per capita` - Economic indicator
- `Social support` - Social connections measure
- `Healthy life expectancy` - Health indicator
- `Freedom to make life choices` - Personal freedom
- `Generosity` - Charitable behavior
- `Perceptions of corruption` - Trust in institutions

## Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'numpy'`
**Solution:** Run `pip install numpy`

**Problem:** CSV file not found
**Solution:** Make sure `WHR20_DataForFigure2.1.csv` is in the same directory

**Problem:** Jupyter notebook won't open
**Solution:** Install with `pip install jupyter notebook`

## Next Steps

1. ✅ Install dependencies
2. ✅ Run the Python script to see the analysis
3. ✅ Open the Jupyter notebook for interactive exploration
4. ✅ Modify the code to explore your own questions
5. ✅ Check README.md for more detailed documentation
