from flask import Flask

app=Flask(__name__)

@app.route('/')
def info():
    return "Salom Davronshox"

if __name__=="__main__":
    app.run()