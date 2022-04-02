import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings
warnings.filterwarnings('ignore')

def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    Energy = pd.read_excel('../Energy Indicators.xls', header=17, nrows=227)
    Energy.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1, inplace=True)
    Energy.rename(columns={'Unnamed: 2': 'Country', 'Petajoules': 'Energy Supply', 'Gigajoules': 'Energy Supply per Capita', '%':'% Renewable'}, inplace=True)
    Energy['Energy Supply']*=1000000
    Energy['Country'].replace('[0-9]+$','',regex=True, inplace = True)
    Energy['Country'].replace('[ ]*\([\w ]*\)','',regex=True, inplace = True)
    Energy.replace('\.+', np.nan, regex=True, inplace=True)
    ctries_ed = {'Bolivia (Plurinational State of)': 'Bolivia', 'Republic of Korea': 'South Korea','United States of America': 'United States','United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong'}
    Energy['Country'].replace(ctries_ed, inplace=True)
    
    GDP = pd.read_csv('../world_bank.csv', header=4)
    GDP["Country Name"].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    years = [str(i) for i in range(1960,2006, 1)]
    GDP.rename(columns={'Country Name':'Country'}, inplace=True)
    GDP.drop(years, axis=1, inplace=True)

    ScimEn = pd.read_excel('../scimagojr-3.xlsx')
    
    data = pd.merge(pd.merge(ScimEn[0:15], Energy, on="Country"), GDP.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1) , on="Country")
    data.set_index("Country", inplace=True)
    
    data['pop']=data['Energy Supply']/ data['Energy Supply per Capita']
    data['Continent'] = data.index
    data['Continent'] = data['Continent'].apply(lambda x: ContinentDict[x])
    
    df = data[['Continent', '% Renewable']]
    df['% Renewable'] = pd.cut(df['% Renewable'], 5)
    return df.groupby(('Continent','% Renewable')).agg({'Continent':np.size}).dropna().squeeze()

answer_twelve()
