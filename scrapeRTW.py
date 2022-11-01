from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup

import numpy as np

from time import sleep
from random import randint

import re

from events.models import Event


class Command(BaseCommand):
    help = "collect events from rigathisweek.lv"    # define logic of command

    def handle(self, *args, **options):
        months = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12,
        }

        # settings for URL request
        headers = {"Accept-Language": "en-US, en;q=0.5"}

        # creating the range to loop
        pages = np.arange(1, 2, 1)

        # creating the loop of the variable pages, each number is therefor represented by the page variable
        for page in pages:

            # URL is stored
            page = requests.get(
                "http://www.rigathisweek.lv/catalog/events?perpage=1&cdate=3&p=" + str(page), headers=headers)

            # convert to soup
            soup = BeautifulSoup(page.text, 'html.parser')

            # grab all postings
            allEvents = soup.find_all("div", class_="event-item")

            # setting a pause to not overwhelm the servers.
            sleep(randint(2, 10))

            # looping through every on the current page
            for event in allEvents:
                title = event.find('h3').text
                fullStartDate = None
                fullEndDate = None
                date = event.find('span', class_="calendar").text
                dateTime = event.find('span', class_="calendar")['content']
                checkDate = re.search("-", date)
                if checkDate:
                    dates = re.split(r"-\s", date)
                    start = dates[0]
                    end = dates[1]
                    splitStart = re.split(",", start)
                    splitEnd = re.split(",", end)
                    splitStart1 = splitStart[0]
                    splitEnd1 = splitEnd[0]
                    splitStart2 = re.split(r"\s", splitStart1)
                    splitEnd2 = re.split(r"\s", splitEnd1)
                    fullStartDate = "2022-" + \
                        str(months[splitStart2[0]]) + "-" + str(splitStart2[1])
                    fullEndDate = "2022-" + \
                        str(months[splitEnd2[0]]) + "-" + str(splitEnd2[1])
                elif dateTime[-1] == 'T':
                    fullStartDate = dateTime[:-1]
                elif dateTime[-6] == 'T':
                    fullStartDate = dateTime[:-6]

                url = event.find('a')['href']
                fullURL = 'http://www.rigathisweek.lv' + url

                try:
                    # save in db
                    Event.objects.create(
                        title=title,
                        startDate=fullStartDate,
                        endDate=fullEndDate,
                        link=fullURL,
                        status='Publish',
                    )
                    print('%s added' % (title,))
                except:
                    print('Something wrong happened or %s already exists' % (title,))

        self.stdout.write('job complete')
