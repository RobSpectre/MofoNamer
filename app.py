import os
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings import username, password

SEND_GRID = smtplib.SMTP('smtp.sendgrid.net', 587)
SEND_GRID.login(username, password)

def send_email(to, sender, description):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Example Python Email"
    msg['From'] = sender
    msg['To'] = to

    body = """
    Helllllloooooo!
    """

    body = MIMEText(html, 'html')
 
    # Attach parts into message container.
    msg.attach(part1)

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
