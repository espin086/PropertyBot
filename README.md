# PropertyBot
This project conducts automated real estate analysis for the purpose of investing in single-family, multifamily, and passive syndication investments.

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to produce a set of tools to automate the due diligence portion of real estate analysis. The main objectives are quick analysis of metropolitan areas & properties for sale. 

### Statistical Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling


### Technologies
* Python 
* Google Cloud
* Jupyter

## Project Description

**Hypotheses**
1. A combination of Census data & Historical Listings can inform investment strategy & tactics
2. Profitable investments can be identified automatically using investor criteria (e.g., IRR, NPV, etc.)

**Data Sources**
1. Listing data comes from Redfin.com & Zillow.com
2. Syndication data comes from Crowdstreet.com
3. Census data comes from the American Community Survey
4. Real Estate Market Data Comes from Zillow

**Analysis Framework**
1. Identify desirable metropolitan areas by population growth, income growth, demographics, etc.
2. Analyze hundreds of properties at scale: expected rents, model expenses, and arrive at profitability. 
3. Create a Web Based tool to scale this analysis to investors across the United States.  

**Blockers**
1. Refactoring code to make it Flask/Web Page ready
2. Automate the collection of data via APIs as opposed to manual downloads.
3. Collect image data from property listings and classify them using Google Vision API. 


## Needs of this project

- frontend developers with experience in Flask and Heroku
- data engineers with experience building data pipelines using Airflow/Google Cloud


## Getting Started

1. Clone this repo: ```git clone https://github.com/espin086/PropertyBot.git```
2. pip install repo: ``` cd PropertyBot/ & pip install .```
3. Install xml scraper: ```sudo apt-get install python-lxml```
4. Use import repo into Python script: ```import PropertyBot```
5. Get help for repo: ```help (PropertyBot)```
6. To learn how to use modules in PropertyBot, get help for those repos: 



## Featured Notebooks/Analysis/Deliverables
* [Real Estate Investment Calculator](https://github.com/espin086/PropertyBot/blob/master/PropertyBot/notebooks/rental_investment_calculator.ipynb)
* [Optimizing Stock vs. Real Estate Investment Portfolio by City](https://github.com/espin086/AutoRedfinAnalysis/blob/master/realestate_vs_stocks/00_re_stock_tool.ipynb)
* [Exploration of Real Estate & Stock Market Returns](https://github.com/espin086/AutoRedfinAnalysis/blob/master/realestate_vs_stocks/01_exploratory_analysis.ipynb)
* [Finding Good Homes for Rent](https://github.com/espin086/PropertyBot/blob/master/RentBot/RentHunter.ipynb)

## Contributing Members

**Team Leads (Contacts) : 
* [JJ Espinoza](https://github.com/espin086) 
* jj.espinoza.la@gmail.com
* [linkedin](https://www.linkedin.com/in/jjespinoza)
* [Google Scholar Profile](https://scholar.google.com/citations?user=-SAt47cAAAAJ&hl=en)


