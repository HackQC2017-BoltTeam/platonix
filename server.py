import os
import tempfile

from flask import Flask
from flask import jsonify
from flask import request
from openalpr import Alpr

app = Flask(__name__)

FLASK_DEBUG = os.environ.get('FLASK_DEBUG', False)

SUPPORTED_EXTENSIONS = ('.png', '.jpg', '.jpeg')

ALPR_CONFIG_FILE = '/usr/share/openalpr/config/openalpr.defaults.conf'
COUNTRY = 'us'
DATA_DIR = '/srv/openalpr/runtime_data/'
ALPR_N_BEST = 10


def allowed_file(filename):
    return filename.lower().endswith(SUPPORTED_EXTENSIONS)


@app.route("/ping")
def ping():
    return "pong"


@app.route('/photo', methods=['POST'])
def upload():

    file = request.files['file']

    if file and allowed_file(file.filename):

        with tempfile.NamedTemporaryFile() as temp_file,\
             Alpr(COUNTRY, ALPR_CONFIG_FILE, DATA_DIR) as alpr:

            if not alpr.is_loaded():
                return('Failed to initialize OpenALPR', 500)
            else:
                alpr.set_top_n(ALPR_N_BEST)

            file.save(temp_file)
            results = alpr.recognize_file(temp_file.name)

        return jsonify(results)


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, host='0.0.0.0', port=5000)
