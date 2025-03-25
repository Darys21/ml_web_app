from flask import Flask, render_template, request 
import os 
import joblib
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import re 


app = Flask(__name__)
UPLOAD_FOLDER = 'data'
MODEL_FOLDER = 'models'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)



@app.route('/')
def index(): 
    """
    ici on affiche la page d'acceuil avec le formulaire d'upload.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Gère le téléchargement d'un fichier CSV et le sauvegardé dans data /.
    """
    file = request.files.get('file') # récupération du fichier
    if file is None:
        return "aucun fichier sélectionné", 400
    if file.filename.endswith('.csv'):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return f"fichier {file.filename} téléchargé avec succès", 200
    return "Seuls les fichiers CSV sont acceptés", 400

@app.route('/train', methods=['POST'])
def train_model():
    """ enttraine le model choisi sur les données uploaedées """
    model_type = request.form.get('model')
    csv_file = os.listdir(UPLOAD_FOLDER)[0]
    file_path = os.path.join(UPLOAD_FOLDER, csv_file)

    data = pd.read_csv(file_path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    #choix du model 
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'random_forest':
        model = RandomForestClassifier(n_estimators=100)
    else:
        return "Model non reconnu", 400
    

    # Entraînement du modèle
    model.fit(X, y)
    
    # sauvegarde du modèle 
    model_path = os.path.join(MODEL_FOLDER, f'{model_type}.pkl')
    joblib.dump(model, model_path)

    return render_template('index.html', message = f"Modèle {model_type} entrainé et sauvegardé avec succès")
    
@app.route('/data')
def list_files():
    """
    Affiche la liste des fichiers dans le dossier data.
    """
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('data.html', files=files)



if __name__ == '__main__':
    app.run(debug=True)