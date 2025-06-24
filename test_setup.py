#!/usr/bin/env python3
"""
Test script to verify that all packages and utilities are working correctly.
"""

import sys
import importlib

def test_imports():
    """Test that all required packages can be imported."""
    packages = [
        'pandas', 'numpy', 'matplotlib', 'seaborn', 'plotly', 'bokeh',
        'sklearn', 'statsmodels', 'requests', 'bs4',
        'sqlalchemy', 'openpyxl', 'tqdm', 'jupyter', 'notebook'
    ]
    
    print("Testing package imports...")
    failed_imports = []
    
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {failed_imports}")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_data_utils():
    """Test our custom data utilities."""
    try:
        from src.data_utils import (
            load_data_from_file, fetch_data_from_api, clean_dataframe,
            create_summary_stats, save_chart, create_dashboard_style,
            generate_sample_data
        )
        print("✅ Data utilities imported successfully")
        
        # Test sample data generation
        sample_df = generate_sample_data(100)
        print(f"✅ Generated sample data: {sample_df.shape}")
        
        # Test summary stats
        summary = create_summary_stats(sample_df, group_cols=['category'])
        print(f"✅ Created summary stats: {summary.shape}")
        
        return True
    except Exception as e:
        print(f"❌ Data utilities test failed: {e}")
        return False

def test_visualization():
    """Test basic visualization capabilities."""
    try:
        import matplotlib.pyplot as plt
        import seaborn as sns
        import pandas as pd
        import numpy as np
        
        # Create a simple plot
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title('Test Plot')
        plt.close()  # Close to avoid displaying
        
        print("✅ Basic visualization test passed")
        return True
    except Exception as e:
        print(f"❌ Visualization test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Data Analysis Environment Setup")
    print("=" * 50)
    
    # Test package imports
    imports_ok = test_imports()
    
    # Test data utilities
    utils_ok = test_data_utils()
    
    # Test visualization
    viz_ok = test_visualization()
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"Package Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"Data Utilities:  {'✅ PASS' if utils_ok else '❌ FAIL'}")
    print(f"Visualization:   {'✅ PASS' if viz_ok else '❌ FAIL'}")
    
    if all([imports_ok, utils_ok, viz_ok]):
        print("\n🎉 All tests passed! Your environment is ready for data analysis.")
        print("\nNext steps:")
        print("1. Open Jupyter: jupyter notebook")
        print("2. Navigate to notebooks/01_data_exploration.ipynb")
        print("3. Start analyzing your data!")
    else:
        print("\n⚠️  Some tests failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 