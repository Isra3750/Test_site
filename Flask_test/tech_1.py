from flask import Flask, redirect, url_for, render_template
# redirect is for redirecting to another page, url_for is for getting the url

app = Flask(__name__)

# render template is for rendering the template from html file
@app.route('/<name>')
def home(name):
    return render_template("index.html", content=name, r=2, more=["a", "b", "c"]) # inline html

if __name__ == '__main__':
    app.run()