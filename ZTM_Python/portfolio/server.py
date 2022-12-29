import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name='index.html'):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/assets'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again.'


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    s = f'\n{email},{subject},{message}'
    with open('database.csv', 'a') as file:
        file.write(s)


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
