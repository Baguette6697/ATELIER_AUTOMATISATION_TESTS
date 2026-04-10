from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')

@app.route('/gamelist')
def get_gamelist():
    api_url = "https://www.mmobomb.com/api1/games?sort-by=release-date"
    
    try:
        # On effectue l'appel à l'API MMOBomb
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # On envoie les données au fichier consignes.html
            return render_template('gamelist.html', games=data)
        else:
            return f"Erreur lors de l'appel API : {response.status_code}", response.status_code
            
    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion : {str(e)}", 500


if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
