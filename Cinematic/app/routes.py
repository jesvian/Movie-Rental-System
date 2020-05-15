from flask import render_template, flash, redirect, url_for, jsonify, request
from flask_login import current_user, login_user, logout_user
from wtforms.validators import email_validator
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, CreditCard, Cart
import json


@app.route('/')
@app.route('/movies')
def movies():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    return render_template('movies.html', movies=movies, query="")


@app.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    req = request.form
    movie_title = req.get("addToCart")
    for movie in movies['movies']:
        if movie['title'] == movie_title:
            movie_id = movie['id']
    user = str(current_user)
    user = user[6:len(user) - 1]
    user_id = User.query.filter_by(username=user).first()
    user_id = user_id.id
    purchase = Cart(user_id=user_id, movie_id=movie_id, total_cost=4.99)
    db.session.add(purchase)
    db.session.commit()
    flash('Item added to cart')
    return redirect(url_for('movies'))


@app.route('/movies/<movie_title>')
def get_movie(movie_title):
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    for movie in movies['movies']:
        if movie['title'] == movie_title:
            return_movie = movie
    return render_template('movie_result.html', movie=return_movie, title=movie_title)


@app.route('/movies/action')
def action():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    action_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Action':
                action_movies['movies'].append(movie)
    return render_template('movies.html', movies=action_movies, title='Action', query="")


@app.route('/movies/adventure')
def adventure():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    adventure_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Adventure':
                adventure_movies['movies'].append(movie)
    return render_template('movies.html', movies=adventure_movies, title='Adventure', query="")


@app.route('/movies/animation')
def animation():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    animation_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Animation':
                animation_movies['movies'].append(movie)
    return render_template('movies.html', movies=animation_movies, title='Animation', query="")


@app.route('/movies/comedy')
def comedy():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    comedy_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Comedy':
                comedy_movies['movies'].append(movie)
    return render_template('movies.html', movies=comedy_movies, title='Comedy', query="")


@app.route('/movies/crime')
def crime():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    crime_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Crime':
                crime_movies['movies'].append(movie)
    return render_template('movies.html', movies=crime_movies, title='Crime', query="")


@app.route('/movies/documentary')
def documentary():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    doc_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Documentary':
                doc_movies['movies'].append(movie)
    return render_template('movies.html', movies=doc_movies, title='Documentary', query="")


@app.route('/movies/drama')
def drama():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    drama_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Drama':
                drama_movies['movies'].append(movie)
    return render_template('movies.html', movies=drama_movies, title='Drama', query="")


@app.route('/movies/family')
def family():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    family_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Family':
                family_movies['movies'].append(movie)
    return render_template('movies.html', movies=family_movies, title='Family', query="")


@app.route('/movies/fantasy')
def fantasy():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    fantasy_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Fantasy':
                fantasy_movies['movies'].append(movie)
    return render_template('movies.html', movies=fantasy_movies, title='Fantasy', query="")


@app.route('/movies/history')
def history():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    history_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'History':
                history_movies['movies'].append(movie)
    return render_template('movies.html', movies=history_movies, title='History', query="")


@app.route('/movies/horror')
def horror():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    horror_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Horror':
                horror_movies['movies'].append(movie)
    return render_template('movies.html', movies=horror_movies, title='Horror', query="")


@app.route('/movies/music')
def music():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    music_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Music':
                music_movies['movies'].append(movie)
    return render_template('movies.html', movies=music_movies, title='Music', query="")


@app.route('/movies/mystery')
def mystery():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    mystery_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Mystery':
                mystery_movies['movies'].append(movie)
    return render_template('movies.html', movies=mystery_movies, title='Mystery', query="")


@app.route('/movies/romance')
def romance():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    romance_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Romance':
                romance_movies['movies'].append(movie)
    return render_template('movies.html', movies=romance_movies, title='Romance', query="")


@app.route('/movies/scifi')
def scifi():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    scifi_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Science Fiction':
                scifi_movies['movies'].append(movie)
    return render_template('movies.html', movies=scifi_movies, title='Science Fiction', query="")


@app.route('/movies/thriller')
def thriller():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    thriller_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Thriller':
                thriller_movies['movies'].append(movie)
    return render_template('movies.html', movies=thriller_movies, title='Thriller', query="")


@app.route('/movies/war')
def war():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    war_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'War':
                war_movies['movies'].append(movie)
    return render_template('movies.html', movies=war_movies, title='War', query="")


@app.route('/movies/western')
def western():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    western_movies = {'movies': []}
    for movie in movies['movies']:
        for genre in movie['genres']:
            if genre == 'Western':
                western_movies['movies'].append(movie)
    return render_template('movies.html', movies=western_movies, title='Western', query="")


@app.route('/checkout')
def checkout():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    user = str(current_user)
    user = user[6:len(user) - 1]
    user_id = User.query.filter_by(username=user).first()
    user_id = user_id.id
    cart = Cart.query.filter_by(user_id=user_id).all()
    _cart = []
    for item in cart:
        for movie in movies['movies']:
            if item.movie_id == movie['id']:
                _cart.append((movie['title'], item.movie_id, round(item.total_cost, 2)))
    return render_template('checkout.html', user=user, cart=_cart, cart_length=len(_cart))


@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
    user = str(current_user)
    user = user[6:len(user) - 1]
    user_id = User.query.filter_by(username=user).first()
    user_id = user_id.id
    cart = Cart.query.filter_by(user_id=user_id).all()
    for item in cart:
        db.session.delete(item)
        db.session.commit()
    return render_template('thank_you.html')


@app.route('/remove_item', methods=['GET', 'POST'])
def remove_item():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    req = request.form
    movie_to_remove = req.get("movie_id")
    user = str(current_user)
    user = user[6:len(user) - 1]
    user_id = User.query.filter_by(username=user).first()
    user_id = user_id.id
    cart = Cart.query.filter_by(user_id=user_id, movie_id=movie_to_remove).first()
    db.session.delete(cart)
    db.session.commit()
    flash('Item deleted')
    return redirect(url_for('checkout'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    req = request.form
    search_query = req.get("search")
    search_results = {'movies': []}
    with open('app/static/data/movies.json') as movies_file:
        movies = json.load(movies_file)
    for movie in movies['movies']:
        if movie['title'].lower() == search_query.lower() or search_query.lower() in movie['title'].lower():
            search_results['movies'].append(movie)
        if movie['cast'] is not None:
            for cast_member in movie['cast']:
                if cast_member.lower() == search_query.lower() or search_query.lower() in cast_member.lower():
                    search_results['movies'].append(movie)
        for genre in movie['genres']:
            if genre.lower() == search_query.lower() or search_query.lower() in genre.lower():
                search_results['movies'].append(movie)
    return render_template('movies.html', movies=search_results, query=search_query)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # print(current_user)
        return redirect(url_for('movies'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('movies'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        flash('You must be logged in to access this page')
        return redirect(url_for('login'))
    logout_user()
    return redirect(url_for('movies'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('movies'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, dob=form.dob.data)
        cc = CreditCard(owner=user, cc_number=form.cc_number.data, cc_company=form.cc_company.data, cc_expiration=form.expiration.data, cc_cvc=form.cvc.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.add(cc)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
