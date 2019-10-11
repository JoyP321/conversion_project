from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1") #annotations tell which function go with which request
def render_page1():
    meters = request.args['input']
    unit = request.args['newUnit']
    if unit == "centimeters" :
        toReturn = meters*100.0
    if unit == "inches" :
        toReturn = meters*39.3701
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

if __name__=="__main__":
    app.run(debug=False)
