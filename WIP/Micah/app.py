from flask import Flask, session, redirect, request, render_template, url_for, jsonify
from functools import wraps
from flask_session import Session
from secrets import token_hex
# from scheduler import sch
from datetime import datetime
from backend import client, db
import requests
from wasabi import wasabi_base_url
app = Flask(__name__)
app.secret_key = token_hex(16)

app.config['SESSION_TYPE'] = 'mongodb'
app.config['SESSION_MONGODB'] = client
app.config['SESSION_MONGODB_DB'] = 'ncjw-rs'
app.config['SESSION_MONGODB_COLLECT'] = 'sessions'
Session(app)

#########################
context = ('cert.pem', 'key.pem')
#########################
#register scheduler, scheduler with initiate celery tasks, clearing tax letters at the end of every year
# sch.start()
# job0 = sch.add_job(clear_tax_letters, 'cron', year='*', month='feb', day=2, hour=1, minute=0, second=0)
# job1 = sch.add_job(create_send_tax_letters, 'cron', year="*", month='jan', day=1, hour=1, minute=0, second=0)
# job2 = sch.add_job(push_dp_update, 'cron', year='*', month='*', day='*', week='*', day_of_week='*', hour=8, minute=0, second=0)

#########################
#register scheduler for celery task to upload info to Donor Perfect

def protected(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        redirect_url = request.url if '/api/v1' not in request.url else url_for('index')
        if 'username' not in session:
            return redirect(url_for('login', redirect=redirect_url))
        else:
            return function(*args, **kwargs)
    return wrapper

@app.route('/api/v1/authenticate', methods=['GET','POST'])
def authenticate():
    credentials = request.get_json()
    username = credentials['user']
    url = request.args.get('redirect') if 'redirect' in request.args else url_for('index')
    if db.users.find_one({'username':username,'password':credentials['pass']}):
        session['username'] = username
        return url
    else:
        return url_for('login', redirect=url)
    #check username and password are in the database


@app.route('/api/v1/taxletter/<dp_id>/<year>')
@protected
def taxletter(dp_id, year):
    tax_letter_url = wasabi_base_url + '/' + dp_id + '/' + year + '/' + 'taxletter.pdf'
    user_name = db.users.find_one({'dp_id': dp_id})['name']
    tax_letter_data = {'url':tax_letter_url, 'name':user_name, 'year':year}
    return jsonify(tax_letter_data)
    #query object storage using id and year
    #return json object of doc name, year, sent via email?, and link to object

@app.route('/api/v1/createitem', methods=['GET', 'POST'])
@protected
def create_item_api():
    new_item_data = request.get_json()
    db.items.insert({key:new_item_data[key] for key in new_item_data})
    return redirect(url_for('index'))

@app.route('/api/v1/itemize/<click_id>')
@protected
def itemize(click_id):
    category_data = list(db.categories.find({'parent_id':click_id}))
    if category_data:
        return jsonify(category_data)
    else:
        return redirect(url_for('view_items') + '/' + click_id)
#the click id is the object id of the item that was clicked on. the click id is stored as an html attribute
#click id of base categories is 0

@app.route('/api/v1/finduser/<user_name>')
@protected
def find_user(user_name):
    user_data = list(db.users.find({'name': user_name}))
    return jsonify(user_data)

@app.route('/api/v1/registerdonor', methods=['GET', 'POST'])
def register_donor_api():
    data = request.get_json()
    redirect(url_for('select_receipt'), pn=data['phone_number'])
    #will have receipt options

@app.route('/api/v1/verifydonor', methods=['GET', 'POST'])
def verify_donor_api():
    data = request.get_json()
    redirect(url_for('select_receipt'), pn=data['phone_number'])
################################################################################

@app.route('/createitem/<dp_id')
@protected
def create_item(dp_id):
    return render_template('createitem.html')
    #javascript will get dp_id from the url
    #page with user and buttons to add items
    #code to add new item

@app.route('/stafflogin')
def login():
    return render_template('login.html')

@app.route('/viewtaxletters')
# @protected
def view_tax_letter():
    return render_template('viewtaxletters.html')

@app.route('/registerdonor')
def register_donor():
    return render_template('registerdonor.html')
    #auto add user to dp to get dp_id

@app.route('/verifydonor')
def verify_donor():
    return render_template('verifydonor.html')

@app.route('/selectreceipt', methods=['POST', 'GET'])
def select_receipt():
    phone_number = request.args.get('pn')
    receipt_status = request.form['receipt_status']
    if db.users.find({'phone_number':phone_number})['receipt'] == 1:
        redirect(url_for('verify_donor'))
    else:
        db.users.update({'phone_number':phone_number}, {'receipt_status':receipt_status})
        redirect(url_for('verify_donor'))

@app.route('/')
@protected
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    if username in session:
        session.pop('username', None)
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(port=443, ssl_context=context)
