# %%
from bs4 import BeautifulSoup
import pandas as pd
import requests
# %%
url = 'https://www.hostelworld.com/hostels/europe/germany/berlin/'
link = requests.get(url).text
# %%
soup = BeautifulSoup(link, 'html.parser')
print(soup.prettify())
# %%
test = soup.find_all(class_= "property-listing-cards")
# %%
test[0]
# %%
print(test[1].prettify())
# %%
len(test)
# %%
asd = test.find_all(class_)
# %%
# "carousel property-carousel-container" 
test2 = soup.find_all(class_="property-card-container horizontal property-listing-card")

name = test2[0].find('div', class_="property-name").get_text()
score = float(test2[0].find('div', class_="property-rating").find('span', class_='score').get_text())
reviews = test2[0].find('span', class_="num-reviews left-margin").get_text().replace('(','').replace(')','')
distance = test2[0].find('span', class_='distance-description').get_text().replace('- ','')
wifi = test2[0].find('div', class_='header-main').get_text()
private = test2[0].find_all('strong', class_="current")[0].get_text().replace('€','')
dorm = test2[0].find_all('strong', class_="current")[1].get_text().replace('€','')
print(
    'nome=',name,
    'score=',score,
    'reviews=',reviews,
    'distance=',distance,
    'wifi=',wifi,
    'private room=',private,
    'dorm=',dorm
)
# %%
df = pd.DataFrame(columns=('name','score','reviews','distance (km from center)','wifi','private room','dorm'))
hotel = soup.find_all(class_="property-card-container horizontal property-listing-card")
for i in range(len(hotel)):
    name = hotel[i].find('div', class_="property-name").get_text()
    score = float(hotel[i].find('div', class_="property-rating").find('span', class_='score').get_text())
    reviews = hotel[i].find('span', class_="num-reviews left-margin").get_text().replace('(','').replace(')','')
    distance = float(hotel[i].find('span', class_='distance-description').get_text().replace('- ','').replace('km from city centre',''))
    
    wifi_element = hotel[i].find('div', class_='tooltip-headers')
    if wifi_element:
        header_main_element = wifi_element.find('div', class_='header-main')
        wifi = header_main_element.get_text() if header_main_element else 'no'
    else:
        wifi = 'no'
    
    private = hotel[i].find_all('strong', class_="current")[0].get_text().replace('€','')
    dorm = hotel[i].find_all('strong', class_="current")[1].get_text().replace('€','')
    new_df = pd.DataFrame([{
                            'name':name,
                            'score':score,
                            'reviews':reviews,
                            'distance (km from center)':distance,
                            'wifi':wifi,
                            'private room':private,
                            'dorm':dorm}])
    df = pd.concat([df,new_df], ignore_index=True)
    
df
    


# %%
