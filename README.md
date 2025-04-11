# Project Title

Los Angeles Forest Fires Time Series Prediction based on Sentiment Analysis of Los Angeles Times Articles
presented by Juan Carlos Katigbak 300366535 to Nikhil Bhardwaj CSIS4260 Special Topics in Data Analytics Section 001

## About the Assignment

The purpose of this assignment is to combine research, benchmarking, and practical coding using the provided time-series dataset of Los Angeles weather patterns from January 1, 2014 to April 8, 2025 and web scraping from Los Angeles Times articles related to this, followed by comprehensive text analysis to be able to come up with an algorithm to try to predict when fires can happen in Los Angeles. The assignment is divided into five phases, each incorporating research and coding elements.

Objectives

Phase 1: Getting and Cleaning Data
Data Collection and Cleaning:
- Getting 1o years of daily weather data for Los Angeles using Meteostat API
- Cleaning data by removing empty columns, filling missing values, and preparing for modelling

Phase 2: Web Scraping
Research and Benchmarking:
- Compare two popular web scraping libraries
- Evaluate libraries based on ease of use and performance
- Scrape 10 years worth of Los Angeles Times articles about forest fires taking place in Los Angeles

Part 3: Text Analysis
Text Analysis:
- Load the data obtained from Phase 2
- Apply two text analysis algorithms LSD and LLM
- Generate a directional importance score (+1 for positive, -1 for negative) based on article content characteristics (e.g., length, summarization quality)
- Present the final analysis results clearly in a CSV file

Phase 4: Benchmarking Algorithms
Data Collection and Cleaning:
- ???

Phase 5: Using Streamlit for Data Visualization
Research and Benchmarking:
- ???


### Prerequisites

- Python (>=3.8)
- Jupyter Notebook (for running notebooks)

## Assignment Structure (if extracted using Github)

Katigbak_300366535_Assignment2
│── beautifulsoup_subreddit_canada_tariffs.ipynb   # Benchmarked BeautifulSoup scraper
│── scrapy_subreddit_canada_tariffs.py             # Benchmarked Scrapy scraper
│── part1.ipynb                                    # Chosen BeautifulSoup scraper used to scrape 100 Reddit                                                        posts
│── part2.ipynb                                    # Text analysis with LSD & Hugging Face algorithms
│── webscraped.csv                                 # Output CSV from Part 1 (created by running part1.ipynb)
│── webscraped.txt                                 # Output TXT from Part 1 (optional, also created                                                                part1.ipynb)
│── textanalysis.csv                               # Final text analysis output from Part 2 (created by                                                            running part2.ipynb)
│── README.md                                      # Assignment documentation (this file)




### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of Katigbak_300366535_Assignment2 folder

If getting it from OneDrive:
Just simply download the Katigbak_300366535_Assignment2.zip folder and extract the folder which will have the files.                           

If getting it from Github:
Extract Katigbak_300366535_Assignment2.zip and make sure that the extracted folder will have the files because there is a tendency that the extracted folder will have another folder before you are able to get the files. You also have to make sure when you run the virtual environment, you are able to locate the exact location of the Katigbak_300366535_Assignment2 folder otherwise it will not run properly.

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

(Note: Regularly copy/paste/run this on the first cell of part1.ipynb and part2.ipynb just to make sure that these dependencies have also been installed in your Terminal/Command Prompt in case they have not been installed yet)


For Jupyter Notebook (Note: Regularly copy/paste/run this on the first cell of part1.ipynb and part2.ipynb just to make sure that these dependencies have also been installed in your Jupyter Notebook in case they have not been installed yet):
!pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy


## Running each part of the assignment
**Best to run Part 1 and 2 in sequence to ensure that the whole assignment runs

Part 1: Web Scraping
First, we are going to be comparing 2 web scraper libraries to use. In my case, I chose BeautifulSoup and Scrapy.

(1) BeautifulSoup
using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open beautifulsoup_subreddit_canada_tariffs.ipynb in the Katigbak_300366535_Assignment2 folder wherever it is located in the Jupyter Notebook and run each code using shift + enter

(2) Scrapy
using either macOS/Linux's Terminal or Windows' Command Prompt, open a new tab for the Shell and run:

if using macOS/Linux's Terminal:

