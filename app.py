# get html templates from templates folder and show them on the browser

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# Path: simple-webapp1/templates/home.html