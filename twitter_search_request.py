import requests
import json

# Write the necessary tokens into the credentials.json file. DO NOT PUSH that file to GitHub
credentials = json.load(open('credentials.json'))
BEARER_TOKEN = credentials["Bearer Token"]


# define api request function
def search_twitter(query, tweet_fields, bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    response = requests.request("GET", url, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# search term
query = "gta online"

# twitter fields to be returned by api call
tweet_fields = "tweet.fields=text,author_id,created_at"

# twitter api call
json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)

# save to json file
with open('data.json', 'w') as f:
    json.dump(json_response, f, indent=4, sort_keys=True)