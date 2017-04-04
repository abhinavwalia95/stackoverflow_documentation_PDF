"""
Scrape http://stackoverflow.com/documentation and save targeted topics
to PDF in /pdf folder automatically.

WARNING: Use complete path of topics in config as in below sample python URL
URL = "http://stackoverflow.com/documentation/python/topics"

PDF is formatted and printable and you may use for reading purpose
instead of reading online.

NOTE: You may scrape desired documentation by changing specified URL in
/config.py and then magic happens! Wait for process to get finished and
print your PDFs from /pdf folder.

LOGGING: logger has been already implemented for logging, you may use
variable named as `logger` for your purpose.
"""
import logging
import requests
import pdfkit
from bs4 import BeautifulSoup
from config import LOG_FILE, LOG_FORMAT, URL, PDF_OPTIONS

logger = logging.getLogger("MAIN.PY")
handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter(LOG_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

all_topics = []
is_next = True
url = URL
options = PDF_OPTIONS

print "INITIATED"

while is_next:
    request = requests.get(url)
    data = request.text
    request.close()
    soup = BeautifulSoup(data, 'html.parser')
    topic = soup.find_all('div', {'class': 'topics'})[0]
    python_topics = topic.find_all('div', {'class': 'topic-row'})
    for each in python_topics:
        topic_url = each['data-topic-url']
        all_topics.append(topic_url)
    next_url_data = soup.find('a', {'rel': 'next'})

    if next_url_data:
        is_next = True
        url = "http://stackoverflow.com" + next_url_data['href']
    else:
        is_next = False

for each in all_topics:
    print "STARTED SCRAPING"
    name = each.split('/')[-1]
    request = requests.get(each)
    html = request.text
    request.close()
    soup_topic = BeautifulSoup(html, 'html.parser')
    try:
        for every in soup_topic.find_all('header'):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'docs-subheader subheader'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'sidebar'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'tabs'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'title-edit-container dno'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'menu-for-show'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'add-example-button-container'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'ask-question-prompt'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'edited-and-contributors'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'class': 'example-vote-controls'}):
            every.decompose()
        for every in soup_topic.find_all('div', {'id': 'footer'}):
            every.decompose()
        for every in soup_topic.find_all('code'):
            every.name = 'pre_code'
            every['style'] = "background: #eff0f1; "
        pdfkit.from_string(soup_topic.prettify(), 'pdf/' + name + '.pdf', options=options)
        print "Converted " + name + " to pdf"
    except:
        logger.error(name, exc_info=True)
