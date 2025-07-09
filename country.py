# %%
from bs4 import BeautifulSoup
import pandas as pd
import requests
# %%
url = 'https://www.scrapethissite.com/pages/simple/'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())
# %%
df = pd.DataFrame(columns=('name','capital','population','area','language',))
web = soup.find_all('div', class_="col-md-4 country")
for i in range(len(web)):
    name = web[i].find('h3', class_="country-name").get_text(strip=True)
    capital = web[i].find('span', class_='country-capital').get_text(strip=True)
    pop = web[i].find('span', class_='country-population').get_text(strip=True)
    area = web[i].find('span', class_='country-area').get_text(strip=True)
    
    name_wiki = name.replace(' ','_')
    url_wiki = 'https://simple.wikipedia.org/wiki/'
    data_wiki = requests.get(url_wiki+name_wiki).text
    soup_wiki = BeautifulSoup(data_wiki,'html.parser')
    
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
        

    
    new_df = pd.DataFrame([{'name':name,
                            'capital':capital,
                            'population':pop,
                            'area':area,
                            'language':language_wiki,
                            }])
    df = pd.concat([df, new_df], ignore_index=True)
df


# %%
df.language.value_counts()
# %%
df.language
# %%
