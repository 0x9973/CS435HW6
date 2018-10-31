from bs4 import BeautifulSoup
import requests
import os

base_url = "https://events.wm.edu/calendar/upcoming/wm"

html = requests.get(base_url).text
soup = BeautifulSoup(html, "lxml")

os.makedirs('./wm_events/', exist_ok=True)

upcoming_events = soup.find_all('div', {"id": "upcoming_events_grid"})

events = upcoming_events[0].find_all('div', {"class": "event_grid_item_container"})
# print(events)
# print(len(events))

for ul in events:
    imgs = ul.find_all('img')
    name = ul.find_all('span', {"class": "____"})

    for img in imgs:
        url = img['____']

    for n in name:
        filename = n.text

        # Titles containing / may cause file I/O error,
        # so replace "/" with ":"
        filename = filename.replace("/", ":")

    r = requests.get(url, stream=True)

    with open('./wm_events/%s' % filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)

    print('Saved %s' % filename)

