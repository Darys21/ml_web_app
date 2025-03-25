from flask import Flask, render_template, request 
import os 


app = Flask(__name__)
UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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

@app.route('/data')
def list_files():
    """
    Affiche la liste des fichiers dans le dossier data.
    """
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('data.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)