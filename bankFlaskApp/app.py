from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method=='POST':
        return request.form['name']
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)