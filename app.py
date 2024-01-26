from flask import Flask

app=Flask(__name__)

@app.route('/')
def info():
    return "Salom Davronshox"
@app.route('/davron')
def about():
    return "My name is Davron,My lastname is Do'stqobilov.\nI am 20 years old. I study in SamTATU"
if __name__=="__main__":
    app.run()