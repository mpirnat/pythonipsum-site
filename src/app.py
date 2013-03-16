from flask import Flask, g, request, session, abort, \
        redirect, render_template, url_for
#from pythonipsum import get_paragraphs

import forms


app = Flask(__name__)

app.config.from_object('settings')
#app.config.from_object('pythonipsum.settings')
app.config.from_envvar('PYTHONIPSUM_SETTINGS', silent=True)


# TODO placeholder until the base lib has a decent setup.py
def get_paragraphs(number):
    return ['Blah blah.', 'Blah blah blah blah']


@app.route('/')
def homepage():
    form = forms.LoremIpsumForm(request.form or request.args)
    if not form.validate():
        abort(400)

    num_paragraphs = form.num_paragraphs.data or 1
    paragraphs = get_paragraphs(num_paragraphs)

    paragraph_options = range(1, 11)

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run()
