"""
Data analysis utilities package.
"""

from .data_utils import (
    load_data_from_file,
    fetch_data_from_api,
    clean_dataframe,
    create_summary_stats,
    save_chart,
    create_dashboard_style,
    generate_sample_data
)

__version__ = "1.0.0"
__author__ = "Data Analysis Team"

__all__ = [
    'load_data_from_file',
    'fetch_data_from_api', 
    'clean_dataframe',
    'create_summary_stats',
    'save_chart',
    'create_dashboard_style',
    'generate_sample_data'
] 