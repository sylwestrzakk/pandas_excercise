import pandas as pd
import numpy as np
import scipy.stats as stats
import re

mlb_df=pd.read_csv("../mlb.csv")
nhl_df=pd.read_csv("../nhl.csv")
nba_df=pd.read_csv("../nba.csv")
nfl_df=pd.read_csv("../nfl.csv")
cities=pd.read_html("../wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def sports_team_performance():
    nfl = nfl_df.where(nfl_df['W'].str.match(r'(\d+)')).dropna()
    nfl['W'] = nfl['W'].astype(int)
    nfl['L'] = nfl['L'].astype(int)
    nfl['ratio'] = nfl['W']/(nfl['L']+nfl['W'])
    nfl = nfl[nfl['year']==2018][['team', 'ratio']]
    nfl['team'].replace('[\*\+]*', '', regex=True, inplace=True)
    nfl.rename(columns={'team': 'NFL'}, inplace=True)
    nfl[['cty', 'NFL']] = nfl['NFL'].str.extract('(.+) (\w+$)')

    nfl['cty'].replace({'Toronto Maple': 'Toronto', 'Detroit Red': 'Detroit','Columbus Blue': 'Columbus', 'Vegas Golden':'Las Vegas', 'Minnesota': 'Minneapolis–Saint Paul',
                        'Portland Trail': 'Portland', 'Brooklyn':'New York', 'Golden State': 'San Francisco Bay Area', 'Miami': 'Miami–Fort Lauderdale',
                        'Indiana':'Indianapolis', 'Utah':'Salt Lake City', 'Boston Red': 'Boston', 'Chicago White':'Chicago',
                        'Toronto Blue':'Toronto', 'Arizona':'Phoenix', 'San Francisco':'San Francisco Bay Area', 'Oakland':'San Francisco Bay Area',
                        'Texas':'Dallas', 'Colorado':'Denver', 'Tennessee':'Nashville', 'New England':'Boston', 'Carolina':'Charlotte',
                       'San Jose':'San Francisco Bay Area', 'Anaheim':'Los Angeles', 'Florida':'Miami–Fort Lauderdale', 'Carolina':'Raleigh', 'New Jersey':'New York'}, inplace=True)
    nfl['NFL'].replace({'Blazers':'Trail Blazers', 'Jays':'Blue Jays'}, inplace=True)
    nfl.sort_values(by='NFL')
    nfl = pd.DataFrame(nfl.groupby('cty').agg(np.mean)['ratio'].reset_index())
    
    teams = nhl_df.where(nhl_df["W"].str.match(r'(\d+)')).dropna() #NHL
    teams['W'] = teams['W'].astype(int)
    teams['L'] = teams['L'].astype(int)
    teams['ratio'] = teams['W']/(teams['L']+teams['W'])
    teams['team'].replace('\*', '', regex=True, inplace=True)
    teams.rename(columns={'team': 'NHL'}, inplace=True)
    teams[['cty', 'NHL']] = teams['NHL'].str.extract('(.+) (\w+$)')
    teams = teams[teams['year']==2018.]
    teams.drop(columns=['OL', 'PTS', 'PTS%', 'GF', 'GA', 'SRS', 'SOS',
               'RPt%', 'ROW', 'year', 'League', 'GP', 'W', 'L'], inplace=True)
    teams['cty'].replace({'Toronto Maple': 'Toronto', 'Detroit Red': 'Detroit','Columbus Blue': 'Columbus', 'Vegas Golden':'Las Vegas', 'Minnesota': 'Minneapolis–Saint Paul',
                            'Portland Trail': 'Portland', 'Brooklyn':'New York', 'Golden State': 'San Francisco Bay Area', 'Miami': 'Miami–Fort Lauderdale',
                            'Indiana':'Indianapolis', 'Utah':'Salt Lake City', 'Boston Red': 'Boston', 'Chicago White':'Chicago',
                            'Toronto Blue':'Toronto', 'Arizona':'Phoenix', 'San Francisco':'San Francisco Bay Area', 'Oakland':'San Francisco Bay Area',
                            'Texas':'Dallas', 'Colorado':'Denver', 'Tennessee':'Nashville', 'New England':'Boston', 'Carolina':'Charlotte',
                           'San Jose':'San Francisco Bay Area', 'Anaheim':'Los Angeles', 'Florida':'Miami–Fort Lauderdale', 'Carolina':'Raleigh', 'New Jersey':'New York'}, inplace=True)
    teams = teams.drop('NHL', axis=1).groupby('cty').agg(np.mean)
    nhl = teams
    
    nba = nba_df.where(nba_df["W"].str.match(r'(\d+)')).dropna()
    nba['W'] = nba['W'].astype(int)
    nba['L'] = nba['L'].astype(int)
    nba['ratio'] = nba['W']/(nba['L']+nba['W'])
    nba = nba[nba['year']==2018][['team', 'ratio']]

    nba['team'].replace('[\*]*\s\(.+\)', '', regex=True, inplace=True)
    nba.rename(columns={'team': 'NBA'}, inplace=True)
    nba[['cty', 'NBA']] = nba['NBA'].str.extract('(.+) (\w+$)')

    nba['cty'].replace({'Toronto Maple': 'Toronto', 'Detroit Red': 'Detroit','Columbus Blue': 'Columbus', 'Vegas Golden':'Las Vegas', 'Minnesota': 'Minneapolis–Saint Paul',
                        'Portland Trail': 'Portland', 'Brooklyn':'New York', 'Golden State': 'San Francisco Bay Area', 'Miami': 'Miami–Fort Lauderdale',
                        'Indiana':'Indianapolis', 'Utah':'Salt Lake City', 'Boston Red': 'Boston', 'Chicago White':'Chicago',
                        'Toronto Blue':'Toronto', 'Arizona':'Phoenix', 'San Francisco':'San Francisco Bay Area', 'Oakland':'San Francisco Bay Area',
                        'Texas':'Dallas', 'Colorado':'Denver', 'Tennessee':'Nashville', 'New England':'Boston', 'Carolina':'Charlotte',
                       'San Jose':'San Francisco Bay Area', 'Anaheim':'Los Angeles', 'Florida':'Miami–Fort Lauderdale', 'Carolina':'Raleigh', 'New Jersey':'New York'}, inplace=True)
    nba['NBA'].replace({'Blazers':'Trail Blazers'}, inplace=True)
    nba = pd.DataFrame(nba.groupby('cty').agg(np.mean)['ratio'].reset_index())
    
    mlb = mlb_df
    mlb['ratio'] = mlb_df['W']/(mlb_df['L']+mlb_df['W'])
    mlb = mlb[mlb['year']==2018][['team', 'ratio']]

    mlb.rename(columns={'team': 'MLB'}, inplace=True)
    mlb[['cty', 'MLB']] = mlb['MLB'].str.extract('(.+) (\w+$)')

    mlb['cty'].replace({'Toronto Maple': 'Toronto', 'Detroit Red': 'Detroit','Columbus Blue': 'Columbus', 'Vegas Golden':'Las Vegas', 'Minnesota': 'Minneapolis–Saint Paul',
                        'Portland Trail': 'Portland', 'Brooklyn':'New York', 'Golden State': 'San Francisco Bay Area', 'Miami': 'Miami–Fort Lauderdale',
                        'Indiana':'Indianapolis', 'Utah':'Salt Lake City', 'Boston Red': 'Boston', 'Chicago White':'Chicago',
                        'Toronto Blue':'Toronto', 'Arizona':'Phoenix', 'San Francisco':'San Francisco Bay Area', 'Oakland':'San Francisco Bay Area',
                        'Texas':'Dallas', 'Colorado':'Denver', 'Tennessee':'Nashville', 'New England':'Boston', 'Carolina':'Charlotte',
                       'San Jose':'San Francisco Bay Area', 'Anaheim':'Los Angeles', 'Florida':'Miami–Fort Lauderdale', 'Carolina':'Raleigh', 'New Jersey':'New York'}, inplace=True)
    mlb['MLB'].replace({'Blazers':'Trail Blazers', 'Jays':'Blue Jays'}, inplace=True)
    mlb = pd.DataFrame(mlb.groupby('cty').agg(np.mean)['ratio'].reset_index())
    
    analy = pd.merge(pd.merge(pd.merge(nfl, nba, on='cty', how='outer'), nhl, on='cty', how='outer'), mlb, on='cty', how='outer')
    analy.columns = ['City','NFL', 'NBA', 'NHL', 'MLB']
    #print(analy)
    
    df = analy.drop('City', axis=1)
    #print(df)
    sports = ['NFL', 'NBA', 'NHL', 'MLB']

    p_values = pd.DataFrame({k:np.nan for k in sports}, index=sports)
    for item in sports:
        for it2 in sports:
            if item != it2:
                x = pd.merge(analy[['City',item]], analy[['City',it2]], on='City', how='inner')[[item, it2]].dropna()
                p_values[item][it2] = stats.ttest_rel(x[item], x[it2])[1]
            else:
                p_values[item][it2] = np.nan
    return p_values

print(sports_team_performance())
