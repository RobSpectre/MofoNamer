import os
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('registered'))
    return render_template('signup.html', form=form)

@app.route('/registered')
def registered():
    return render_template('complete.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
