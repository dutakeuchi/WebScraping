# %%
# importing libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
# %%
# getting data from web site and visualizing it
url = 'https://www.scrapethissite.com/pages/simple/'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())
# %%
# creating a dataframe and adding values.
df = pd.DataFrame(columns=('name','capital','population','area','language',))
web = soup.find_all('div', class_="col-md-4 country")
for i in range(len(web)):
    name = web[i].find('h3', class_="country-name").get_text(strip=True)
    capital = web[i].find('span', class_='country-capital').get_text(strip=True)
    pop = web[i].find('span', class_='country-population').get_text(strip=True)
    area = web[i].find('span', class_='country-area').get_text(strip=True)
    
    
# getting language from wikipedia
    name_wiki = name.replace(' ','_')
    url_wiki = 'https://simple.wikipedia.org/wiki/'
    data_wiki = requests.get(url_wiki+name_wiki).text
    soup_wiki = BeautifulSoup(data_wiki,'html.parser')

# language information values
    table = soup_wiki.find('table')
    if table:
        language_get = table.find('tr',class_='mergedtoprow')
        if language_get:
            find_language = language_get.find('a')
            if find_language:
                language_wiki = find_language.get_text(strip=True)
            else:
                find_language = language_get.find('td')
                language_wiki = find_language.get_text(strip=True) if find_language else 'NO INFORMATION'
        else:
            language_wiki = 'NO INFORMATION'
    else:
        language_wiki = 'NO INFORMATION'
    
    
    # table = soup_wiki.find('table')
    # if table:  
    #     language_get = table.find('tr',class_='mergedtoprow')
    #     if language_get:
    #         find_language = language_get.find('a')
    #         language_wiki = find_language.get_text(strip=True) if find_language else 'NO INFORMATION'
    #     elif:
    #         find_language = language_get.find('td')
    #         language_wiki = find_language.get_text(strip=True) if find_language else 'NO INFORMATION'
    #     else:
    #         language_wiki = 'NO INFORMATION'
    # else:
    #     language_wiki = 'NO INFORMATION'
        

# adding values to dataframe    
    new_df = pd.DataFrame([{'name':name,
                            'capital':capital,
                            'population':pop,
                            'area':area,
                            'language':language_wiki,
                            }])
    df = pd.concat([df, new_df], ignore_index=True)
df



# %%
# some tables don't follow the same standarts so many languages could not get scraped.
# %%
df.to_csv('Web_scraping.csv', sep=';')
# %%
