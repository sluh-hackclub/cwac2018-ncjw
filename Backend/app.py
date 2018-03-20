from flask import Flask, make_response, jsonify, make_response
import boto3

app = Flask(__name__)

s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

donor_list = [
                {'name':'Micah', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'Dan', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'Nina', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'Naomi', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'John Smith', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'Tyrell Williams', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'Lynda Smith', 'id':'1234', 'address':'1545 Legacy Circle'},
                {'name':'John Adams', 'id':'1234', 'address':'1545 Legacy Circle'},
            ]
# donors = sorted(donors_unorderd, key=lambda x: x['name'])
category_list = [
                    {'parent_id': '0', 'id': '1', 'category': 'shirts'},
                    {'parent_id': '0', 'id': '2', 'category': 'pants'},
                    {'parent_id': '0', 'id': '3', 'category': 'hats'},
                    {'parent_id': '1', 'id': '4', 'category': 'longsleeve'},
                    {'parent_id': '1', 'id': '5', 'category': 'shortsleeve'},
                    {'parent_id': '1', 'id': '6', 'category': 'tanktop'},
                    {'parent_id': '4', 'id': '7', 'category': 'mens'},
                    {'parent_id': '4', 'id': '8', 'category': 'womens'},
                    {'parent_id': '4', 'id': '9', 'category': 'kids'}
                ]


def find_items(search_list, key, value):
    searched_items = []
    for item in search_list:
        if value in item[key]:
            searched_items.append(item)
        else:
            pass
    return searched_items


@app.route('/get_donors/<donor_name>')
def index(donor_name):
    donors = find_items(donor_list, 'name', donor_name)
    resp = make_response(jsonify(donors=donors))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/get_categories/<parent_id>')
def get_categories(parent_id):
    categories = find_items(category_list, 'parent_id', parent_id)
    resp = make_response(jsonify(categories=categories))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/get_tax_letter_url/<donor_id>')
def get_tax_letter_url(donor_id):
    url = s3.generate_presigned_url(ClientMethod='get_object', Params={'Bucket':'taxletters2', 'Key':donor_id + '.pdf'})
    resp = make_response(url)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.run()
