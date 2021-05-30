import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.969670000000065&lon=-118.249935#.YLOxNagzbb0')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

period_names = [items.find(class_='period-name').get_text() for items in items]
short_descriptions = [items.find(class_='short-desc').get_text() for items in items]
temp = [items.find(class_='temp').get_text() for items in items]


weather_stuff = pd.DataFrame(
    {
        'period_names': period_names,
        'short_descriptions': short_descriptions,
        'temp': temp,
    })

print(weather_stuff)

print(weather_stuff.to_csv('result.csv'))