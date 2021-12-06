<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
@app.route("/index") 
def home(): 
    return render_template("index.html")

@app.route("/perfil")
def profile():
    return render_template("perfil.html")

@app.route("/experiencia")
def experience():
    return render_template("experiencia.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contato")
def contact():
    return render_template("contato.html")


=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
@app.route("/index") 
def home(): 
    return render_template("index.html")

@app.route("/perfil")
def profile():
    return render_template("perfil.html")

@app.route("/experiencia")
def experience():
    return render_template("experiencia.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contato")
def contact():
    return render_template("contato.html")

if __name__== "__main__":
    app.run(debug=True) #host='0.0.0.0'
>>>>>>> 4002d99cb4b5be2f4fcd93f3273066533a811158
   