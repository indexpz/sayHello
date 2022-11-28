from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret_secret"


@app.route("/hello")
def index():
	flash("What's your name?")
	# input_name = request.args.get("input_name", "nieznajomy")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	name = str(request.form["input_name"])
	flash(f"Hi {name.title()}, great to see you!")
	return render_template("index.html")

if __name__ == "__main__":
	app.run()
