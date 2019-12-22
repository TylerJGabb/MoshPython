import requests
import sys
try:
    from popular_python_packages.PyYelp import config
except ImportError as imp:
    sys.stderr.write(str(imp) + '\nconfig.py file was excluded from source to hide the API_KEY, you need to add this\n')
    exit(1)

if __name__ == '__main__':
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": "Bearer " + config.API_KEY
    }
    params = {
        "term": "barber",
        "location": "NYC"
    }

    response = requests.get(url, headers=headers, params=params)
    businesses = response.json()["businesses"]
    highly_rated = [b for b in businesses if b["rating"] >= 4]
    for b in businesses:
        print(f'{b["name"]} ({b["rating"]})')
