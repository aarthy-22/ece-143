import requests
import pandas as pd

def scrape_cwur(year,columns):
    if year > 2017:
        url = 'https://cwur.org/'+str(year)+'-'+str(year+1)[-2:]+'.php'
    else:
        url = 'https://cwur.org/'+str(year)+'.php'
    headers = {'user-agent': 'PostmanRuntime/7.28.4','Accept': '*/*'}
    res = requests.get(url, headers=headers)
    df = pd.read_html(res.content)
    df[0]['year'] = year
    df[0] = df[0].rename(columns={"World Rank": "world_rank", "Institution": "institution", "Country":"country", "Location":"country",  "National Rank":"national_rank", "Score":"score"})
    return df[0][columns]