from flask import Flask
from flask import g, make_response, redirect, render_template, request, url_for
from flask_babel import Babel
from flask_babel import refresh, gettext as _


app = Flask(__name__, template_folder='template')

app.config['DEBUG'] = True
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = {
                            'en': _('English'),
                            'es': _('Spanish'),
                            'fr': _('French'),
                            'hi': _('Hindi')
                        }

def get_locale():
    user_language = getattr(g, 'user_language', None)

    if user_language:
        return user_language
        
    return request.accept_languages.best_match(
            app.config['LANGUAGES'].keys()
        )
                
babel = Babel(app=app, locale_selector=get_locale)

@app.before_request
def before_request():
    # Set the language based on user preferences (from cookies, for example)
    user_language = request.cookies.get('language', None)

    if user_language in app.config['LANGUAGES']:
        g.user_language = user_language
        refresh()  # Refresh translations for the selected language
    else:
        # If no language is set, use the default language
        g.user_language = 'en'
        refresh()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/change-language/<string:language>')
def change_language(language):

    if language in app.config['LANGUAGES']:
        response = make_response(redirect(request.referrer))
        response.set_cookie('language', language)
        return response

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()