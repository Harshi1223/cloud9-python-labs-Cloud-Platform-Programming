from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("home.html", names=names)

# Dynamic Profile Page
@app.route("/user/<username>")
def profile(username):
    return render_template("profile.html", username=username)

# Login Page (GET and POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return render_template("login.html", username=username)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)