#http://www.cruisingworld.com/features/2015-boat-of-the-year-awards/
# git add -A && git commit -m "Your Message"

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()