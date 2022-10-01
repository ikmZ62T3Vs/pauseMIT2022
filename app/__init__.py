import os
import sys
from flask import Flask, request, render_template, redirect
import jinja2

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST', 'GET'])
def analysis():
    if request.method == "POST":
        # here we get Sakeths data from the python file, and then we parse it for further analysis
        times = str(request.form.get('data')).split(' ')
        print(times)

        # here we send a list of values to be outputted to a table
        return render_template('analysis_page.html',times=times)
    else:
        return redirect("/", code=10)


def main():
    return 1
main()


