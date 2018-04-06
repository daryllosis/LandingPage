from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas', methods=['GET', 'POST'])
def ninjas():
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template("ninjas.html", first_name = first_name, last_name = last_name)

@app.route('/dojos/new')
def new_ninjas():
    return render_template("dojos.html")


if __name__ == "__main__":
    #run our server
    app.run(debug=True)