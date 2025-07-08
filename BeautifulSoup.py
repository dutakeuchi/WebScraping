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
for i in tables[table_index].tbody.find_all("tr"):
    print('\n')
    for row in i.find_all('td'):
        rank = row[0].text.strip()
        country = row[1]
        pop = row[2]
        area = row[3]
        dens = row[4]
        print(row, rank, country, area, dens)
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
for i in tables[table_index].tbody.find_all("tr"):
    col = i.find_all('td')
    # if col:
    print(col)
    print('\n')
# %%
tabela = pd.DataFrame(columns = ['Rank','Country','Population','Area','Density'])
tabela
# %%
