from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator


@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        pass
    return render_template('interest_form.html', calc_total=True)


@app.route('/time', methods=['POST', 'GET'])
def time_interest():
    pass


@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html')
