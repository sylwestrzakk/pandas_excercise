# pandas
These are tasks, which I've completed as a participant of online courses. Main domain is working with pandas library.

# us_teams

In this assignment you must read in a file of metropolitan regions and associated sports teams from assets/wikipedia_data.html 
and answer some questions about each metropolitan region. 

Each of these regions may have one or more teams from the "Big 4": 
NFL (football, in assets/nfl.csv), 
MLB (baseball, in assets/mlb.csv), 
NBA (basketball, in assets/nba.csv or 
NHL (hockey, in assets/nhl.csv). 
Please keep in mind that all questions are from the perspective of the metropolitan region, 
and that this file is the "source of authority" for the location of a given sports team. 
Thus teams which are commonly known by a different area (e.g. "Oakland Raiders") need to be mapped into 
the metropolitan region given (e.g. San Francisco Bay Area). 
This will require some human data understanding outside of the data you've been given.

Task:
Explore the hypothesis that **given that an area has two sports teams in different sports, those teams will perform the same within their respective sports**. 
How I would like to see this explored is with a series of paired t-tests (so use [`ttest_rel`]) between all pairs of sports. 
Are there any sports where we can reject the null hypothesis? 
Again, average values where a sport has multiple teams in one region. 
Remember, you will only be including, for each sport, cities which have teams engaged in that sport, drop others as appropriate. 

# countries_energy
Load the energy data from the file `assets/Energy Indicators.xls`, which is a list of indicators of 
[energy supply and renewable electricity production](assets/Energy%20Indicators.xls) 
from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013.

Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. 

The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
`['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`

Convert `Energy Supply` to gigajoules (**Note: there are 1,000,000 gigajoules in a petajoule**). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.

Rename the following list of countries (for use in later questions):

```"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"```

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.  `'Switzerland17'` should be `'Switzerland'`.

Next, load the GDP data from the file `assets/world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 

Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `assets/scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.

Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 

The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
       'Citations per document', 'H index', 'Energy Supply',
       'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
       '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
       
NEXT TASK:
Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
*This function should return a Series with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*
