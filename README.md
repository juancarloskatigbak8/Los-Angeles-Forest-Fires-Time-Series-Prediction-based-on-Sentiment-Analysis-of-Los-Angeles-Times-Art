# Project Title

Los Angeles Forest Fires Time Series Prediction based on Sentiment Analysis of Los Angeles Times Articles
presented by Juan Carlos Katigbak 300366535 to Nikhil Bhardwaj CSIS4260 Special Topics in Data Analytics Section 001

## About the Assignment

This assignment combines research, benchmarking, and real-world coding to create a predictive model that estimates the likelihood of forest fires in Los Angeles based on 10 years of daily weather data and public sentiment extracted from LA Times articles. The assignment is divided into five logical phases, each building on the previous.

Objectives

Phase 1: Getting and Cleaning Weather Data
- Retrieve 10 years of daily weather data (2014–2025) using the Meteostat API.
- Clean the dataset by handling null values and removing empty columns.
- Prepare for time series modeling by ensuring consistency and completeness.

Phase 2: Web Scraping Los Angeles Times Articles
- Benchmark BeautifulSoup and Scrapy as scraping tools.
- Use BeautifulSoup with requests + cookies to scrape fire-related articles from latimes.com from 2014–2025.
- Apply strict keyword and location filtering ("wildfire", "los angeles", etc.) to improve data relevance.
- Store results in CSV and TXT files (latimes_fire_articles.csv, latimes_fire_articles_cleaned.csv).

Phase 3: NLP & Sentiment Analysis
- Clean and preprocess all scraped content.
- Use HuggingFace Transformers for:
  - Sentiment scoring (range: -1 to +1)
  - Emotion classification (fear, alert, sadness, anger, neutral)
  - Summarization using bart-large-cnn
- Assign each article a directional importance score based on combined sentiment and emotion analysis.
- Save all outputs to CSV for integration in Phase 4.

Phase 4: Predictive Modeling (Upcoming)
- Merge weather and sentiment data by date.
- Engineer features combining meteorological and public emotion/sentiment trends.
- Train a classifier (e.g., Random Forest, XGBoost) to predict “fire/no fire” labels for each day.

Phase 5: Streamlit Dashboard (Upcoming)
- Build an interactive dashboard to:
  - Display forecast probabilities
  - Visualize historical fire events
  - Track emotion/sentiment trends
  - Include upload feature for new LA Times article input and prediction


### Prerequisites

- Python (>=3.8)
- Jupyter Notebook (for running notebooks)

## Folder Structure (if extracted using Github)

Katigbak_300366535_Project
├── la_wildfire_ten_year_prediction    # Scraper and filtering pipeline using BeautifulSoup
├── latimes_fire_articles.csv          # Raw scraped articles
├── latimes_fire_articles_cleaned.csv  # Filtered articles by keyword relevance
├── latimes_fire_articles_sentiment.csv# Articles with sentiment score
├── latimes_fire_summary_importance.csv# Articles with summary + importance
├── latimes_emotion.csv                # Articles with emotion classification
├── los_angeles_weather_10yrs.csv      # Cleaned weather dataset (2014–2025)
├── README.md                          # Documentation (this file)




### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of Katigbak_300366535_Project folder

If getting it from OneDrive:
Just simply download the Katigbak_300366535_Project.zip folder and extract the folder which will have the files.                           

If getting it from Github:
Extract Katigbak_300366535_Project.zip and make sure that the extracted folder will have the files because there is a tendency that the extracted folder will have another folder before you are able to get the files. You also have to make sure when you run the virtual environment, you are able to locate the exact location of the Katigbak_300366535_Project folder otherwise it will not run properly.

2. Set Up a Virtual Environment (Optional but Recommended)
   
For macOS/Linux (Terminal):
python -m venv env
source env/bin/activate

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

* Make sure to proactively do this in both Terminal/Command Prompt and Jupyter Notebook just to be sure so that there is no interruption with running the assignment!

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy


For Jupyter Notebook (Note: Regularly copy/paste/run this on the first cell of part1.ipynb and part2.ipynb just to make sure that these dependencies have also been installed in your Jupyter Notebook in case they have not been installed yet):
!pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy


### Running the Project
Phase 1: Weather Data Collection
Weather data retrieved from the Meteostat API. Run code cells in la_wildfire_ten_year_prediction.ipynb.

Phase 2: Web Scraping
- Run la_wildfire_ten_year_prediction.ipynb.ipynb for scraping LA Times articles (filtered for fire-related events).
- Requires cookies from an active LA Times subscription.

Phase 3: Text Analysis
- Run part2.ipynb to process scraped articles with:
  - HuggingFace summarization
  - Sentiment polarity analysis
  - Emotion classification (fear, alert, sadness, neutral, anger)
- Output: CSV files for modeling.


Notes on Modeling (Phase 4)
Initial modeling will:

Merge article sentiment/emotion with weather by date.

Use historical wildfire occurrences (if available) as labels.

Train a classifier to forecast risk of fire based on weather + public mood.












   

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
