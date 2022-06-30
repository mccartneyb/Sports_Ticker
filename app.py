from flask import Flask, render_template
import get_schedules
app = Flask(__name__, static_url_path='/static')
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route("/", methods=['GET', 'POST'])
def home_page(name='Home'):
    return render_template('home.html', name=name)


@app.route("/browns")
def browns(name='Cleveland Browns'):
    year = 2022
    games = get_schedules.get_browns_schedule(year)
    return render_template('default_schedule.html', name=name, games=games, year=year)


@app.route("/indians")
def indians(name='Cleveland Indians'):
    year = 2022
    games = get_schedules.get_indians_schedule(year)
    return render_template('default_schedule.html', name=name, games=games, year=year)


@app.route("/buckeyes")
def buckeyes(name='The Ohio State Buckeyes'):
    year = 2021
    games = get_schedules.get_buckeyes_schedule(year)
    return render_template('default_schedule.html', name=name, games=games, year=year)


app.run(debug= True)