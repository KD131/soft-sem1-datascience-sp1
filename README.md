# SP1
This project is centred around companies that fellow students have previously interned with as part of the school program. The goal of the project is to create some sort of model for determining which company is the best *fit* given some profile parameters.

## Process
The initial data was given in a spreadsheet with student and company names. I then anonymised the student names and retrieved further data on the companies using [CVRAPI](https://cvrapi.dk/documentation). I save that data in a JSON file so I can retrieve it without having to make more requests to the API. Exceeding the quota proved an issue on the school network, and since I have a dynamic IP address at home, it was entirely unsuccessful there.

We clean the data by removing columns that have 90% missing data, all the same data (or close), and just columns I didn't think we'd need. Furthermore, later in the notebook when we take a closer look at the `employee` column, we will note that two values are missing. One of those values was because the API returned the version of a company listed as being bankrupt or no longer functional. In any case, we replace those values with the *median*. Not the *mean* because it is **heavily** skewed thanks to Novo Nordisk being a gigantic company.

We use [geopy](https://pypi.org/project/geopy/) (which in turn uses [Nominatim](https://nominatim.openstreetmap.org/ui/search.html)) to get geographical coordinates based on the street address. Those coordinates are then plotted on a map using [Folium](https://python-visualization.github.io/folium/) with information about the companies, like their names, added.

We find the companies' website and scrape them using [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), retrieve all their text paragraphs, and transform them into *vectors*. We then use *cosine similarity* to compare the companies to each other and see the ones most closely related, and find the most relevant to a search query.

Finally, we explore the descriptive statistics and distribution of the `employees` column, seeing as it is basically the only numerical data we have. We discover that the mean is heavily skewed by outliers, so we clean the data by removing those. Even still, the dataset has enormous variance because our sample size is so small. We plot the frequency distribution using [seaborn](https://seaborn.pydata.org/).

## Reflection
Our dataset is tiny, only 12 companies that vary greatly in size. The data retrieved from the CVR API also did not provide us with super useful data. The only truly numerical value of any use that I could see was the `employees` column, and that was heavily skewed by outliers.

In terms of categorical data, we have cities which are already coded by ZIP code, and industry description which also has a code in the API already.

While it was interesting working with data that may be useful for us in our search for companies to intern at, in terms of data quality it might have been easier and more instructive to work with datasets more designed for data analysis.

## Status
I didn't finish every task, sadly. I didn't integrate categorical encoding properly, and I didn't get to explore if any values were correlated.

Given how limited our dataset is, both in sample and feature size, I am unsure how good the results would be. There's not much to compare.
