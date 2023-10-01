from flask import Flask
from flask import render_template, request
# from flask_babel import Babel

app = Flask(__name__, template_folder='template')

app.config['DEBUG'] = True
# app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config['LANGUAGES'] = {
#                             'en': _('English'),
#                             'fr': _('French')
#                         }

# babel = Babel(app=app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8085)