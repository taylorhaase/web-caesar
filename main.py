from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="rot" method="post">
            <label for "rot">
            Rotate by:
            <input type="text" name="rot" value=0 />
            </label>

            <textarea name="text">
            </textarea>
            <input type="submit" value="Submit Query" />

        </form>
      
      
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)

    text = rewuest.form['text']
    text = str(text)

    encrypted = rotate_string(text, rot)

    return encrypted

app.run()