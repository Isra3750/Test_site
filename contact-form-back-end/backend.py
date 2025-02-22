from flask import Flask, redirect, url_for, request

# Flask constructor, using current name of __name__
app = Flask(__name__)

#  create a route, the route() decorator in Flask is used to bind a URL to a function
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

# login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# __name__ == '__main__' means that this file is the main file
if __name__ == '__main__':
    app.run()