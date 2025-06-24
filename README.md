# Data Analysis Project

This project is set up for data analysis using Jupyter notebooks. It includes tools for data collection, manipulation, aggregation, and visualization.

## Requirements

- **Python 3.13+** (other recent versions may work, but 3.13 is tested)
- Recommended: Use a virtual environment

## Setup Instructions

### 1. Create a Virtual Environment (Recommended)
```bash
# Create a virtual environment
python3.13 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Your Environment
Run the provided test script to ensure all dependencies and utilities are working:
```bash
python test_setup.py
```
If all tests pass, you're ready to go!

### 4. Start Jupyter Lab
```bash
jupyter lab --collaborative
```

This will open Jupyter Lab in your default browser. Navigate to the `notebooks/` directory to find your analysis notebooks.

We use the `jupyter_collaboration` package with the `--collaborative` flag to enable collaborative editing, which is useful when using Cursor MCP.

### [Optional] 5. Cursor MCP

To use Cursor MCP, you need to install the `cursor-notebook-mcp` package. It is installed by default in the `requirements.txt` file.

In a new terminal, you need to run the MCP server in the background:

```bash
source venv/bin/activate
cursor-notebook-mcp --transport streamable-http --allow-root $(pwd)/notebooks --host 127.0.0.1 --port 8080
```

If you run into issues, try uninstalling and installing the `fastmcp` package as the default version installed by the cursor mcp library crashes:

```bash
pip uninstall fastmcp
pip install fastmcp==2.6.1
```

Then register the MCP server in Cursor as `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "notebook_mcp": {
      "url": "http://127.0.0.1:8080/mcp"
    }
  }
}
```

### 6. Environment Variables

Create a `.env` file in the root directory and add your environment variables.

```bash
DUNE_API_KEY=your_dune_api_key
VALIDATORS_API_KEY=your_validators_api_key
IPINFO_KEY=your_ipinfo_key
``` 

## Project Structure

```
decentralization_comps/
├── .env                # Environment variables
├── notebooks/           # Jupyter notebooks for analysis
│   └── 01_data_exploration.ipynb
├── data/               # Data files (raw and processed)
│   ├── raw/
│   └── processed/
├── src/                # Python modules and utilities
│   ├── __init__.py
│   └── data_utils.py
├── charts/             # Generated charts and visualizations
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore file
├── README.md           # This file
└── test_setup.py       # Environment test script
```



## Available Packages

- **Data Manipulation**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn, plotly, bokeh
- **Statistical Analysis**: scikit-learn, statsmodels
- **Web Scraping**: requests, beautifulsoup4, selenium
- **File Handling**: openpyxl, xlrd, sqlalchemy

## Getting Started

1. Open the `notebooks/01_data_exploration.ipynb` notebook
2. Follow the analysis workflow
3. Create additional notebooks as needed for specific analyses

## Troubleshooting

- **Installation fails with pandas or numpy errors:**
  - Make sure you are using Python 3.13+ and your virtual environment is activated.
  - If you see errors about `externally-managed-environment`, ensure you are not installing system-wide and that your venv is active.
- **Some packages not found:**
  - Try running `pip install --upgrade pip` before installing requirements.
- **Test script fails:**
  - Check the error messages for missing or misnamed packages. The script expects import names (e.g., `sklearn` for scikit-learn, `bs4` for beautifulsoup4).

## Tips

- Use virtual environments to manage dependencies
- Keep raw data separate from processed data
- Document your analysis steps in the notebooks
- Save charts and visualizations in the `charts/` directory

---

Happy analyzing! 🚀 