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


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions = ['инженер-исследователь', 'пилот', 'строитель',
                   'врач', 'инженер по жизнеобеспечению'
        , 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(port=8080)
