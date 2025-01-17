from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def hello_world():
    
    todo=Todo(title="First Todo",desc="Start investing in Stock MArket")
    db.session.commit()
    db.session.add(todo)
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route('/show')
def products():
    allTodo=Todo.query.all()
    print(allTodo)
    return 'this id product page'

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()  # Create database tables
    app.run(debug=True, port=8000)
