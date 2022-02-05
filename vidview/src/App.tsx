import React from 'react';
import VidDisplay from './components/vid-display';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>
        gRPC Video Streamer Demo
      </h1>
      <VidDisplay/>
    </div>
  );
}

export default App;
