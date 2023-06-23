from flask import Flask, render_template, request, redirect, url_for,flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from teaminfo import getTeamInfo
from squad import getSquad
from coach import getCoach, getCoachByTeam


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'] or ' '
        password = request.form['password'] or ' '

        user = User.query.filter_by(username=username).first()
        if username==' ' or password==' ':
            return 'Empty username or password.'
        elif not user or not check_password_hash(user.password, password):
            return 'Invalid username or password.'
        else:
            session['username'] = username
        login_user(user, remember=True)
        return redirect(url_for('getleague'))
    else:
        if not current_user.is_authenticated:
            return render_template('login.html')
        else:
            return redirect(url_for('getleague'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()


        if username == '' or password == '':
            return 'Empty username or password.'
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return 'Username already exists'

        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    else:
        session.clear()

        return render_template('signup.html')

    


@app.route('/getleague',methods=["GET"])
@login_required
def getleague():
    flash(f"Hello {current_user.username}! This is a flash message.")
    return render_template('getleague.html')


@app.route('/team')
def team():
    teamID = request.args.get('teamID')
    teamresponse=getTeamInfo(teamID)
    return render_template('team.html', teamresponse=teamresponse)


@app.route('/league')
def league():
    league_id = request.args.get('leagueid')
    season = request.args.get('season')
    return render_template('league.html', league_id=league_id, season=season)


@app.route('/logout')
def logout():
    logout_user()
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/squad')
def squad():
    teamID=request.args.get("teamID")
    squad=getSquad(teamID)
    coach=getCoachByTeam(teamID)    
    return render_template("squad.html",squad=squad,coach=coach)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
