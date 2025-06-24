"""
Data utility functions for the analysis project.
This module contains common functions for data loading, processing, and visualization.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import requests
import json
import os

def load_data_from_file(file_path, file_type='auto'):
    """
    Load data from various file formats.
    
    Parameters:
    -----------
    file_path : str
        Path to the data file
    file_type : str
        Type of file ('csv', 'excel', 'json', 'auto')
    
    Returns:
    --------
    pandas.DataFrame
        Loaded data
    """
    if file_type == 'auto':
        file_type = file_path.split('.')[-1].lower()
    
    try:
        if file_type == 'csv':
            return pd.read_csv(file_path)
        elif file_type in ['xlsx', 'xls']:
            return pd.read_excel(file_path)
        elif file_type == 'json':
            return pd.read_json(file_path)
        elif file_type == 'parquet':
            return pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def fetch_data_from_api(url, params=None, headers=None):
    """
    Fetch data from an API endpoint.
    
    Parameters:
    -----------
    url : str
        API endpoint URL
    params : dict, optional
        Query parameters
    headers : dict, optional
        Request headers
    
    Returns:
    --------
    pandas.DataFrame
        API response data
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Handle different API response formats
        if isinstance(data, list):
            return pd.DataFrame(data)
        elif isinstance(data, dict):
            # Try to find a data key
            for key in ['data', 'results', 'items', 'records']:
                if key in data:
                    return pd.DataFrame(data[key])
            # If no data key found, try to convert the dict directly
            return pd.DataFrame([data])
        else:
            return pd.DataFrame(data)
    except Exception as e:
        print(f"Error fetching from API: {e}")
        return None

def clean_dataframe(df, remove_duplicates=True, handle_missing='drop'):
    """
    Clean a dataframe by removing duplicates and handling missing values.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe
    remove_duplicates : bool
        Whether to remove duplicate rows
    handle_missing : str
        How to handle missing values ('drop', 'fill_mean', 'fill_median', 'fill_mode')
    
    Returns:
    --------
    pandas.DataFrame
        Cleaned dataframe
    """
    df_clean = df.copy()
    
    # Remove duplicates
    if remove_duplicates:
        initial_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        removed_rows = initial_rows - len(df_clean)
        if removed_rows > 0:
            print(f"Removed {removed_rows} duplicate rows")
    
    # Handle missing values
    if handle_missing == 'drop':
        df_clean = df_clean.dropna()
    elif handle_missing == 'fill_mean':
        df_clean = df_clean.fillna(df_clean.mean())
    elif handle_missing == 'fill_median':
        df_clean = df_clean.fillna(df_clean.median())
    elif handle_missing == 'fill_mode':
        df_clean = df_clean.fillna(df_clean.mode().iloc[0])
    
    return df_clean

def create_summary_stats(df, group_cols=None):
    """
    Create summary statistics for a dataframe.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe
    group_cols : list, optional
        Columns to group by
    
    Returns:
    --------
    pandas.DataFrame
        Summary statistics
    """
    if group_cols:
        return df.groupby(group_cols).agg({
            col: ['count', 'mean', 'std', 'min', 'max'] 
            for col in df.select_dtypes(include=[np.number]).columns
        }).round(2)
    else:
        return df.describe().round(2)

def save_chart(fig, filename, charts_dir='../charts', format='png', dpi=300):
    """
    Save a matplotlib figure to the charts directory.
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        Figure to save
    filename : str
        Name of the file (without extension)
    charts_dir : str
        Directory to save charts in
    format : str
        File format ('png', 'jpg', 'pdf', 'svg')
    dpi : int
        Resolution for raster formats
    """
    os.makedirs(charts_dir, exist_ok=True)
    filepath = os.path.join(charts_dir, f"{filename}.{format}")
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"Chart saved to: {filepath}")

def create_dashboard_style():
    """
    Set up a consistent style for all charts.
    """
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14
    print("Dashboard style applied!")

def generate_sample_data(n_rows=1000):
    """
    Generate sample data for testing and development.
    
    Parameters:
    -----------
    n_rows : int
        Number of rows to generate
    
    Returns:
    --------
    pandas.DataFrame
        Sample dataset
    """
    np.random.seed(42)
    
    # Generate dates
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(n_rows)]
    
    # Generate sample data
    data = {
        'date': dates,
        'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
        'value': np.random.normal(100, 20, n_rows),
        'count': np.random.poisson(50, n_rows),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_rows),
        'score': np.random.uniform(0, 100, n_rows)
    }
    
    return pd.DataFrame(data)

def pie_colors(n_main=10, others_color=(0.6, 0.6, 0.6)):
    """
    Returns a list of colors for a pie chart with n_main slices + 'Others'.
    Uses tab20 for main slices and a neutral color for 'Others'.
    """
    base_colors = plt.get_cmap('tab20').colors
    if n_main > len(base_colors):
        raise ValueError("Not enough distinct colors in the colormap for n_main slices.")
    return list(base_colors[:n_main]) + [others_color]

def chain_colors():
    """
    Returns a dictionary of brand colors for different blockchain networks.
    These colors are commonly used in their branding and documentation.
    
    Returns:
    --------
    dict
        Dictionary with chain names as keys and their brand colors as values
    """
    return {
        'ethereum': '#627EEA',  # Ethereum's official blue
        'solana': '#14F195',    # Solana's signature green
        'sui': '#4CA3FF'        # Sui's brand blue
    }

if __name__ == "__main__":
    # Test the functions
    print("Testing data utilities...")
    
    # Generate sample data
    sample_df = generate_sample_data(100)
    print(f"Generated sample data with {len(sample_df)} rows")
    
    # Test summary stats
    summary = create_summary_stats(sample_df, group_cols=['category'])
    print("\nSummary statistics by category:")
    print(summary) 