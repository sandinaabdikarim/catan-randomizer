from flask import Flask, jsonify, render_template
from randomizer.generator import generate_board

app = Flask(__name__)

RESOURCE_IMAGES = {
    "forest": "/static/images/forest.png",
    "pasture": "/static/images/pasture.png",
    "field": "/static/images/field.png",
    "hill": "/static/images/hill.png",
    "mountain": "/static/images/mountain.png",
    "desert": "/static/images/desert.png",
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hexes')
def get_hexes():
    hexes = generate_board()
    hexes_with_images = []
    for row in hexes:
        row_data = []
        for h in row:
            hex, token = list(h.items())[0]
            row_data.append({
                "type": hex,
                "token": token,
                "image": RESOURCE_IMAGES[hex]})
        hexes_with_images.append(row_data)

    return jsonify({"hexes": hexes_with_images})  # Sending a two-dimensional array

if __name__ == '__main__':
    app.run(debug=True)
