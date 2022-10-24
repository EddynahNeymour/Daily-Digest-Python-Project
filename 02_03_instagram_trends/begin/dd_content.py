from asyncio import events
import csv
import random
from urllib import request
import json
import datetime

import requests

"""
Retrieve a random quote from the specified CSV file.
"""
def get_random_quote(quotes_file='quotes.csv'):
    try: # load motivational quotes from csv file 
       with open(quotes_file) as csvfile:
           quotes = [{'author': line[0],
                      'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]

    except Exception as e: # use a default quote to help things turn out for the best
        quotes = [{'author': 'Jackie Kennedy',
                   'quote': 'Fashion fade, style is eternal.'}]
    
    return random.choice(quotes)

"""
Retrieve the current sale events from Chicmi Local Fashion.
"""
def get_sale_events(prams={'date_from': 2022/10/15, 'date_to': 2022/10/18}): # default location at London

    try: # retrieve event for specified coordinates
        url = "https://chicmi.p.rapidapi.com/calendar_in_city/"
        querystring = {"city":"london","days":"5","types":"brand-sales","max_results":"3"} 
        headers = {
	   "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	   "X-RapidAPI-Host": "chicmi.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        print(response.text)
        
        data = json.load(request.urlopen(url))

        events = {'city': data['city']['name'], # city name
                    'dates': list()} # list to hold event data for future datess

        for dates in data['list'][0:3]: # populate list with next 3 event dates 
            events['dates'].append({'timestamp': datetime.datetime.fromtimestamp(dates['dt']),
                                        'temp': round(dates['main']),
                                        'description': dates['sale'][0]['description'].title()})
        return events

    except Exception as e:
        print(e)     

def get_twitter_trends():
    pass

def get_skincare_article():
    pass

if __name__=='_main_':
    ##### test get_random_quote() #####
    print('\nTesting quote generation...')

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quotes_file = None)
    print(f' - Default quote is "{quote["quote"]}" - {quote["author"]}')

    ##### test get_sale_events() #####
    print('\nTesting sale events retrieval...')

    event = get_sale_events() # get events for default location
    if event:
        print(f'\nSale event for {event["city"]} is...')
        for dates in event['dates']:
            print(f' - {dates["sales"]} | {dates["description"]}')

    event = get_sale_events(prams={'date_from': 2022/10/20, 'date_to': 2022/10/22}) # get Manchester sale events
    if event:
        url = "https://chicmi.p.rapidapi.com/calendar_in_city/"
        querystring = {"city":"manchester","days":"3","max_results":"3"}
        headers = {
	   "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	   "X-RapidAPI-Host": "chicmi.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        
        print(response.text)
        
    invalid = {'date_from': 2022/10/13 ,'date_to': 2022/10/25} # invalid parameters
    event = get_sale_events(prams = invalid) # get event for invalid location
    if event is None:
        print('Sale event for invalid parameters returned None')