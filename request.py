import datetime
import json
import os

import requests
from notion_client import Client

from dtos import *

# declare today datetime before month
today = datetime.datetime.now()
beforeMonth = today.date() - datetime.timedelta(days=30)
afterWeek = today.date() + datetime.timedelta(days=14)

data = {"start_time": today, "end_time": afterWeek}
res = requests.post("https://jasoseol.com/employment/calendar_list.json", data=data)

# res to object
res = json.loads(res.text)["employment"]
jobs = []
job_group_filter = [164, 165, 166, 167, 170, 175, 176, 177, 178, 179, 180, 181, 182]
for job in res:
    j = Job(**job)
    employments = j.employments

    has_it = False
    for employment in employments:
        for duty in employment.duty_groups:
            if duty.group_id in job_group_filter:
                has_it = True
                break
        else:
            continue
        break
    if not has_it:
        continue

    # if j.employments
    jobs.append(j)

notion_api_token = os.environ["NOTION_TOKEN"]
notion_database_id = os.environ["NOTION_DB_ID"]
notion = Client(auth=notion_api_token)
query = notion.databases.query(notion_database_id)

# delete all notion pages
for page in query["results"]:
    notion.pages.update(page["id"], archived=True)

# create page
for job in jobs:
    page = notion.pages.create(
        parent={"database_id": notion_database_id},
        properties={
            "채용명": {"title": [{"text": {"content": job.title}}]},
            "기업": {"rich_text": [
                {
                    "text": {
                        "content": job.name,
                        "link": {
                            "url": f'https://jasoseol.com/recruit/{job.id}'
                        }
                    }
                }
            ]
            },
            "서류 일정": {"date": {"start": job.start_time, "end": job.end_time}},
            "마감일": {"date": {"start": job.end_time}},
            "자소설 닷컴 링크": {"url": f'https://jasoseol.com/recruit/{job.id}'},
        },
    )
