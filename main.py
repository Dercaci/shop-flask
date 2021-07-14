from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    memory = db.Column(db.String(50))
    camera = db.Column(db.String(50))
    ram = db.Column(db.String(30))
    color = db.Column(db.String(30))
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.title

@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        memory = request.form['memory']
        camera = request.form['camera']
        ram = request.form['ram']
        color = request.form['color']


        item = Item(title=title, price=price, memory=memory, camera=camera, ram=ram, color=color)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except: 
            return "Input error"
    else:
        return render_template('create.html')


if __name__ =="__main__":
    app.run(debug=True)

