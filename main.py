from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
form="""<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
      <h2>Signup</h2>
      <form method="post" action="result">
      <table>
      <tr>
      <td>Username</td>
      <td><input type="text" name="txtUsername" value="{4}"><font color=red>{0}</font></td>
      </tr>
        <tr>
      <td>Password</td>
    <td><input type="password" name="txtPassword" value="{5}"><font color=red>{1}</font></td>
      </tr>
        <tr>
      <td>Verify Password</td>
    <td><input type="password" name="txtVerify" value="{6}"><font color=red> {2}</font></td>
      </tr>
        <tr>
      <td>Email (Optional)</td>
      <td><input type="text" name="txtEmail" value="{7}"><font color=red> {3}</font></td>
      </tr>
      <tr>
      <td colspan=2>
      <input type="submit" value="Submit">
      </td></tr>
      </table>
      
    
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("","","","","","","","","")
@app.route("/result", methods=['POST'])
def encrypt():
    username=request.form['txtUsername']
    err1=""
    success="true"
    if(username==""):
        err1="Please enter Username"
        success="false"
    elif(len(username)<3 or len(username)>20 or (' ' in username)):
        err1="Invalid Username. Must be between 3 and 20 without spaces in it"
        success="false"
    pwd=request.form['txtPassword']
    err2=""
    if(pwd==""):
        err2="Please enter Password"
        success="false"
    pwdVerify=request.form['txtVerify']
    err3=""
    if(pwdVerify==""):
        err3="Password do not match"
        success="false"
    if(pwdVerify!=pwd):
        err3="Password do not match"
        success="false"
    email=request.form['txtEmail']
    err4=""
    if(len(email)<3 or len(email)>20 or (' ' in email)):
        err4="Invalid Email. Must be between 3 and 20 without spaces in it"
        success="false"
    else:
        if (('.' in email) and ('@' in email)):
            err4=""
        else:
            err4="Invalid Email. Must contain @ and ."
            success="false"
    if(success=="false"):
        return form.format(err1,err2,err3,err4,username,"","",email)
    else:
        return "<h2>Welcome, "+username+"!</h2>"
app.run()