cd ~/Desktop/Katigbak_300366535_Assignment2
scrapy runspider scrapy_subreddit_canada_tariffs.py

if using Windows' Command Prompt:

cd %USERPROFILE%\Desktop\Katigbak_300366535_Assignment2
(e.g. cd OneDrive\Desktop\Katigbak_300366535_Assignment2) #since Katigbak_300366535_Assignment2 is the folder with the file

scrapy runspider scrapy_subreddit_canada_tariffs.py


Second, since I decided with BeautifulSoup we continue using part1.ipynb in the Katigbak_300366535_Assignment2 folder wherever it is located in the Jupyter Notebook and run each code using shift + enter. Once you run everything, it will create the webscraped.csv and webscraped.txt files in the same Katigbak_300366535_Assignment2 folder with webscraped.csv being the file to be able to do Part 2: Text Analysis (just the same, the webscraped.csv and webscraped.txt files are also available in the Katigbak_300366535_Assignment2 folder and will be overwritten once part1.ipynb is run).


Part 2: Text Analysis
In the same Jupyter Notebook wherever Katigbak_300366535_Assignment2 folder is located, open part2.ipynb and run each code using shift + enter which will then create textanalysis.csv in the samen folder which contains a summary of each article with corresponding importance score. (just the same, textanalysis.csv is also available in the Katigbak_300366535_Assignment2 folder and will be overwritten once part2.ipynb is run).

You can also skip Part 1 and go straight to Part 2 using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open part2.ipynb and run each code using shift + enter.

*Warning: expect 10 to 20 minutes for Part 2 Text Analysis to get the results depending on the CPU of your laptop

*Note: In case you run to a problem with running step2.ipynb on Windows, here is the step-by-step guide to install and fix transformers on Windows:

Step 1: Activate Your Virtual Environment
If you have already created a virtual environment, activate it.

- For Windows Command Prompt (CMD):

env\Scripts\activate

- For Windows PowerShell:

env\Scripts\Activate.ps1

If PowerShell gives a security error:
Run this command to allow scripts in PowerShell:

Set-ExecutionPolicy Unrestricted -Scope Process

Then, activate the environment again.

Step 2: Upgrade pip and setuptools
Old versions of pip and setuptools might cause issues when installing transformers. Upgrade them first:


pip install --upgrade pip setuptools wheel


Step 3: Install transformers, torch, and sentencepiece
Now, install transformers and all required dependencies:


pip install transformers torch sentencepiece

If you have issues installing sentencepiece, try:

pip install --no-cache-dir sentencepiece


Step 4: Verify the Installation
After installing, check if transformers is available:


python -c "import transformers; print(transformers.__version__)"
You should see an output like:

4.49.0




## Explanation of Each Part

Part 1: Web Scraping with BeautifulSoup
The goal of Part 1 was to evaluate popular web scraping libraries (BeautifulSoup and Scrapy) for retrieving data from websites, focusing primarily on ease of use, reliability, and beginner friendliness. After researching and benchmarking these libraries:

BeautifulSoup (selected library):

Pros: Easy to use and beginner-friendly for someone like me. Simple syntax for parsing HTML content.
Cons: Slightly slower compared to Scrapy, not designed for large-scale scraping tasks
Time to fetch article details: 26.21 seconds
Total time for scraping process: 26.79 seconds

Scrapy:

Pros: Highly efficient and scalable, built-in support for asynchronous scraping.
Cons: Higher complexity, less beginner-friendly for me due to the steep learning curve.
Time to fetch article details: 3.13 seconds
Total time for scraping process: 4.47 seconds


In spite of the delay in fetching and scraping, BeautifulSoup was chosen due to ease of use, readability of the code, and excellent suitability for beginners like me learning web scraping.

Implementation:

- Scraped the r/canada subreddit for 100 posts containing the topic "tariffs".
- Collected and parsed the Reddit titles, direct Reddit URLs, external links (if provided), and retrieved up to 50 comments per post.
- Implemented retry logic to handle Reddit API limitations (HTTP 429 rate limits).
- Generated two files (webscraped.csv and webscraped.txt) containing the retrieved posts and associated comments.

Output Example:

[1/100] Retrieved: 'Only Works as a State': Trump Vows Not 'To Bend' On Tariffs
Reddit URL: [reddit link]
External URL: [external link]
...
Collected 100 posts in 150.25 seconds.
Scraping complete!

