import os

from flask import Flask, render_template
from database import db, User, get_joyful_users, get_all_users, get_unjoyful_users
from data_insertion import insert_data

app = Flask(__name__)

# Use environment variables for database connection
db_username = os.environ.get('DB_USERNAME', 'postgres')
db_password = os.environ.get('DB_PASSWORD', 'secretpassword')
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME', 'postgres')

# Construct the database connection string
db_uri = f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_app():
    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_data()

    @app.route('/')
    def hello_world():
        all_users = get_all_users()
        joyful_users = get_joyful_users()
        unjoyful_users = get_unjoyful_users()
        return render_template('index.html', joyful_users=joyful_users, unjoyful_users=unjoyful_users, all_users=all_users)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
