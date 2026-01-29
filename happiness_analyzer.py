"""
World Happiness Report Data Analyzer
A comprehensive NumPy-based data analysis tool for exploring happiness data across countries.
"""

import numpy as np
import csv
from typing import Dict, List, Tuple, Optional


class HappinessAnalyzer:
    """Analyze World Happiness Report data using NumPy."""
    
    def __init__(self, csv_file: str):
        """
        Initialize the analyzer with data from CSV file.
        
        Args:
            csv_file: Path to the CSV file containing happiness data
        """
        self.csv_file = csv_file
        self.data: Optional[np.ndarray] = None
        self.headers: List[str] = []
        self.country_names: List[str] = []
        self.regional_indicators: List[str] = []
        self.column_map: Dict[str, int] = {}
        
        self.load_data()
    
    def load_data(self) -> None:
        """Load data from CSV file into NumPy arrays."""
        with open(self.csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.headers = next(reader)
            
            # Create column mapping
            for i, header in enumerate(self.headers):
                self.column_map[header] = i
            
            # Read all data
            rows = []
            for row in reader:
                if row and len(row) > 2:  # Skip empty rows
                    self.country_names.append(row[0])
                    self.regional_indicators.append(row[1])
                    # Extract numeric values (columns 2 onwards)
                    numeric_row = []
                    for val in row[2:]:
                        try:
                            numeric_row.append(float(val))
                        except ValueError:
                            numeric_row.append(np.nan)
                    rows.append(numeric_row)
            
            self.data = np.array(rows)
        
        print(f"Loaded data: {len(self.country_names)} countries, {self.data.shape[1]} features")
    
    def get_column_index(self, column_name: str) -> int:
        """Get the index of a column by name (adjusted for numeric data only)."""
        # Adjust index since we skip first 2 columns (country name, regional indicator)
        return self.column_map[column_name] - 2
    
    def get_basic_statistics(self, column_name: str) -> Dict[str, float]:
        """
        Calculate basic statistics for a given column.
        
        Args:
            column_name: Name of the column to analyze
            
        Returns:
            Dictionary containing mean, median, std, min, max
        """
        col_idx = self.get_column_index(column_name)
        column_data = self.data[:, col_idx]
        
        # Remove NaN values
        clean_data = column_data[~np.isnan(column_data)]
        
        return {
            'mean': np.mean(clean_data),
            'median': np.median(clean_data),
            'std': np.std(clean_data),
            'min': np.min(clean_data),
            'max': np.max(clean_data),
            'count': len(clean_data)
        }
    
    def get_top_countries(self, column_name: str, n: int = 10) -> List[Tuple[str, float]]:
        """
        Get top N countries by a specific metric.
        
        Args:
            column_name: Name of the column to rank by
            n: Number of top countries to return
            
        Returns:
            List of tuples (country_name, value)
        """
        col_idx = self.get_column_index(column_name)
        values = self.data[:, col_idx]
        
        # Get indices of top N values (excluding NaN)
        valid_indices = ~np.isnan(values)
        valid_values = values[valid_indices]
        valid_countries = np.array(self.country_names)[valid_indices]
        
        # Sort and get top N
        sorted_indices = np.argsort(valid_values)[::-1][:n]
        
        return [(valid_countries[i], valid_values[i]) for i in sorted_indices]
    
    def get_bottom_countries(self, column_name: str, n: int = 10) -> List[Tuple[str, float]]:
        """
        Get bottom N countries by a specific metric.
        
        Args:
            column_name: Name of the column to rank by
            n: Number of bottom countries to return
            
        Returns:
            List of tuples (country_name, value)
        """
        col_idx = self.get_column_index(column_name)
        values = self.data[:, col_idx]
        
        # Get indices of bottom N values (excluding NaN)
        valid_indices = ~np.isnan(values)
        valid_values = values[valid_indices]
        valid_countries = np.array(self.country_names)[valid_indices]
        
        # Sort and get bottom N
        sorted_indices = np.argsort(valid_values)[:n]
        
        return [(valid_countries[i], valid_values[i]) for i in sorted_indices]
    
    def filter_by_region(self, region: str) -> Tuple[List[str], np.ndarray]:
        """
        Filter data by region.
        
        Args:
            region: Regional indicator to filter by
            
        Returns:
            Tuple of (country_names, data_array)
        """
        indices = [i for i, r in enumerate(self.regional_indicators) if r == region]
        countries = [self.country_names[i] for i in indices]
        data = self.data[indices, :]
        
        return countries, data
    
    def get_correlation_matrix(self, column_names: List[str]) -> np.ndarray:
        """
        Calculate correlation matrix for specified columns.
        
        Args:
            column_names: List of column names to include
            
        Returns:
            Correlation matrix
        """
        indices = [self.get_column_index(name) for name in column_names]
        subset_data = self.data[:, indices]
        
        # Remove rows with any NaN values
        clean_data = subset_data[~np.any(np.isnan(subset_data), axis=1)]
        
        return np.corrcoef(clean_data.T)
    
    def compare_regions(self, column_name: str) -> Dict[str, Dict[str, float]]:
        """
        Compare statistics across different regions.
        
        Args:
            column_name: Name of the column to compare
            
        Returns:
            Dictionary mapping region names to their statistics
        """
        col_idx = self.get_column_index(column_name)
        unique_regions = list(set(self.regional_indicators))
        
        results = {}
        for region in unique_regions:
            _, region_data = self.filter_by_region(region)
            region_values = region_data[:, col_idx]
            clean_values = region_values[~np.isnan(region_values)]
            
            if len(clean_values) > 0:
                results[region] = {
                    'mean': np.mean(clean_values),
                    'median': np.median(clean_values),
                    'std': np.std(clean_values),
                    'count': len(clean_values)
                }
        
        return results
    
    def find_outliers(self, column_name: str, threshold: float = 2.0) -> List[Tuple[str, float, float]]:
        """
        Find outliers using z-score method.
        
        Args:
            column_name: Name of the column to analyze
            threshold: Z-score threshold for outlier detection
            
        Returns:
            List of tuples (country_name, value, z_score)
        """
        col_idx = self.get_column_index(column_name)
        values = self.data[:, col_idx]
        
        # Calculate z-scores
        mean = np.nanmean(values)
        std = np.nanstd(values)
        z_scores = np.abs((values - mean) / std)
        
        # Find outliers
        outlier_indices = np.where(z_scores > threshold)[0]
        
        return [(self.country_names[i], values[i], z_scores[i]) 
                for i in outlier_indices if not np.isnan(values[i])]
    
    def get_country_data(self, country_name: str) -> Dict[str, float]:
        """
        Get all data for a specific country.
        
        Args:
            country_name: Name of the country
            
        Returns:
            Dictionary mapping column names to values
        """
        try:
            idx = self.country_names.index(country_name)
            result = {
                'Country name': country_name,
                'Regional indicator': self.regional_indicators[idx]
            }
            
            # Add numeric data
            for header in self.headers[2:]:
                col_idx = self.get_column_index(header)
                result[header] = self.data[idx, col_idx]
            
            return result
        except ValueError:
            return {}
    
    def calculate_percentile_rank(self, country_name: str, column_name: str) -> float:
        """
        Calculate the percentile rank of a country for a specific metric.
        
        Args:
            country_name: Name of the country
            column_name: Name of the column
            
        Returns:
            Percentile rank (0-100)
        """
        col_idx = self.get_column_index(column_name)
        country_idx = self.country_names.index(country_name)
        country_value = self.data[country_idx, col_idx]
        
        all_values = self.data[:, col_idx]
        clean_values = all_values[~np.isnan(all_values)]
        
        percentile = (np.sum(clean_values < country_value) / len(clean_values)) * 100
        return percentile


def main():
    """Main function to demonstrate the analyzer."""
    # Initialize analyzer
    analyzer = HappinessAnalyzer('WHR20_DataForFigure2.1.csv')
    
    print("\n" + "="*80)
    print("WORLD HAPPINESS REPORT DATA ANALYSIS")
    print("="*80)
    
    # 1. Basic Statistics for Ladder Score
    print("\n1. BASIC STATISTICS FOR LADDER SCORE (Happiness Score)")
    print("-" * 60)
    stats = analyzer.get_basic_statistics('Ladder score')
    for key, value in stats.items():
        print(f"  {key.capitalize()}: {value:.4f}")
    
    # 2. Top 10 Happiest Countries
    print("\n2. TOP 10 HAPPIEST COUNTRIES")
    print("-" * 60)
    top_countries = analyzer.get_top_countries('Ladder score', 10)
    for i, (country, score) in enumerate(top_countries, 1):
        print(f"  {i:2d}. {country:30s} {score:.3f}")
    
    # 3. Bottom 10 Countries
    print("\n3. BOTTOM 10 COUNTRIES BY HAPPINESS SCORE")
    print("-" * 60)
    bottom_countries = analyzer.get_bottom_countries('Ladder score', 10)
    for i, (country, score) in enumerate(bottom_countries, 1):
        print(f"  {i:2d}. {country:30s} {score:.3f}")
    
    # 4. Regional Comparison
    print("\n4. HAPPINESS SCORE BY REGION")
    print("-" * 60)
    regional_stats = analyzer.compare_regions('Ladder score')
    sorted_regions = sorted(regional_stats.items(), 
                           key=lambda x: x[1]['mean'], reverse=True)
    for region, stats in sorted_regions:
        print(f"  {region:35s} Mean: {stats['mean']:.3f} (±{stats['std']:.3f})")
    
    # 5. Correlation Analysis
    print("\n5. CORRELATION ANALYSIS")
    print("-" * 60)
    factors = [
        'Logged GDP per capita',
        'Social support',
        'Healthy life expectancy',
        'Freedom to make life choices',
        'Generosity',
        'Perceptions of corruption'
    ]
    
    print("  Analyzing correlations with Ladder score...")
    for factor in factors:
        col_idx_ladder = analyzer.get_column_index('Ladder score')
        col_idx_factor = analyzer.get_column_index(factor)
        
        # Get clean data
        ladder_data = analyzer.data[:, col_idx_ladder]
        factor_data = analyzer.data[:, col_idx_factor]
        valid = ~(np.isnan(ladder_data) | np.isnan(factor_data))
        
        if np.sum(valid) > 0:
            corr = np.corrcoef(ladder_data[valid], factor_data[valid])[0, 1]
            print(f"  {factor:35s} r = {corr:.3f}")
    
    # 6. Country Lookup Example
    print("\n6. DETAILED DATA FOR INDIA")
    print("-" * 60)
    india_data = analyzer.get_country_data('India')
    if india_data:
        print(f"  Country: {india_data['Country name']}")
        print(f"  Region: {india_data['Regional indicator']}")
        print(f"  Ladder score: {india_data['Ladder score']:.3f}")
        print(f"  GDP per capita: {india_data['Logged GDP per capita']:.3f}")
        print(f"  Social support: {india_data['Social support']:.3f}")
        print(f"  Life expectancy: {india_data['Healthy life expectancy']:.3f}")
        
        percentile = analyzer.calculate_percentile_rank('India', 'Ladder score')
        print(f"  Percentile rank: {percentile:.1f}%")
    
    # 7. Outlier Detection
    print("\n7. OUTLIER DETECTION FOR GDP PER CAPITA")
    print("-" * 60)
    outliers = analyzer.find_outliers('Logged GDP per capita', threshold=2.0)
    if outliers:
        print(f"  Found {len(outliers)} outliers:")
        for country, value, z_score in outliers[:5]:  # Show top 5
            print(f"  {country:30s} Value: {value:.3f}, Z-score: {z_score:.2f}")
    
    print("\n" + "="*80)


if __name__ == "__main__":
    main()
