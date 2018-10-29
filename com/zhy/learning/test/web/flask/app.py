from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def home():
    return '<H1> HOME </H1>'



@app.route('/sign_in',methods=['GET'])
def sign_in_form():
    return '''<form action="/sign_in" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit"> Sign In</p>
              </form>      '''

@app.route('/sign_in',methods=['POST'])
def sign_in():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<H3> hello ,admin !</H3>'
    return '<H3> Bad Request !</H3>'


if __name__ == '__main__':
    app.run()

