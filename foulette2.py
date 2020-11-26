#!/usr/bin/env python3

import sys
import requests
import json
import random
import os


# New version to do API calls to Yelp

# TODO: combine the 4 requests into one JSON, for cleaner code

# Use key.private for yelp API key

# Use + for space
foulette_location = "niles+il"
foulette_searchterm = "restaurants"

def main(argv):


    with open('key.private', 'r') as f:
        foulette_api_key = f.readline()

    yelp_headers = {
        'Authorization': f"Bearer {foulette_api_key}"
    }

    yelp_url1 = f"https://api.yelp.com/v3/businesses/search?term={foulette_searchterm}&location={foulette_location}&limit=50&radius=25000"
    yelp_url2 = f"https://api.yelp.com/v3/businesses/search?term={foulette_searchterm}&location={foulette_location}&limit=50&radius=25000&offset=50"
    yelp_url3 = f"https://api.yelp.com/v3/businesses/search?term={foulette_searchterm}&location={foulette_location}&limit=50&radius=25000&offset=100"
    yelp_url4 = f"https://api.yelp.com/v3/businesses/search?term={foulette_searchterm}&location={foulette_location}&limit=50&radius=25000&offset=150"

    yelp_get1 = requests.get(url=yelp_url1, headers=yelp_headers)
    yelp_get2 = requests.get(url=yelp_url2, headers=yelp_headers)
    yelp_get3 = requests.get(url=yelp_url3, headers=yelp_headers)
    yelp_get4 = requests.get(url=yelp_url4, headers=yelp_headers)

    json_yelp_get1 = json.loads(yelp_get1.text)
    json_yelp_get2 = json.loads(yelp_get2.text)
    json_yelp_get3 = json.loads(yelp_get3.text)
    json_yelp_get4 = json.loads(yelp_get4.text)
    

    rd = random.randint(0,49)
    rd_get = random.randint(1,4) # pick one of the four json_yelp_get variables

    # ["businesses"][rd]["name"] is within JSON (dict, list, dict)
    if rd_get == 1:
        your_pick = json_yelp_get1["businesses"][rd]["name"] + " in " + json_yelp_get1["businesses"][rd]["location"]["city"]
    elif rd_get == 2:
        your_pick = json_yelp_get2["businesses"][rd]["name"] + " in " + json_yelp_get1["businesses"][rd]["location"]["city"]   
    elif rd_get == 3:
        your_pick = json_yelp_get3["businesses"][rd]["name"] + " in " + json_yelp_get1["businesses"][rd]["location"]["city"]   
    elif rd_get == 4:
        your_pick = json_yelp_get4["businesses"][rd]["name"] + " in " + json_yelp_get1["businesses"][rd]["location"]["city"]   

    print (f'Your Pick is: \n{your_pick}')

    os.system("say \"" + your_pick + "\"") # " to surround text to ignore speical character issues



if __name__== "__main__":
    main(sys.argv[1:])




