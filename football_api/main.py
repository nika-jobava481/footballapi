from flask import Flask, render_template, request, redirect, url_for,flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


"""
აქ ხელითაა მიცემული სეზონი და ლიგა
რეალურად გვინდა ის რასაც მომხმარებელი მონიშნავს
მერე მანდედან ვიღებთ teamid-ს რომელიც გვჭირდება
lineup-ისა და მწვრთნელის გამოსატანად
მაგრამ აქ ერთი პრობლემაა ამას სჭირდება ორი პარამეტრი
teamid რომელიც წამოღებულია ქვევით ეიპიაიში და fixtures
ეს ვერსად ვერ ვნახე
"""
import requests
import json

# url = "https://api-football-v1.p.rapidapi.com/v3/standings"

# querystring = {"season": "2021", "league": "78"}

# headers = {
#     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
#     "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

# response = requests.request("GET", url, headers=headers, params=querystring)

# result_json = response.text
# res = json.loads(result_json)
# res = response.json()['response'][0]['league']['standings'][0]
# res_structured = json.dumps(res, indent=4)


# team_id = []
# for i in range(len(res)):
#     team_info = res[i]
#     team_id.append(team_info['team']['id'])



"""
ესაა ლაინაფი და აქაა პირველი პარამეტრის პრობლემა
"""
# url2 = "https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups"
# querystring2 = {"fixture": "215662", "team": "463"}

# headers2 = {
#     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
#     "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

# response2 = requests.request("GET", url, headers=headers2, params=querystring2)


# result_json2 = response.text
# res2 = json.loads(result_json)
# res2 = response.json()['response']
# res_structured2 = json.dumps(res, indent=4)
# print(res_structured)


# team_name = res[0]['team']['name']
# team_logo = res[0]['team']['logo']
# coach = res[0]['coach']['name']
# coach_photo = res[0]['coach']['photo']
# start_11 = res[0]['startXI']
# print(team_name, team_logo,coach,coach_photo)


# for i in range(len(start_11)):
#     player_id = start_11[0]['player']['id']
#     playar_name = start_11[0]['player']['name']
#     playar_number = start_11[0]['player']['number']
#     playar_position = start_11[0]['player']['pos']
#     print(player_id, playar_name, playar_number, playar_position)

"""
ახლა დავწერ მოთამაშეების ინფორმაციას რომლისთვისაც 
პარამეტრები არის გუნდის აიდი და სეზონი
მოაქვს 20 მოთამაშე მარა ჩვენ გვინდა კონკრეტული 11
მოთამაშეების კოდი რომელსაც წინა ეიპიაიდან წამოვიღებთ
უბრალოდ ჩემი შესაძლებლობები ვეღარ წვდება დანარჩენს
თორემ ვიზამდი აუცილებლად
"""

# url1 = "https://api-football-v1.p.rapidapi.com/v3/players"

# querystring1 = {"team":"33", "season":"2020"}

# headers1 = {
#     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
#     "X-RapidAPI-Key": "68cd65fa40mshd0152fc63f9e5fep151d51jsn9ca3f6ffeb04"}

# response1 = requests.request("GET", url, headers=headers1, params=querystring1)


# result_json1 = response.text
# res1 = json.loads(result_json)
# res1 = response.json()['response']
# res_structured1 = json.dumps(res, indent=4)
# print(res_structured)

# for i in range(len(res)):
#     player_id = res[i]['player']['id']
#     name = res[i]['player']['name']
#     age = res[i]['player']['age']
#     birthday = res[i]['player']['birth']['date']
#     country = res[i]['player']['birth']['country']
#     heigth = res[i]['player']['height']
#     weight = res[i]['player']['weight']
#     photo = res[i]['player']['photo']
#     print(f"player id: {player_id}, name: {name}, age: {age}, birthday: {birthday}, ", f"country: {country}, heigth: {heigth}, weight: {weight},", f"photo: {photo}")








@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password.')
        else:
            session['username'] = username
        login_user(user, remember=True)
        return redirect(url_for('getleague'))
    else:
        if not current_user.is_authenticated:
            return render_template('login.html')
        else:
            return render_template('getleague.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        # Perform validation (you can customize this based on your requirements)
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('signup'))
        elif username == '' or password == '':
            flash("Fill in all blanks!")
            return redirect(url_for('signup'))

        # Check if the username already exists in the database

        else:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
        
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

    


@app.route('/getleague',methods=["GET"])
@login_required
def getleague():
    return render_template('getleague.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/league')
def league():
    return render_template('league.html')

@app.route('/logout')
def logout():
    # Log out the user
    logout_user()
    return 'Logged out successfully.'




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
