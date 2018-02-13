from apscheduler.schedulers.background import BackgroundScheduler
from tasks import dp_update, tax_letters, cl_tax_letter

sch = BackgroundScheduler()

def clear_tax_letters():
    cl_tax_letters.delay()

def push_dp_update():
    dp_update.delay()

def create_send_tax_letters():
    tax_letters.delay()
