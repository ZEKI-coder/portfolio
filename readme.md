# Portfolio Flask — Dark Cyberpunk 🟢

Un portfolio personnel moderne et animé construit avec **Python / Flask**.

## 🗂️ Structure du projet

```
portfolio/
├── app.py                  ← Serveur Flask + données du portfolio
├── requirements.txt
├── templates/
│   └── index.html          ← Template Jinja2 (HTML)
└── static/
    ├── css/
    │   └── style.css       ← Thème dark néon
    └── js/
        └── main.js         ← Animations, typewriter, formulaire
```

## ⚡ Installation & lancement

```bash
# 1. Crée et active un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux / macOS
# OU
venv\Scripts\activate           # Windows

# 2. Installe les dépendances
pip install -r requirements.txt

# 3. Lance le serveur
python app.py
```

Ouvre **http://localhost:5000** dans ton navigateur.

## ✏️ Personnalisation

Tout se passe dans `app.py`, dans le dictionnaire `DATA` :

| Clé         | Description                        |
|-------------|------------------------------------|
| `name`      | Ton prénom                         |
| `lastname`  | Ton nom de famille                 |
| `title`     | Intitulé de poste                  |
| `tagline`   | Phrase d'accroche                  |
| `about`     | Texte de présentation              |
| `skills`    | Liste { name, level (0-100) }      |
| `projects`  | Liste { title, description, tags } |
| `experience`| Liste { company, role, period }    |
| `email`     | Ton e-mail de contact              |
| `github`    | URL GitHub                         |
| `linkedin`  | URL LinkedIn                       |

## 📸 Ajouter ta photo

Remplace le bloc `.photo-placeholder` dans `templates/index.html` :

```html
<img src="{{ url_for('static', filename='images/photo.jpg') }}"
     alt="Photo" class="photo-img" />
```

Et place ton image dans `static/images/photo.jpg`.

## 🚀 Déploiement (Render / Railway)

```bash
pip install gunicorn
gunicorn app:app
```

Crée un `Procfile` :
```
web: gunicorn app:app
```

## 🎨 Couleurs (CSS variables)

| Variable    | Valeur    | Usage          |
|-------------|-----------|----------------|
| `--neon`    | `#00FFB2` | Accent vert    |
| `--neon2`   | `#00D4FF` | Accent cyan    |
| `--bg`      | `#050A0E` | Fond principal |
| `--bg-card` | `#0C1519` | Fond cartes    |

Modifie-les dans `static/css/style.css` → section `:root`.