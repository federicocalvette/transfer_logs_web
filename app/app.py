from flask import Flask, render_template, request, url_for, flash, redirect
import prometeo_request
import settings

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        date_start = request.form['date_start']
        date_end = request.form['date_end']

        if not date_start:
            flash('Date start is required!')
        elif not date_end:
            flash('Date end is required!')
        else:
            json_base = prometeo_request.get_transfer_logs(date_start, date_end)
            lista_pagos = json_base.get('result')

            return render_template('index.html', lista_pagos=lista_pagos, dates=f'{date_start} to {date_end}')

    return render_template('index.html')
