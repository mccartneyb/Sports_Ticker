from flask import Flask, render_template
import get_schedules
app = Flask(__name__)

@app.route("/")
def home_page(name='Home'):
    return render_template('home.html', name=name)

@app.route("/browns")
def browns(name='Cleveland Browns'):
    return f"<p>{get_schedules.get_browns_schedule(2022)}</p>"

@app.route("/indians")
def indians(name='Cleveland Indians'):
    return f"<p>{get_schedules.get_indians_schedule(2022)}</p>"

@app.route("/buckeyes")
def buckeyes(name='The Ohio State Buckeyes'):
    return f"<p>{get_schedules.get_buckeyes_schedule(2021)}</p>"