from flask import Flask, redirect, url_for
# redirect is for redirecting to another page, url_for is for getting the url

app = Flask(__name__)

# how to get into this page, require route (path with "/"" which is default)
@app.route('/')
def home():
    return "Hello this is the main page <h1>HELLO WORLD</h1>" # inline html

@app.route('/about')
def about():
    return "This is the about page"

@app.route('/user/<name>') # this is a dynamic route, grabs the name from the url
def user(name):
    return f"Hello {name}"

# example of redirect and url_for
@app.route('/admin/')
def admin():
    # can add if statement to check if user is admin
    return redirect(url_for("user", name="Admin!")) # put name of function that we want to redirect to, which is "user" function in this case with name of parameter "admin"

if __name__ == '__main__':
    app.run()