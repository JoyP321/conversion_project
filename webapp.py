from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1") #annotations tell which function go with which request
def render_page1():
    meters = float(request.args['input'])
    unit = request.args['newUnit']
    if unit == "centimeters" :
        toReturn = meters*100.0
    if unit == "inches" :
        toReturn = meters*39.3701
    if unit == "feet" :
        toReturn = meters*3.28084
    return render_template('page1.html', responseFromServer =  toReturn)

@app.route("/response")
def render_response():
    meters = float(request.args['input'])
    unit = request.args['newUnit']
    if unit == "centimeters" :
        toReturn = meters*100.0
    if unit == "inches" :
        toReturn = meters*39.3701
    if unit == "feet" :
        toReturn = meters*3.28084
    return render_template('response.html', responseFromServer = toReturn)

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

if __name__=="__main__":
    app.run(debug=False)
