from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ──────────────────────────────────────────────
# DONNÉES DU PORTFOLIO — SERI EZECHIEL STEPHANE
# ──────────────────────────────────────────────
DATA = {
    "name": "Ezéchiel Stéphane",
    "lastname": "SERI",
    "title": "Informaticien · Développeur Full-Stack",
    "tagline": "Étudiant en Licence 3 DASI à l'ESATIC, je conçois des applications mobiles et web performantes.",
    "phone": "0545572045",
    "email": "ezechieltrade@gmail.com",
    "github": "https://github.com/ZEKI-coder",
    "linkedin": "https://linkedin.com/in/ezechiel-seri",
    "location": "Abidjan, Yopougon — Côte d'Ivoire",
    "about": (
        "Passionné d'informatique depuis le lycée, je me spécialise dans le "
        "Développement d'Applications et Systèmes d'Information (DASI) à l'ESATIC. "
        "Titulaire d'un BTS en Réseaux Informatiques et Télécommunications, "
        "j'ai acquis une solide expérience en développement mobile (Flutter, Kotlin, Android Studio), "
        "en développement web (Python, PHP, HTML/CSS, Java) et en administration réseau. "
        "Ponctuel, travailleur et passionné, je transforme les idées complexes en produits simples et efficaces."
    ),
    "skills": [
        {"name": "Python / PHP / Java", "level": 80},
        {"name": "Flutter / Kotlin / Android Studio", "level": 82},
        {"name": "HTML / CSS", "level": 85},
        {"name": "PostgreSQL / MySQL", "level": 75},
        {"name": "Câblage & Config. Réseau", "level": 80},
        {"name": "Git / VS Code / IntelliJ", "level": 78},
    ],
    "projects": [
        {
            "title": "Projets GitHub",
            "description": "Retrouve l'ensemble de mes projets réalisés sur mon profil GitHub : applications mobiles, scripts Python, projets web et plus encore.",
            "tags": ["Flutter", "Python", "Java", "Kotlin", "HTML/CSS"],
            "github": "https://github.com/ZEKIcoder?tab=repositories",
            "demo": "",
            "icon": "🗂️",
        },
        {
            "title": "Application Mobile (Flutter)",
            "description": "Développement d'une application mobile cross-platform avec Flutter et Dart, connectée à une base de données PostgreSQL.",
            "tags": ["Flutter", "Dart", "PostgreSQL"],
            "github": "https://github.com/ZEKIcoder",
            "demo": "",
            "icon": "📱",
        },
        {
            "title": "Site Web Dynamique",
            "description": "Conception d'un site web complet avec back-end PHP, base de données MySQL et interface HTML/CSS responsive.",
            "tags": ["PHP", "MySQL", "HTML", "CSS"],
            "github": "https://github.com/ZEKIcoder",
            "demo": "",
            "icon": "🌐",
        },
        {
            "title": "Script d'Automatisation Python",
            "description": "Développement de scripts Python pour l'automatisation de tâches répétitives et la manipulation de données.",
            "tags": ["Python", "Automatisation"],
            "github": "https://github.com/ZEKIcoder",
            "demo": "",
            "icon": "🐍",
        },
    ],
    "experience": [
        {
            "company": "TGS (Tous Genre de Service)",
            "role": "Technicien Stagiaire en Télécom",
            "period": "1 Juin – 31 Août 2024",
            "desc": (
                "Assistance au technicien chef sur les missions de câblage réseau, "
                "désaturation d'infrastructures et installation de nouveaux clients."
            ),
        },
        {
            "company": "Beryl Informatique",
            "role": "Stagiaire Technicien Réseau",
            "period": "2023",
            "desc": (
                "Gestion et supervision du réseau informatique de l'entreprise. "
                "Formation complémentaire en sécurité informatique."
            ),
        },
    ],
    "education": [
        {
            "school": "ESATIC — Abidjan",
            "degree": "Licence 3 DASI (Développement d'Applications et Systèmes d'Information)",
            "period": "2025 – 2026",
        },
        {
            "school": "Groupe Loko Yopougon",
            "degree": "BTS option RIT (Réseaux Informatiques et Télécommunications)",
            "period": "2021 – 2023",
        },
        {
            "school": "Collège Anador Yopougon",
            "degree": "BAC D",
            "period": "2020 – 2021",
        },
        {
            "school": "Collège Anador Yopougon",
            "degree": "BEPC",
            "period": "2016 – 2017",
        },
    ],
    "languages": [
        {"name": "Français", "level": "Courant (lire, écrire, parler)"},
        {"name": "Anglais", "level": "A2 — Notions"},
    ],
    "qualities": ["Ponctuel", "Travailleur", "Respectueux", "Passionné"],
}


@app.route("/")
def index():
    return render_template("index.html", d=DATA)


@app.route("/contact", methods=["POST"])
def contact():
    """Endpoint pour le formulaire de contact."""
    payload = request.get_json()
    name    = payload.get("name", "")
    email   = payload.get("email", "")
    message = payload.get("message", "")
    # TODO : remplacer par smtplib ou SendGrid pour envoyer un vrai e-mail
    print(f"[CONTACT] De : {name} <{email}>\n{message}")
    return jsonify({"status": "ok", "message": "Message reçu ! Je te répondrai sous 24h."})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)