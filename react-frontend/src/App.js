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
        console.log(response)
        const data = await response.text();
        const list=[data]
        const dataObject = JSON.parse(list);
        // console.log(dataObject)
        const presenttemp=dataObject.slice(-1)
        const formattedTime = formatDateToISO8601();
        const timetable=dataObject.slice(0,-1)
        let presenttime
        for (let i = 0; i < timetable.length; i++) {
          const datatimestamp=timetable[i]['timestamp']
            if (datatimestamp.slice(0,13)===formattedTime.slice(0,13)){
              console.log("matches")
            presenttime=i

            }

        }
        const weathertimetable=[]
        for (let i = presenttime; i < presenttime+5; i++) {
          const datatimestamp=timetable[i]
          // console.log(datatimestamp.slice(0,13))
          weathertimetable.push(datatimestamp)
        }
        console.log(weathertimetable)
        // dataObject.slice(0, -1).forEach(element => {
        //   const datatimestamp=element['timestamp']
        //   if (datatimestamp.slice(0,13)===formattedTime.slice(0,13)){
        //     console.log("matches")
        //   }
        //   // console.log(datatimestamp.slice(0,13)===formattedTime.slice(0,13))
        // });
        // console.log(formattedTime.slice(0,13))

        // console.log(dataObject.)
        setApiData(presenttemp);
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
