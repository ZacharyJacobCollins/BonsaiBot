from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/time')
def time():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Anyone got the time?', 
        'time' : timeString
    }
    return render_template('time.html', **templateData)

@app.route('/light/on')
def light():
    return 'light is on'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

