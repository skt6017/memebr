from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    mbti = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    pros = db.Column(db.String, nullable=False)
    work_style = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    blog_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.role}'

@app.route('/')
def show_members():
    members = Member.query.all()
    return render_template('index.html', data=members)

if __name__ == '__main__':
    app.run(debug=True)