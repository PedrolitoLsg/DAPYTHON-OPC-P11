import json
from flask import Flask, render_template, request, redirect, flash, url_for
import datetime as dt


def load_clubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def load_competitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'
competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """Allows connected to see it's club details(points) and future competitions"""
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash('Email was not found. Please try again.')
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("The competition selected doesn't exists, Something went wrong-please try again")
        return render_template('welcome.html')


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places']
    current_date = dt.datetime.now()
    if current_date > competition['date']:
        if (club['points'] <= places_required) and (places_required <= 12):
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            # deduct points from the team
            club['points'] -= places_required
            flash('Great-booking complete!')
        else:
            flash('Your club does  not have enough points, or you booked more than 12 spots')
    else:
        flash('It is too late to register to this competitions')
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/rankings', methods=['GET'])
def show_points():
    return (clubs, competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
