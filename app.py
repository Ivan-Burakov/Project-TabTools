from flask import Flask, render_template

app = Flask(__name__)


@app.route('/menu')
@app.route('/')
def menu_page():
    return render_template('menu.html')


@app.route('/tabs')
def tabs_page():
    return render_template('tabs.html')





if __name__ == '__main__':
    app.run(debug=True)