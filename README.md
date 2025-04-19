# Twitter Trend Scraper

## Overview

**Twitter Trend Scraper** is a Flask-based web application that automates the process of extracting trending topics from Twitter. The project uses Selenium for browser automation and MongoDB for storing the extracted data. This tool is designed to provide insights into the most popular discussions on Twitter in real time, making it valuable for trend analysis, market research, and content creation.

## Features

- **Automated Login**: Uses Selenium to log into Twitter securely.
- **Trending Topic Extraction**: Scrapes the top 5 trending topics directly from Twitter.
- **Data Storage**: Saves extracted trends with timestamps and metadata into a MongoDB database.
- **Proxy Support**: Integrates with ProxyMesh to enhance security and bypass regional restrictions.

## Technologies Used

- **Backend**: Flask, Python
- **Web Scraping**: Selenium with ChromeDriver
- **Database**: MongoDB
- **Proxy Management**: ProxyMesh

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kayush2003/Twitter-trend-scraper.git
   cd Twitter-trend-scraper
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MongoDB and ProxyMesh credentials in the script.
4. Run the application locally:
   ```bash
   python app.py
   ```
5. Access the web app at `http://localhost:8080`.


