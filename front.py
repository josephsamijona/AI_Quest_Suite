import os
import json
from pathlib import Path

# Structure des fichiers avec leur contenu
file_structure = {
    "frontend": {
        "src": {
            "components": {
                "games": {
                    "MazeGame.jsx": """import React from 'react';

const MazeGame = () => {
  return (
    <div>
      <h2>Maze Game</h2>
    </div>
  );
};

export default MazeGame;""",
                    "SnakeGame.jsx": """import React from 'react';

const SnakeGame = () => {
  return (
    <div>
      <h2>Snake Game</h2>
    </div>
  );
};

export default SnakeGame;""",
                    "CTFGame.jsx": """import React from 'react';

const CTFGame = () => {
  return (
    <div>
      <h2>Capture The Flag Game</h2>
    </div>
  );
};

export default CTFGame;"""
                },
                "visualizations": {
                    "PerformanceGraph.jsx": """import React from 'react';

const PerformanceGraph = () => {
  return (
    <div>
      <h2>Performance Graph</h2>
    </div>
  );
};

export default PerformanceGraph;""",
                    "RewardChart.jsx": """import React from 'react';

const RewardChart = () => {
  return (
    <div>
      <h2>Reward Chart</h2>
    </div>
  );
};

export default RewardChart;""",
                    "StateVisualizer.jsx": """import React from 'react';

const StateVisualizer = () => {
  return (
    <div>
      <h2>State Visualizer</h2>
    </div>
  );
};

export default StateVisualizer;"""
                },
                "controls": {
                    "TrainingControls.jsx": """import React from 'react';

const TrainingControls = () => {
  return (
    <div>
      <h2>Training Controls</h2>
    </div>
  );
};

export default TrainingControls;""",
                    "GameControls.jsx": """import React from 'react';

const GameControls = () => {
  return (
    <div>
      <h2>Game Controls</h2>
    </div>
  );
};

export default GameControls;"""
                }
            },
            "hooks": {
                "useWebSocket.js": """import { useState, useEffect } from 'react';

const useWebSocket = (url) => {
  const [socket, setSocket] = useState(null);
  
  useEffect(() => {
    const ws = new WebSocket(url);
    setSocket(ws);
    
    return () => {
      ws.close();
    };
  }, [url]);
  
  return socket;
};

export default useWebSocket;""",
                "useGameState.js": """import { useState, useEffect } from 'react';

const useGameState = () => {
  const [gameState, setGameState] = useState({});
  
  // Ajoutez votre logique de gestion d'état ici
  
  return { gameState, setGameState };
};

export default useGameState;"""
            },
            "store": {
                "gameSlice.js": """import { createSlice } from '@reduxjs/toolkit';

const gameSlice = createSlice({
  name: 'game',
  initialState: {
    score: 0,
    level: 1,
    isPlaying: false
  },
  reducers: {
    updateScore: (state, action) => {
      state.score = action.payload;
    },
    setLevel: (state, action) => {
      state.level = action.payload;
    },
    togglePlaying: (state) => {
      state.isPlaying = !state.isPlaying;
    }
  }
});

export const { updateScore, setLevel, togglePlaying } = gameSlice.actions;
export default gameSlice.reducer;"""
            }
        },
        "package.json": """{
  "name": "frontend",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@reduxjs/toolkit": "^1.9.0",
    "react-redux": "^8.0.5"
  }
}"""
    }
}

def create_file_structure(base_path: Path, structure: dict):
    """Crée récursivement la structure de fichiers et dossiers."""
    for name, content in structure.items():
        path = base_path / name
        
        if isinstance(content, dict):
            # C'est un dossier
            path.mkdir(parents=True, exist_ok=True)
            create_file_structure(path, content)
        else:
            # C'est un fichier
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8')

def main():
    # Créer la structure à partir du répertoire courant
    base_path = Path('.')
    
    try:
        create_file_structure(base_path, file_structure)
        print("✅ Structure de fichiers créée avec succès!")
        
        # Afficher la structure créée
        print("\nStructure créée :")
        def print_tree(path: Path, prefix="", is_last=True):
            print(prefix + ("└── " if is_last else "├── ") + path.name)
            if path.is_dir():
                children = list(path.iterdir())
                for i, child in enumerate(sorted(children)):
                    is_last_child = i == len(children) - 1
                    print_tree(child, prefix + ("    " if is_last else "│   "), is_last_child)
        
        print_tree(base_path / "frontend")
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la structure : {str(e)}")

if __name__ == "__main__":
    main()