# NumPy Data Explorer - World Happiness Report Analysis

A comprehensive data analysis project for exploring the World Happiness Report 2020 dataset using NumPy.

## 📊 Dataset

The project analyzes **WHR20_DataForFigure2.1.csv** which contains:
- **153 countries** with happiness scores and socioeconomic indicators
- **20 features** including:
  - Ladder score (happiness score)
  - GDP per capita
  - Social support
  - Healthy life expectancy
  - Freedom to make life choices
  - Generosity
  - Perceptions of corruption
  - Regional indicators

## 🚀 Features

### Python Script (`happiness_analyzer.py`)
A class-based implementation with the following capabilities:

#### Statistical Analysis
- Basic statistics (mean, median, std, min, max)
- Top/bottom country rankings
- Percentile calculations
- Outlier detection using z-scores

#### Regional Analysis
- Filter data by region
- Compare metrics across regions
- Regional statistics

#### Correlation Analysis
- Correlation matrix generation
- Factor correlation with happiness scores
- Multi-variate analysis

#### Data Querying
- Country-specific profiles
- Custom filtering
- Percentile rankings

### Jupyter Notebook (`happiness_explorer.ipynb`)
Interactive analysis with:
- Step-by-step data exploration
- Visual statistical summaries
- Regional comparisons
- Country profiling
- Similar country finder
- Custom query functions
- Data quality checks

## 📋 Requirements

```
Python 3.6+
NumPy
```

Install dependencies:
```bash
pip install numpy
```

For Jupyter notebook support:
```bash
pip install jupyter notebook
```

## 🎯 Usage

### Option 1: Run Python Script

```bash
python happiness_analyzer.py
```

This will generate a comprehensive report including:
1. Basic statistics for happiness scores
2. Top 10 happiest countries
3. Bottom 10 countries
4. Regional comparisons
5. Correlation analysis with key factors
6. Country-specific analysis (example: India)
7. Outlier detection

### Option 2: Interactive Jupyter Notebook

```bash
jupyter notebook happiness_explorer.ipynb
```

The notebook provides 13 sections:
1. Setup and Data Loading
2. Data Overview
3. Basic Statistical Analysis
4. Country Rankings
5. Regional Analysis
6. Factor Analysis
7. Correlation Analysis
8. Correlation Matrix
9. Country-Specific Analysis
10. Custom Analysis Functions
11. Advanced Queries
12. Data Quality Check
13. Summary and Insights


## 📊 Key Findings

Based on the 2020 World Happiness Report data:

### Top 5 Happiest Countries
1. **Finland** - 7.809
2. **Denmark** - 7.646
3. **Switzerland** - 7.560
4. **Iceland** - 7.504
5. **Norway** - 7.488

### Happiness by Region
- **Western Europe** - Highest average happiness
- **Sub-Saharan Africa** - Lowest average happiness
- **North America and ANZ** - Second highest

### Key Correlates of Happiness
Factors most strongly correlated with happiness:
1. **GDP per capita** - Strong positive correlation
2. **Social support** - Strong positive correlation
3. **Healthy life expectancy** - Strong positive correlation
4. **Freedom to make life choices** - Moderate positive correlation

## 🔧 Class Methods Reference

### `HappinessAnalyzer` Class

| Method | Description |
|--------|-------------|
| `load_data()` | Load data from CSV file |
| `get_basic_statistics(column_name)` | Get mean, median, std, min, max for a column |
| `get_top_countries(column_name, n)` | Get top N countries by metric |
| `get_bottom_countries(column_name, n)` | Get bottom N countries by metric |
| `filter_by_region(region)` | Filter data by regional indicator |
| `get_correlation_matrix(column_names)` | Calculate correlation matrix |
| `compare_regions(column_name)` | Compare metric across regions |
| `find_outliers(column_name, threshold)` | Find outliers using z-score |
| `get_country_data(country_name)` | Get all data for a country |
| `calculate_percentile_rank(country, column)` | Calculate percentile rank |

## 📂 Project Structure

```
NumPy Data Explorer/
├── WHR20_DataForFigure2.1.csv      # Dataset
├── happiness_analyzer.py            # Python script with analysis class
├── happiness_explorer.ipynb         # Interactive Jupyter notebook
├── README.md                        # This file
└── software_doc.md                  # (Empty - for additional documentation)
```

## 🎓 Learning Objectives

This project demonstrates:
- NumPy array manipulation and operations
- Statistical analysis with NumPy
- Data filtering and querying
- Correlation analysis
- Object-oriented programming in Python
- Working with CSV data
- Jupyter notebook development

## 📈 Extending the Project

Ideas for extending this project:
1. Add data visualization using matplotlib
2. Implement time-series analysis (if multi-year data available)
3. Add machine learning models for prediction
4. Create interactive dashboards with Plotly
5. Add geographical mapping
6. Implement clustering analysis
7. Add statistical hypothesis testing

## 🤝 Contributing

Feel free to extend this project with:
- Additional analysis methods
- Visualization features
- Documentation improvements
- Bug fixes

## 📄 License

This is an educational project for learning NumPy and data analysis.

## 📞 Support

For questions or issues, please refer to:
- NumPy documentation: https://numpy.org/doc/
- World Happiness Report: https://worldhappiness.report/

---

**Note**: Make sure the CSV file `WHR20_DataForFigure2.1.csv` is in the same directory as the Python script when running the analysis.
