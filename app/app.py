from crypt import methods
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
import prometeo_request
import settings
import csv_generator

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        apikey = request.form['apikey']

        if not date_start:
            flash('Date start is required!')
        elif not date_end:
            flash('Date end is required!')
        elif not apikey:
            flash('API Key is required!')
        else:
            json_base = prometeo_request.get_transfer_logs(date_start, date_end, apikey)
            lista_pagos = json_base.get('result')
            csv_file_name = csv_generator.get_csv(lista_pagos)
            return render_template('index.html', lista_pagos=lista_pagos, dates=f'{date_start} to {date_end}', csv_name = csv_file_name)

    return render_template('index.html')

@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    directory = './download_file/'
    return send_from_directory(directory, filename)