# Bangladesh Post Code Scraper

This is a Python-based web scraper built using **Selenium** that retrieves post codes of all the post offices in **Bangladesh**, along with their corresponding **district** and **upazila** information. It provides a simple way to collect post code data for various locations across the country, making it useful for applications or databases that need geographical data.

## Features

- Scrapes the list of post offices in Bangladesh.
- Retrieves post codes, district names, and upazila information.
- Data is collected from the official government website of Bangladesh.
- Outputs the data in a structured format for easy use.

## Requirements

Before running the scraper, make sure you have the following installed:

- **Python 3.x**
- **Selenium**: `pip install selenium`
- **WebDriver**: You need chrome browser. No need to download webdriver additionaly.
- **Pandas (optional)**: For data manipulation and output formatting: `pip install pandas`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anisurMahmud/webscrapper.git
   cd webscrapper

# Output Format

The output CSV file will have the following columns:
- Post Office Name: The name of the post office.
- District: The district to which the post office belongs.
- Upazila: The upazila (sub-district) of the post office.
- Post Code: The postal code of the post office.
