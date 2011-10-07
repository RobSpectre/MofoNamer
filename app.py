import os
from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index(page_title="Home"):
    return render_template('index.html', page_title=page_title)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # Disable in production
    app.debug = True
    app.run(host='0.0.0.0', port=port)
