from flask import Flask
app=Flask(__name__)


def add(a,b):
    return a+b 

def subtract(a,b):
    return a-b

#print(add(2,3))
#print(subtract(5,7))
@app.route("/")
def home():
    return "Hello, this is my sample app for pipeline testing"
@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return str(add(a, b))

@app.route("/subtract/<int:a>/<int:b>")
def subtract_route(a, b):
    return str(subtract(a, b))

if __name__ == "__main__":
    app.run(debug=True)







#ci cd automatic trigger test
