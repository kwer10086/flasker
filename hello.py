from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    context ={
            'para1':'This is <strong> BOLD </strong> text',
            'my_list':['computerScience','Language','Chemistry','Automation'],
    }

    return render_template('index.html',context=context)

@app.route('/<name>')
def user(name):
    context={
        'name':name,
    }
    return render_template("user.html",context=context)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500