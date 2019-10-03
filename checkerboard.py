from flask import Flask, render_template

app = Flask(__name__)
# 1. http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def checkerboard():
    num = int(8)
    return render_template('index.html', times=num, another=num, color1='black', color2='red')

# 2. http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:num>')
def numCheckerboard(num):
    return render_template('index.html', times=num, another=8, color1='black', color2='red')

# 3. http://localhost:5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<int:x>/<int:y>')
def choiceCheckerboard(x,y):
    return render_template('index.html', times=y, another=x, color1='black', color2='red')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def colorCheckerboard(x,y,color1,color2):
    return render_template('index.html', times=y, another=x, color1=color1, color2=color2)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
    # return 'This is a 404 Error! Please check the URL and try again.'




if __name__=="__main__":
    app.run(debug=True)