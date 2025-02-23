from flask import Flask, request, render_template 

# Flask constructor, using current name of __name__
app = Flask(__name__)

#  create a route, the route() decorator in Flask is used to bind a URL to a function
@app.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == 'POST':
        first_name = request.form.get("Firstname")
        last_name = request.form.get("Lastname")
        email = request.form.get("email")
        op = request.form.get("op")
        message = request.form.get("Message")
        
        return "Your name is " + first_name + " " + last_name + ", your email is " + email + ", your query type is " + op + ", and your message is " + message
    return render_template("index.html")


# __name__ == '__main__' means that this file is the main file
if __name__ == '__main__':
    app.run(debug=True)
