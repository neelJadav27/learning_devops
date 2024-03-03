from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://cdn.pixabay.com/photo/2016/11/14/04/45/elephant-1822636_1280.jpg",
    "https://cdn.pixabay.com/photo/2013/05/17/07/12/elephant-111695_1280.jpg",
    "https://cdn.pixabay.com/photo/2016/05/28/08/32/elephant-1421167_1280.jpg",
    "https://cdn.pixabay.com/photo/2016/11/14/03/46/girl-1822525_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/10/20/10/58/elephant-2870777_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/11/06/15/30/elephants-2923917_1280.jpg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