Key Findings for Part 1:
- BeautifulSoup effectively retrieved data with minimal complexity.
- Error handling was necessary due to occasional retrieval issues (rate limits or unavailable content).
- Adding delays (time.sleep()) was necessary to avoid overwhelming Reddit servers and getting rate-limited (HTTP 429 errors).



Part 2: Text Analysis
In this section, the objective was to analyze the textual data scraped from Part 1 (Web Scraping), summarize each article, and determine an importance score with directional sentiment (positive or negative). I applied two algorithms:

LexRank (via LexRank summarizer - LSD): A straightforward, extractive summarization algorithm.
Hugging Face (transformers): Leveraged a pretrained language model for summarization.
These two methods were used to summarize the collected articles/comments and assign importance scores with a direction (positive or negative) related to the topic of "tariffs involving Canada".

Step 1 – Loading and Validating the Scraped Data
First, I verified the presence of the scraped CSV file before loading it, to ensure the script runs without file-related issues:

import os
import pandas as pd

SCRAPED_FILE = "webscraped.csv"

if not os.path.exists(SCRAPED_FILE):
    raise FileNotFoundError(f"Error: {SCRAPED_FILE} not found. Ensure file exists in directory.")
else:
    df = pd.read_csv(SCRAPED_FILE)
    print("Dataset loaded successfully.")
    
This validation makes sure there is reliability when running analysis on any machine.


Step 2 – Applying Text Summarization Algorithms
I chose two distinct summarization algorithms to explore their performance and quality differences:

(1) LSA-based (LSD) Summary:

This method applies the classical extractive summarization approach using Latent Semantic Analysis (LSD-based summarization), which works reliably regardless of text size but provides simpler summaries.

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_lsd(text, sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return ' '.join(str(sentence) for sentence in summary)
    
Observations:

- LSD summarizer consistently produced summaries for most articles.
- It failed only when insufficient text or no content was available.


Step 3 – Summarization with Hugging Face transformers
Utilized the Hugging Face library, specifically transformers with a pretrained summarization model (e.g., bart-large-cnn). However, this model encountered limitations, specifically an "IndexError: index out of range in self" due to the token input limit (~1024 tokens).

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_hf(text):
    max_input_tokens = 1024
    words = text.split()
    truncated_text = " ".join(words[:max_tokens])
    summary = summarizer(truncated_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
    
The Hugging Face summarizer frequently encountered errors like "IndexError: index out of range in self" due to the excessive length of some comments/posts, causing failures in generating summaries.

As a result, many summaries resulted in "Summarization error," indicating limitations in model input lengths or internal tokenizer errors.


Step 4 – Computing Importance Scores & Direction
For each summarization method, I derived an importance score based on the sentiment analysis of each summarized article/comment, using a pre-trained sentiment analyzer (transformers pipeline sentiment-analysis):

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    sentiment_result = sentiment_analyzer(text)[0]
    direction = 1 if sentiment['label'] == 'POSITIVE' else -1
    score = sentiment['score']
    return score, sentiment
    
Positive direction (+1): Indicates a positive sentiment towards tariffs as beneficial or favorable towards Canada.

Negative (-1) indicates negative sentiment, signifying negative impacts or criticism of tariffs against Canada.

Example:

"Canada stands strong against tariffs." = Positive score: +1
"Tariffs will severely harm Canadian industries." = Negative score: -1

Final Findings:
- LSA (sumy) summarization successfully handled almost all articles, providing concise, reliable summaries for a majority of articles.
- Hugging Face summarizer (transformers) was limited by input text length and often failed when text was too long or insufficiently structured.
- Sentiment analysis effectively assigned directional importance scores, clearly indicating the sentiment context around tariffs.
  
Key Takeaways:
- BeautifulSoup was successfully used to scrape Reddit efficiently for a small-to-medium dataset.
- Sumy's LSA summarizer reliably summarized content but provided simpler, less nuanced summaries.
- Hugging Face summarization models provided richer summaries but encountered issues with lengthy texts or input formatting constraints.
- Sentiment analysis provided meaningful directional scores for interpreting summarized text sentiment, enhancing interpretability and contextual analysis of the data.







   

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
