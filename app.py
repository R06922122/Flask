from flask import Flask

app = Flask(__name__) # __name__ means running model

@app.route("/") # Function Decorator -> provide extera usage, base on function below
def home():
    return "Hello Flask"

@app.route("/test") # Function Decorator -> provide extera usage, base on function below
def test():
    return "Hello Flask test"


if __name__ == "__main__": # if main function running 
    app.run() # run the server