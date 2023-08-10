import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    async function fetchApiData() {
      try {
        const response = await fetch('http://localhost:8000/');
        const data = await response.text();
        setApiData(data);
      } catch (error) {
        console.error('Error fetching API data:', error);
      }
    }

    fetchApiData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          { 'Learn React'}
        </a>
        {/* Here our data is being printed in the variable apiData*/}
        {apiData}
      </header>
    </div>
  );
}

export default App;
