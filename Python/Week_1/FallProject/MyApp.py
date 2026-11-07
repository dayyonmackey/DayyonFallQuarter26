# import the Flask Library into this file
from flask import Flask, render_template

# Create a new Flask app called "app"
app = Flask(__name__)

# Create a home page for our Flask app (website)
@app.route ('/') # The route for the home page
def Index(): # 
    return render_template("index.html") # Load the index html template

if __name__ == '__main__':
    app.run(debug = True)