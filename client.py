import requests


def get_content(tag):
    url="https://medium.com/tag/"+tag
    r=requests.get(url)
    print(r.status_code)
    print(r.url)
    print(r.content)
    return r

get_content("devops")
