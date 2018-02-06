import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--domain',
                    required=True,
                    help='The domain of the company')

parser.add_argument('--firstname',
                    required=True,
                    help='The firstname of the person')

parser.add_argument('--lastname',
                    required=True,
                    help='The lastname of the person')

parser.add_argument('--apikey',
                    required=True,
                    help='Your API key')

args = parser.parse_args()
url = "https://api.getemail.io/v1/find-mail"

querystring = {"firstname": args.firstname,
               "lastname": args.lastname,
               "domain": args.domain,
               "api_key": args.apikey
               }

headers = {
    'Cache-Control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
