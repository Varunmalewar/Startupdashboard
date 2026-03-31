# Startup Dashboard

Live app:
https://pagepy-npmcvcrkqmiblcujulvbmc.streamlit.app/

## Overview
Startup Dashboard is a Streamlit project for exploring startup funding data with interactive views.

The project includes:
- A main funding analysis dashboard
- Investor-level analysis with charts
- A basic login and file upload demo page
- A UI playground page for Streamlit components

## Features
- Overall funding metrics:
  - Total funding
  - Maximum funding in a startup
  - Average funding per startup
  - Total funded startups
- Month-over-month trend view by amount or count
- Investor analysis:
  - Recent investments
  - Top investments
  - Sector split
  - Round/type split
  - City split
  - Year-wise investment trend
- CSV and Excel upload demo in login page

## Tech Stack
- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

## Project Structure
- app.py: Streamlit UI playground and widgets demo
- login.py: Simple login form and file uploader (CSV/XLSX)
- page.py: Main startup funding dashboard used for deployment
- requirements.txt: Python dependencies
- start_up_cleaned (2).csv: Preferred dataset for main dashboard
- start_up_cleaned.csv: Fallback dataset for main dashboard
- startup_funding.csv: Additional fallback dataset

## Data Loading Logic
The app uses deployment-safe relative paths in page.py.

It tries these files in order:
1. start_up_cleaned (2).csv
2. start_up_cleaned.csv
3. startup_funding.csv

If none are found, the app shows an error and stops safely.

## Local Run
1. Open terminal in project folder.
2. Create and activate virtual environment.
3. Install dependencies:
   pip install -r requirements.txt
4. Run Streamlit app:
   streamlit run page.py
5. Open the local URL shown in terminal.

## Deployment Notes (Streamlit Cloud)
- Main file path should be: page.py
- Keep dataset files in repository root with exact names listed above
- Do not use Windows absolute paths (for example D:\...)
- Use relative path loading (already implemented in page.py)
- If deployment looks stale:
  - Reboot app
  - Clear cache
  - Redeploy latest commit

## Required Dataset Columns
For page.py to work, dataset should contain these columns:
- startup
- investors
- vertical
- city
- round
- amount
- date

## Dependencies
Current requirements.txt:
- streamlit
- pandas
- numpy
- matplotlib

## Author
Varun Malewar
