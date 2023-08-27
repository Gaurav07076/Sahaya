from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/generic',methods = ['GET','POST'])
def generic():
    return render_template('generic.html')

@app.route('/fifth',methods = ['GET','POST'])
def fifth():
    return render_template('fifth.html')

@app.route('/elements',methods = ['GET','POST'])
def elements():
    return render_template('elements.html')






if __name__ == '__main__':
    app.run(debug=True,port=5000)