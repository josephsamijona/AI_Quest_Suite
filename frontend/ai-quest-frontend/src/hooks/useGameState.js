import { useState, useEffect } from 'react';

const useGameState = () => {
  const [gameState, setGameState] = useState({});
  
  // Ajoutez votre logique de gestion d'état ici
  
  return { gameState, setGameState };
};

export default useGameState;