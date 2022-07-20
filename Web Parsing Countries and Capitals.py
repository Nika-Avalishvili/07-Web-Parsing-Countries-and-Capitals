import requests
from bs4 import BeautifulSoup

resp = requests.get("https://geographyfieldwork.com/WorldCapitalCities.htm")
cont = resp.text

soup = BeautifulSoup(cont, "html.parser")
data = soup.find_all('td')

countries = []
cities = []

for index,i in enumerate(data,1):
    if index % 2 == 1:
        countries.append(i.text.capitalize())
    else:
        cities.append(i.text.capitalize())

new_dict = {}

for i in range(len(countries)):
    new_dict[countries[i]] = cities[i]



test = True

while test:
    try:
        user_input = input("Enter the country name: ")
        print(f"The capital of {user_input.capitalize()} is {new_dict[user_input.capitalize()]}!")
        test = False
    except:
        print(f"The county named {user_input} is not found!\n Please try again!" )
