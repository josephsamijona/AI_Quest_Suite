import os

# Structure du système de fichiers
filesystem_structure = {
    "backend": {
        "ai_quest_project": ["__init__.py", "settings.py", "urls.py", "asgi.py", "wsgi.py"],
        "agents": {
            "__init__.py": None,
            "apps.py": None,
            "models": ["__init__.py", "base_agent.py", "maze_agent.py", "snake_agent.py", "ctf_agent.py"],
            "training": ["__init__.py", "trainers.py"],
            "serializers.py": None
        },
        "metrics": {
            "__init__.py": None,
            "apps.py": None,
            "models": ["__init__.py", "training_metrics.py"],
            "serializers.py": None
        },
        "websockets": {
            "__init__.py": None,
            "consumers": ["__init__.py", "game_consumer.py"],
            "routing.py": None
        }
    }
}

# Fonction pour créer la structure des fichiers et dossiers
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                open(os.path.join(path, file), 'a').close()
        else:
            open(path, 'a').close()

# Point de départ pour la création du système de fichiers
create_structure('.', filesystem_structure)

print("File system structure created successfully.")
