import logging

from flask import Flask


app = Flask(__name__)
# app.register_blueprint(errors_bp)
app.logger.setLevel(logging.INFO)

from api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/admin")
def healthcheck():
    return "GOOD"
