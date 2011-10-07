import os
import smtplib
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
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

    SEND_GRID.sendmail(sender, to, msg.as_string())


app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index(page_title="Home"):
    if request.method == 'POST': 
        flash('Thanks for registering')
        send_email("kyle.j.conroy@gmail.com", "kyle@twilio.com", 3)
        return redirect(url_for('registered'))
    return render_template('index.html', page_title=page_title)


@app.route('/registered')
def registered():
    return render_template('complete.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
