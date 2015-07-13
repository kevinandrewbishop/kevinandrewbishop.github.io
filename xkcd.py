import requests as r

responses = []
for i in range(1, 1546):
    if i%10 == 0:
        print(i)
    response = r.get('http://xkcd.com/%s/info.0.json' %i)
    responses.append(response.json())



