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
    places_required = int(request.form['places'])
    time_object = datetime.now()
    comp_time = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    # 2022-03-24 12:53:00.151212
    if time_object < comp_time:
        if (int(club['points']) <= places_required):
            if places_required <= 12 and places_required > 0:
                flash('Great-booking complete!' + str(places_required) + "spots booked for the " + str(competition))
                competition['numberOfPlaces'] -= places_required
                club['points'] -= places_required
            else:
                flash('You can book a maximum of 12 spots per comp')
        else:
            flash('Your club does not have enough points')
    else:
        flash("ERROR : you can t purchase places, it's a past competition")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/rankings', methods=['GET'])
def show_points():
    return (clubs, competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
