from flask import Flask
from joblib import dump, load
from flask import request
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__ , template_folder='template')

#import du modèle entrainé
model = load('model.joblib')


@app.route("/", methods=["GET"])

def index():
    return render_template("index.html")


@app.route("/quality", methods=["POST"])


def prediction():
    if request.json:
        json_data = request.get_json()
        regressor = model

        prediction = regressor.predict([json_data['quality']])
        prediction = float(prediction[0])

        response = {
            'Niveau de qualité estimé' : prediction
        }

        return jsonify(response), 200
    
#Iniialisation de Flask       
if __name__ == "__main__":
    app.run(debug=True)