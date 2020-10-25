#!/usr/bin/env python3

import sys
import requests
import json
import random
import os


# New version to do API calls to Yelp

foulette_api_key = "placeholder"
foulette_location = "chicago+il"


def main(argv):

    yelp_headers = {
        'Authorization': f"Bearer {foulette_api_key}"
    }

    yelp_url = f"https://api.yelp.com/v3/businesses/search?term=restaurants&location={foulette_location}&limit=50&radius=25000"

    yelp_get = requests.get(url=yelp_url, headers=yelp_headers)
    json_yelp_get = json.loads(yelp_get.text)
    
    rd = random.randint(0,49)
    your_pick = json_yelp_get["businesses"][rd]["name"]

    print (f'Your Pick is: \n{your_pick}')

    os.system("say \"" + your_pick + "\"") # " to surround text to ignore speical character issues



if __name__== "__main__":
    main(sys.argv[1:])




