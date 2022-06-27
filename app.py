from flask import Flask, render_template
import get_schedules
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/")
def home_page(name='Home'):
    return render_template('home.html', name=name)


@app.route("/browns")
def browns(name='Cleveland Browns'):
    games = get_schedules.get_browns_schedule(2022)
    return render_template('default_schedule.html', name=name, games=games)


@app.route("/indians")
def indians(name='Cleveland Indians'):
    games = get_schedules.get_indians_schedule(2022)
    return render_template('default_schedule.html', name=name, games=games)


@app.route("/buckeyes")
def buckeyes(name='The Ohio State Buckeyes'):
    games = get_schedules.get_buckeyes_schedule(2021)
    return render_template('default_schedule.html', name=name, games=games)
