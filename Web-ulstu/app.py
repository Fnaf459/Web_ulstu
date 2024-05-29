from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/login', methods=['POST'])
def login():
    phone = request.form['phone']
    password = request.form['password']
    return render_template('index.html', message="Вы успешно вошли!")

if __name__ == '__main__':
    app.run(debug=True)
