from flask import Flask
from routes import users
from dbase import db, login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/LR6'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(users)
if __name__ == "__main__":
    app.run(debug=True)
