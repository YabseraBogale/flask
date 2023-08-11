from flask import Flask,render_template,url_for


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/memo.html')
def memo():
    return render_template('memo.html')


if __name__=="__main__":
    app.run(debug=True)