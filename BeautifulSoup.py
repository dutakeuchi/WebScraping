# %%
from bs4 import BeautifulSoup
import pandas as pd
import requests

# %%
url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
# %%
pop = BeautifulSoup(data, 'html.parser')
# %%
print(pop.prettify())
# %%
tables = pop.find_all('table')
# %%
len(tables)
# %%
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
# %%

# for index,table in enumerate(tables):
#     if ("World population" in str(table)):
#         table_index = index
# print(table_index)
# %%
print(tables[table_index].prettify())

# %%
tabela = pd.DataFrame(columns = ['Rank','Country','Population','Area','Density'])
for i in tables[table_index].tbody.find_all("tr"):
    col = i.find_all('td')
    if col:
        rank = col[0].text.strip()
        country = col[1].text.strip()
        pop = col[2].text.strip()
        area = col[3].text.strip()
        dens = col[4].text.strip()
        new_df = pd.DataFrame([{'Rank':rank, 'Country':country, 'Population':pop, 'Area':area, 
                              'Density':dens}])
        tabela = pd.concat([tabela, new_df], ignore_index=True)
tabela

# tabela

        

# %%
pop_df = pd.read_html(str(tables[5]), flavor='bs4')[0]
pop_df
# %%
dataframe_list = pd.read_html(url, flavor='bs4')
dataframe_list
# %%
len(dataframe_list)
# %%
dataframe_list[5]
# %%
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
# %%
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')
# %%
