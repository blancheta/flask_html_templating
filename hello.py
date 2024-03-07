from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    print("Passing by the view")
    name = "Tacos"

    # Could come from a database
    list_of_meals = [
        {"name": "French fries", "price": 10},
        {"name": "Burger", "price": 20},
        {"name": "Pizza", "price": 15}
    ]

    return render_template('home.html',
                           recipe_name=name, meals=list_of_meals)
