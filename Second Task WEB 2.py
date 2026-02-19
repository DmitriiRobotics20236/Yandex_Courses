from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    t = request.args.get('title', 'Главная страница')
    return render_template('base.html', title=t)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', profession=prof)

if __name__ == '__main__':
    app.run(port=8080)