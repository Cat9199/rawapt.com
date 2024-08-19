from flask import Flask , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Links(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      goto = db.Column(db.String(200), nullable=False)
      unique = db.Column(db.String(200), nullable=False)
      Visit = db.Column(db.Integer, nullable=False)


@app.route('/<string:unique>')
def goto(unique):
      link = Links.query.filter_by(unique=unique).first()
      if link:
            link.Visit = link.Visit + 1
            db.session.commit()
            return render_template('goto.html', link=link)
            
      else:
            return 'Link not found'

if __name__ == '__main__':
      with app.app_context():
            db.create_all()
      app.run(debug=True)