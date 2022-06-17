import requests
from datetime import datetime
import json

# Insert the Bearer_Token here. DO NOT commit it to keep it secret!
bearer_token = ""

# define api request function
def search_twitter(bearer_token = bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}

    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&{tweet_fields}&{expansion}&max_results=100"
    response = requests.request("GET", url, headers=headers)

    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

    return response.json()


# search term
game = "gta online"
query = f"({game}) lang:en -is:retweet -is:reply -is:quote -(twitch) -(youtube)"

# twitter fields to be returned by api call
tweet_fields = "tweet.fields=text,lang,created_at,public_metrics,geo,source"
expansion = "expansions=author_id&user.fields=name,username,location,protected,verified"

# twitter api call
json_response = search_twitter()

# save to json file
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
with open(f'api_responses/{timestamp}_{game}.json', 'w') as f:
    json.dump(json_response, f, indent=4, sort_keys=True)