from flask import Flask, render_template, session, redirect, url_for, request
from random import randint

app = Flask(__name__)
app.secret_key = "coolio"

@app.route('/')
def index():
    if "act_log" not in session:
        session["act_log"] = []
    return render_template("index.html", act_log=session["act_log"], current_gold=get_current_gold()) #this route is already processing and updating the money#

@app.route('/test', methods=['POST']) #was not working at first so I implemented this as a test#
def test():
    return "Test route is working!"

@app.route('/farm', methods=['POST'])
def farm():
    gold_earned = randint(10, 20)
    session["act_log"].append(f"You have earned {gold_earned}!")
    update_gold(gold_earned)
    print(f"Current Gold: {get_current_gold()}")
    return redirect(url_for("index"))

@app.route('/cave', methods = ['POST'])
def cave():
    gold_earned = randint(10, 20)
    session["act_log"].append(f"You have earned {gold_earned}!")
    update_gold(gold_earned)
    print(f"Current Gold: {get_current_gold()}")
    return redirect(url_for("index"))

@app.route('/house', methods = ['POST'])
def house():
    gold_earned = randint(2, 5)
    session["act_log"].append(f"You have earned {gold_earned}!")
    update_gold(gold_earned)
    print(f"Current Gold: {get_current_gold()}")
    return redirect(url_for("index"))

@app.route('/casino', methods = ['POST'])
def casino():
    gold_earned = randint(0, 50)
    if randint(0, 1) == 0:  # 50% chance to lose the gold
        gold_earned *= -1
        session["act_log"].append(f"You have lost {abs(gold_earned)} gold in the casino!")
    else:
        session["act_log"].append(f"You have earned {gold_earned} gold in the casino!")
    update_gold(gold_earned)
    return redirect(url_for("index"))

def get_current_gold():
    return session.get('gold_update', 0)

def update_gold(amount):
    current_gold = get_current_gold()
    updated_gold = current_gold + amount
    session['gold_update'] = updated_gold
    print(f"Updated Gold: {updated_gold}")

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
