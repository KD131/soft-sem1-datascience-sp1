# Company Internships
## Table of contents
- [1. SP1](#1-sp1)
  - [1.1. Process](#11-process)
  - [1.2. Reflection](#12-reflection)
  - [1.3. Status](#13-status)
- [2. SP2](#2-sp2)
  - [2.1. What did I do?](#21-what-did-i-do)
  - [2.2. Methods](#22-methods)
  - [2.3. Challenges](#23-challenges)
  - [2.4. Accuracy](#24-accuracy)
  - [2.5. Improvements](#25-improvements)
- [3. SP3](#3-sp3)
  - [3.1. Data](#31-data)
  - [3.2. Processing](#32-processing)
  - [3.3. Prototype](#33-prototype)
- [4. SP4](#4-sp4)
  - [4.1. Setup](#41-setup)
  - [4.2. Status](#42-status)

## 1. SP1
This project is centred around companies that fellow students have previously interned with as part of the school program. The goal of the project is to create some sort of model for determining which company is the best *fit* given some profile parameters.

### 1.1. Process
The initial data was given in a spreadsheet with student and company names. I then anonymised the student names and retrieved further data on the companies using [CVRAPI](https://cvrapi.dk/documentation). I save that data in a JSON file so I can retrieve it without having to make more requests to the API. Exceeding the quota proved an issue on the school network, and since I have a dynamic IP address at home, it was entirely unsuccessful there.

We clean the data by removing columns that have 90% missing data, all the same data (or close), and just columns I didn't think we'd need. Furthermore, later in the notebook when we take a closer look at the `employee` column, we will note that two values are missing. One of those values was because the API returned the version of a company listed as being bankrupt or no longer functional. In any case, we replace those values with the *median*. Not the *mean* because it is **heavily** skewed thanks to Novo Nordisk being a gigantic company.

We use [geopy](https://pypi.org/project/geopy/) (which in turn uses [Nominatim](https://nominatim.openstreetmap.org/ui/search.html)) to get geographical coordinates based on the street address. This data is also saved to a JSON file to avoid requesting the same data from the API when the code is rerun. This is in compliance with Nominatum's [terms of service](https://operations.osmfoundation.org/policies/nominatim/). Those coordinates are then plotted on a map using [Folium](https://python-visualization.github.io/folium/) with information about the companies, like their names, added.

We find the companies' website and scrape them using [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), retrieve all their text paragraphs, and transform them into *vectors*. We then use *cosine similarity* to compare the companies to each other and see the ones most closely related, and find the most relevant to a search query.

The scraped text data is again saved to JSON to avoid further requests.

Finally, we explore the descriptive statistics and distribution of the `employees` column, seeing as it is basically the only numerical data we have. We discover that the mean is heavily skewed by outliers, so we clean the data by removing those. Even still, the dataset has enormous variance because our sample size is so small. We plot the frequency distribution using [seaborn](https://seaborn.pydata.org/).

### 1.2. Reflection
Our dataset is tiny, only 12 companies that vary greatly in size. The data retrieved from the CVR API also did not provide us with super useful data. The only truly numerical value of any use that I could see was the `employees` column, and that was heavily skewed by outliers.

In terms of categorical data, we have cities which are already coded by ZIP code, and industry description which also has a code in the API already.

While it was interesting working with data that may be useful for us in our search for companies to intern at, in terms of data quality it might have been easier and more instructive to work with datasets more designed for data analysis.

### 1.3. Status
I didn't finish every task, sadly. I didn't integrate categorical encoding properly, and I didn't get to explore if any values were correlated.

Given how limited our dataset is, both in sample and feature size, I am unsure how good the results would be. There's not much to compare.

## 2. SP2
The second part of the project centred around acquiring more numerical data and using it in machine learning algorithms.

### 2.1. What did I do?
In this exercise, we got some more numerical data from [Proff.dk](https://proff.dk/), specifically more accurate data regarding no. employees and financial reports dating back some years.

I then plotted the data to investigate it, and used that financial data to create a model for a specific company that can predict their profits for a given year.

I unfortunately did not have time to do any classification for task 3 of the assignment. I will do it soon, but at the time of hand-in, it has not been done.

### 2.2. Methods
We do not have access to the Proff.dk API, so I instead built a web-scraper to fetch the data, I wanted. Like my other functions that fetch data from somewhere, I save it to a JSON file, so that it doesn't need to be fetched every time the code is run.

I used a **LinearRegression** model to predict a company's profits given a year. The model is trained on that compnay's prior finances each year, so it makes sense to just plot a line with the trend over the years.

### 2.3. Challenges
The webscraper took way longer than anticipated to create. I build a Pandas dataframe from the finance table and clean it and process it so it contains what I want. That took some bug fixing.

When reading the JSON file, it would insert the rows in incorrect order which also took some time to figure out. That could've been avoided by not saving everything to JSON and then reading it from a file, but it makes the program run faster and saves on network calls.

I had some doubts on what the right way to train the linear regression model on profits would be. It makes sense to build a more general model that takes more parameters. However, the companies vary wildly in their finances, and we also don't have much other data to use.

So I trained a model for specific companies using that company's financial data for the previous years.

### 2.4. Accuracy
Because I only have a max of 9 years history for the linear regression model, there's not a lot of data to do a *train-test split* on. I therefore do not have any test data to actually test the accuracy of the model.

### 2.5. Improvements
If we had more data to generalise the model instead of being specific to a company, and we had more companies, we could more confidently split the data to actually test the accuracy.

## 3. SP3
This part of the project centred on NLP.

### 3.1. Data
I found two Python packages for fetching data from Wikipedia, [`wikipedia`](https://pypi.org/project/wikipedia/) and [`Wikipedia-API`](https://pypi.org/project/Wikipedia-API/). I ended up using the older `wikipedia` package but either is completely fine.

I fetched data for each of the companies. Some of the search results on Wikipedia led to pages that were unrelated to them, like "Alpha Solutions" leading to a [German diesel company](https://da.wikipedia.org/wiki/MAN_Diesel), and "Dafolo" a [Brazilian football player](https://da.wikipedia.org/wiki/Danilo_Luiz_da_Silva).

### 3.2. Processing
I used DaCy since the data I'm working with is Danish.

I showed a small test of processing a bit of text, but I didn't have a use for processing all the text data that I retrieved from Wikipedia.

### 3.3. Prototype
The task was to make a prototype for a *typical NLP implementation*. I couldn't come up with a good idea for an application, and frankly, I didn't have a ton of time with two other projects to do over the Easter **holiday**, one of them being an **exam** that I've then not had time to work on.

Instead I just showed a word cloud of the "Novo Nordisk" Wikipedia page.

## 4. SP4
This assignment is about visualisation of data using various graphs and exposing them in some sort of frontend so users can explore the data.

I've decided to use [Streamlit](https://streamlit.io/) because it's an easy way to build a webapp in Python that also integrates all manner of graph libraries.

### 4.1. Setup
To run it, install Streamlit.

```shell
pip install streamlit
```

 Then run the main page.

 ```shell
 streamlit run 9_🏠_Visualisation.py
 ```

 or 

 ```shell
 streamlit run https://raw.githubusercontent.com/KD131/soft-sem1-datascience-sp1/main/9_%F0%9F%8F%A0Visualisation.py
 ```

 *For some reason, it doesn't read the `pages` folder when using the URL from GitHub, so run it from a local clone.*

 ### 4.2. Status
 I got the basics down, but it'd be cool to try out more plotting libraries and more interesting aspects of the data to show, though I don't know what that would be exactly.

 The map is very disappointing seeing as the height of the hexagons has nothing to do with the individual company. I tried hard to fix it, but no such luck.

 - [x] Table
 - [x] Graph
 - [x] Map
 - [ ] Maybe some other fun stuff