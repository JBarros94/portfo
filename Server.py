import csv
from flask import Flask, render_template, request, redirect

def write_to_file(data):
    with open('DataBase.txt', mode='a') as database:
        file = database.write(f'\n{data["email"]}, {data["subject"]}, {data["message"]}')

def write_to_csv(data):
    with open('DataBase.csv', newline='', mode='a') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong. Please try again.'