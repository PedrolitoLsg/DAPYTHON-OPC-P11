import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

""" Private Functions """
def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'
clubs = load_clubs()
competitions = load_competitions()


if __name__ == '__main__':
    app.run(debug=True)


""" PUBLIC FUNCTIONS """


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


"""Allows connected to see it's club details(points) and future competitions"""
@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash('Email was not found. Please try again.')
        return render_template('index.html')


@app.route('/book/<competition>/<club>', methods=['GET'])
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club]
    found_competition = [c for c in competitions if c['name'] == competition]
    if found_club and found_competition:
        flash("Here is the form to complete")
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("The competition selected doesn't exists, Something went wrong-please try again")
        return render_template('welcome.html')


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    if datetime.now() < datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S"):
        if (int(club['points']) <= places_required) and (places_required <= 12):
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            #  deduct points from the team
            club['points'] -= places_required
            flash('Great-booking complete!')
        else:
            flash('Your club does  not have enough points, or you booked more than 12 spots')
    else:
        flash("ERROR : you can t purchase places, it's a past competition")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/rankings', methods=['GET'])
def show_points():
   return render_template('rankings.html', club=clubs)


@app.route('/logout')
def logout():
    flash('You disconnected')
    return redirect(url_for('index'))
