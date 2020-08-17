from flask import *

app = Flask(__name__)
app.secret_key = 'vhg'

@app.route('/')
def default():
    return render_template('Register.html')

@app.route('/Register.html',methods=["POST"])
def register_data():
    firstname=request.form['rfn']
    lastname=request.form['rln']
    username=request.form['run']
    password=request.form['rpw']

    session['session_fn']=firstname
    session['session_ln']=lastname
    session['session_un']=username
    session['session_pw']=password
    return render_template('Login.html')

@app.route('/Login.html',methods=["POST"])
def login_data():
    lun=request.form['lun']
    lpw=request.form['lpw']

    session_fn=session['session_fn']
    session_ln=session['session_ln']
    session_un=session['session_un']
    session_pw=session['session_pw']

    if lun==session_un:
        if lpw== session_pw:
            return render_template('Home.html' ,fn=session_fn,ln=session_ln)
        else:
            return render_template('Login.html',msg=flash('You Username & Password Incorrect'))
    else:
        return render_template('Login.html',msg=flash('You Username & Password Incorrect'))
app.run(threded=True)
