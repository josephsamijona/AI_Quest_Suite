import { createSlice } from '@reduxjs/toolkit';

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
export default gameSlice.reducer;