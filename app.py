from flask import Flask, render_template, request
from database import initialize_db, save_child

app = Flask(__name__)

initialize_db()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        child_name = request.form.get("child_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        talent = request.form.get("talent")
        parent_name = request.form.get("parent_name")

        save_child(child_name, age, gender, talent, parent_name)

        return f"""
        <h1>Registration Successful!</h1>
        <p>Child Name: {child_name}</p>
        <p>Age: {age}</p>
        <p>Gender: {gender}</p>
        <p>Talent: {talent}</p>
        <p>Parent Name: {parent_name}</p>
        <a href="/register">Register Another Child</a>
        """

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
