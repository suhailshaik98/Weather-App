import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css'

// ---------------------------RESOURCES TO REFER---------------------------------------------------
// Refer to this link https://react-bootstrap.netlify.app/docs/components/accordion
// Watch youtube video https://www.youtube.com/watch?v=8pKjULHzs0s
// -------------------------------------------------------------------------------------

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
          {/* how to add a bootstrap button example */}
        <Button>TestButton</Button> 
        {/* ------------------------------- */}
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
