from flask import Flask, render_template, request, redirect
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('testing.html')


@app.route("/proses_selesai", methods=["GET", "POST"])
def proses_selesai():
    radio_result = request.form["radio_proses"]

    if (radio_result):
        subprocess.Popen('run_proses.bat',
                         creationflags=subprocess.CREATE_NEW_CONSOLE)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
