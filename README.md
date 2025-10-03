# Project Title

Los Angeles Forest Fires Time Series Prediction based on Sentiment Analysis of Los Angeles Times Articles

## About the Project

This project combines research, benchmarking, and real-world coding to create a predictive model that estimates the likelihood of forest fires in Los Angeles based on 10 years of daily weather data and public sentiment extracted from LA Times articles. The project is divided into five logical phases, each building on the previous.

Objectives


Phase 1: Getting and Cleaning Weather Data
Retrieve 10 years of daily weather data using the Meteostat API.

Clean and normalize missing data.

Output: los_angeles_weather_10yrs_cleaned.csv

Phase 2: Web Scraping LA Times Articles
Compare BeautifulSoup vs. Scrapy.

Use requests + BeautifulSoup + cookies to bypass paywall.

Filter articles by fire-related and location keywords.

Output:

latimes_fire_articles.csv (raw)

latimes_fire_articles_cleaned.csv (relevant articles)

Phase 3: NLP & Sentiment Analysis
Use HuggingFace Transformers to:

Assign sentiment scores (-1 to +1)

Classify dominant emotion (fear, anger, concern, etc.)

Generate article summaries

Output:

latimes_fire_articles_sentiment.csv

latimes_emotion.csv

latimes_fire_summary_importance.csv

Phase 4: Predictive Modeling
Merge weather and emotion data by date (weather_enriched_with_emotion.csv)

Use fire_occurred as label (1 for fire, 0 for no fire).

Train and benchmark:

Logistic Regression

Random Forest

XGBoost

Output: logistic_regression.pkl, weather_with_fire_labels.csv

Phase 5: Streamlit Dashboard
Visualize trends and predictions:

Fire distribution pie chart

Box plot of temperature vs. fire occurrence

Dominant emotion trends

Interactive timeline with temperature + emotion + fire events

Output:

app.py

Streamlit dashboard




### Prerequisites

- Python (>=3.8)
- Jupyter Notebook (for running notebooks)

## Folder Structure (if extracted using Github)

Katigbak_300366535_Project/
├── app.py
├── model/
│   └── logistic_regression.pkl
├── data/
│   ├── los_angeles_weather_10yrs_cleaned.csv
│   ├── latimes_fire_articles.csv
│   ├── latimes_fire_articles_cleaned.csv
│   ├── latimes_fire_articles_sentiment.csv
│   ├── latimes_emotion.csv
│   ├── latimes_fire_summary_importance.csv
│   ├── weather_with_fire_labels.csv
│   └── weather_enriched_with_emotion.csv
├── README.md
├── requirements.txt
└── la_wildfire_ten_year_prediction.ipynb





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
pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy streamlit plotly



For Jupyter Notebook (Note: Regularly copy/paste/run this on the first cell of part1.ipynb and part2.ipynb just to make sure that these dependencies have also been installed in your Jupyter Notebook in case they have not been installed yet):
!pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy streamlit plotly



### Running the Project
Running the Project
Phase 1–4 (in Jupyter Notebook)
Open la_wildfire_ten_year_prediction.ipynb to run all the preprocessing, analysis, and modeling.

Phase 5: Streamlit Dashboard
From terminal inside the project folder:

streamlit run app.py

This opens the wildfire predictor dashboard in your browser.



What I Learned / Limitations

Learned:

Combining time series + NLP for multi-source forecasting

How emotion and sentiment can signal real-world events

Visual storytelling via Streamlit

Limitations:

Very few fire events (14 in 10 years) led to class imbalance

Emotions derived from articles may lag real fire dates

Summarization was not used in final model due to limited contribution



## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
