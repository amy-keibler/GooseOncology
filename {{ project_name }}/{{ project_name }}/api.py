from flask import Flask
from {{ project_name }}.lib import hello

app = Flask(__name__)

@app.route("/")
def hello_endpoint():
    return hello("{{ project_name }}")