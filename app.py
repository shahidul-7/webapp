from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/submit", methods=["POST"])
def submit():
     name = request.form["Name"]
     email = request.form["Email"]
     return f"Hello, {name}! \n Your email is: {email}"

if __name__ == "__main__":
     app.run(debug=True)