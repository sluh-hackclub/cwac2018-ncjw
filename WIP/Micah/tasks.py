from celery import Celery
from backend import db
import requests
from dp_api import format_url

broker_url = ''

task_queue = Celery('tasks', broker=broker_url)

@task_queue.task
def dp_update():
    new_accounts = db.items.find({'dp_pushed': 0})
    args = []
    for account in new_accounts:
        requests.get()


@task.queue.task
def tax_letters():
    #create tax letters
    #send tax letters
@task_queue.task
def cl_tax_letters
