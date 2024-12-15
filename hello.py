from flask import Flask
app = Flask(__name__)


@app.route('/')
def Hello():
    # run automatically
    return "<h1> Hello There.!! </h1>" 

@app.route('/ping')
def ping():
    return {"Message": "Why are you Pinning ME?"}