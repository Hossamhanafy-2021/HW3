from flask import Flask, render_template, request, redirect, url_for
# Initialize the Flask application
app = Flask(__name__)
 
@app.route('/')
def index():
   return render_template('index.html')
    
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['TxtName'] == 'hossamhanafy@gmail.com' and request.form['TxtPass'] == 'smsm' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('errorlogin'))
 
@app.route('/success')
def success():
   return '<h1 style="background-color:powderblue;" align ="Center" Font-size= "14">You are successfully logged in </h1>'
  
@app.route('/errorlogin')
def errorlogin():
   return '<br><br><h1 style="background-color:powderblue;" align ="Center" Font-size= "14">Sorry!!.. Please check your user name or password <a href = "/">login</a></h1>'
    
if __name__ == '__main__':
   app.run(debug = True)