import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import {Button,Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// ---------------------------RESOURCES TO REFER---------------------------------------------------
// Refer to this link https://react-bootstrap.netlify.app/docs/components/accordion
// Watch youtube video https://www.youtube.com/watch?v=8pKjULHzs0s
// -------------------------------------------------------------------------------------

function App() {
  const [apiData, setApiData] = useState(null);
  const [weathertimetable, setWeathertimetable] = useState(null);

  useEffect(() => {
    async function fetchApiData() {
      try {
        const response = await fetch('http://localhost:8000/');
        const data = await response.text();
        const dataObject = JSON.parse(data);

        const formattedTime = formatDateToISO8601(); // Define this function or replace with appropriate time formatting

        let presenttime = -1;

        for (let i = 0; i < dataObject.length; i++) {
          const datatimestamp = dataObject[i]['timestamp'];
          if (datatimestamp.slice(0, 13) === formattedTime.slice(0, 13)) {
            console.log("matches");
            presenttime = i;
            break;
          }
        }

        const weathertimetable = [];
        if (presenttime !== -1) {
          for (let i = presenttime; i < Math.min(presenttime + 5, dataObject.length); i++) {
            weathertimetable.push(dataObject[i]);
          }
        }
        console.log(weathertimetable);

        setWeathertimetable(weathertimetable);
        setApiData(dataObject[dataObject.length - 1]); // Assuming you want to set the last item as apiData
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
          {/* Example of adding a Bootstrap button */}
          <Button variant="primary">TestButton</Button> 
        </p>
        {/* Displaying weathertimetable data in a Bootstrap card */}
        <Card>
  <Card.Body>
    <Card.Title>Weather Timetable</Card.Title>
    <Card.Text>
      {weathertimetable !== null ? (
        weathertimetable.map((entry, index) => (
          <div key={index}>
            {/* Display your data properties here */}
            <p>{entry.time}</p>
            <p>{entry.temperature} C</p>
            {/* Add more properties as needed */}
          </div>
        ))
      ) : (
        <p>Loading weather data...</p>
      )}
    </Card.Text>
  </Card.Body>
</Card>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

function formatDateToISO8601() {
  const currentTime = new Date();
  const year = currentTime.getUTCFullYear();
  const month = String(currentTime.getUTCMonth() + 1).padStart(2, '0');
  const day = String(currentTime.getUTCDate()).padStart(2, '0');
  const hours = String(currentTime.getUTCHours()).padStart(2, '0');
  const minutes = String(currentTime.getUTCMinutes()).padStart(2, '0');
  const seconds = String(currentTime.getUTCSeconds()).padStart(2, '0');
  
  return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}Z`;
}

const formattedTime = formatDateToISO8601();
// console.log(formattedTime);
export default App;
