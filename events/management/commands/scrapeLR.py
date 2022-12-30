from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date
import numpy as np
from time import sleep
from random import randint
import re

from events.models import Event


class Command(BaseCommand):
    help = "collect events from liveriga.com"
    # define logic of command

    def handle(self, *args, **options):
        months = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,
        }

        # settings for URL request
        headers = {"Accept-Language": "en-US, en;q=0.5"}

        # creating the range to loop
        pages = np.arange(1, 5, 1)

        # creating the loop of the variable pages, each number is therefor represented by the page variable
        for page in pages:

            # URL is stored
            page = requests.get(
                "https://liveriga.com/en/visit/events?page=" + str(page), headers=headers)

            # convert to soup
            soup = BeautifulSoup(page.text, 'html.parser')

            # grab all postings
            postings = soup.find_all("div", class_="col mb-3 mb-md-5")

            # setting a pause to not overwhelm the servers.
            sleep(randint(2, 10))

            # looping through every on the current page
            for p in postings:
                url = p.find('a', class_='card')['href']
                fullURL = 'https://liveriga.com' + url
                title = p.find('h3').text
                startDate = p.find(class_="d-none d-md-block").text
                date_day = re.findall(r"\d{1,2}", startDate)
                date_month = re.findall(r"[A-Za-z]{3}", startDate)
                start_day = str(date_day[0])
                start_month = str(months[date_month[0]])
                currentDate = datetime.date.today()
                fullStartDate = str(currentDate.year) + "-" + start_month + "-" + start_day

                if len(date_day) >= 2:
                    end_day = str(date_day[1])
                    end_month = str(months[date_month[1]])
                    fullEndDate = str(currentDate.year) + "-" + str(end_month) + "-" + str(end_day)

                    if int(end_month) < int(start_month):
                        fullEndDate = str(date.today().year + 1) + "-" + str(end_month) + "-" + str(end_day)
                    else:
                        pass

                else:
                    if int(start_month) < int(date.today().month - 1):
                        fullStartDate = str(date.today().year + 1) + "-" + str(start_month) + "-" + str(start_day)
                        fullEndDate = str(date.today().year + 1) + "-" + str(end_month) + "-" + str(end_day)

                    else:
                        fullEndDate = fullStartDate
                
                # print(title + ' ' + fullStartDate + ' ' + fullEndDate)

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
