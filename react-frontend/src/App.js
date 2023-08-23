import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
import './App.css';
import { Card, Container, Row, Col} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import sample from './bgvideo.mp4';


// ---------------------------RESOURCES TO REFER---------------------------------------------------
// Refer to this link https://react-bootstrap.netlify.app/docs/components/accordion
// Watch youtube video https://www.youtube.com/watch?v=8pKjULHzs0s
// -------------------------------------------------------------------------------------

function App() {
  const [apiData, setApiData] = useState(null);
  const [temperaturestring, setWeathertimetable] = useState(null);
  const [timestring, settime] = useState(null);

  useEffect(() => {
    async function fetchApiData() {
      try {
        const response = await fetch('http://192.168.1.251:8000/');
        const data = await response.text();
        const dataObject = JSON.parse(data);
        console.log(dataObject)

        const formattedTime = formatDateToISO8601Local(); // Define this function or replace with appropriate time formatting
        console.log(formattedTime)
        let presenttime = -1;

        for (let i = 0; i < dataObject.length; i++) {
          const datatimestamp = dataObject[i].timestamp;
          if (datatimestamp.slice(0, 13) === formattedTime.slice(0, 13)) {
            console.log("matches");
            presenttime = i;
            break;
          }
        }

        const weathertimetable = [];
        if (presenttime !== -1) {
          for (let i = presenttime+1; i < Math.min(presenttime + 6, dataObject.length); i++) {
            weathertimetable.push(dataObject[i]);
          }
        }
        console.log(weathertimetable);
        let temperaturestring
        let timestring
      //   for (let i = 0; i < weathertimetable.length; i++) {
      //     temperaturestring +=
      //     weathertimetable[i].temperature +
      // '  ' +
      // '<div style="width: 2px;"></div> ';
      //     timestring += weathertimetable[i].time +" "
      //   }
      const formatTime = (time) => {
        const hour = parseInt(time.split(':')[0]);
        const suffix = hour >= 12 ? 'am ' : 'pm';
        const formattedHour = hour > 12 ? hour - 12 : hour;
        return `${formattedHour} ${suffix}`;
      };

      const weatherElements = weathertimetable.map((weatherData, i) => (
          
          <Col key={i}>
          <Card   className="card border-0 bg-transparent">
            <Card.Body>
            <Card.Title style={{ fontSize:'90%' }}  >
              {Math.round(weatherData.temperature)} C</Card.Title>
              <Card.Text style={{ fontSize:'70%' }}>{formatTime(weatherData.time)}</Card.Text>
            </Card.Body>
          </Card>
        </Col>


      ));
        // timestring=timestring.slice(9)
        // temperaturestring=temperaturestring.slice(9)
        // console.log(temperaturestring)

        setWeathertimetable(weatherElements);
        settime(timestring)
        setApiData(dataObject[dataObject.length - 1]); // Assuming you want to set the last item as apiData
      } catch (error) {
        console.error('Error fetching API data:', error);
      }
    }

    fetchApiData();
  }, []);

  // function getDynamicText(weathertimetable) {
  //   let temperaturestring
  //   for (let i=0;i<weathertimetable.length;i++){
  //     temperaturestring=weathertimetable[i].temperature+" "
  //   }
  //   return temperaturestring;

  // }

  return (
    
    <div className="App">
          <video className='videoTag' autoPlay loop muted >
    <source src={sample} type='video/mp4' />
</video>
      <header className="App-header">


        <Container>

         <Row>
          <Col>
          <div style={{ height: '40%' }}></div>
          <Card className='card bg-transparent border-0'> 
          <Card.Title style={{ fontSize:'160%' }}>Hello Buffalo!</Card.Title>
          </Card>
          </Col>
          
          <Col>
          <Row>
          <Card className='card-glass'> 
            <Container>
              <Row>
                <Col>
                <Card className="card bg-transparent border-0">
                  <Card.Body>
                  <Card.Title><img src='https://www.blog.christinepolz.com/wp-content/uploads/2020/05/IMG_0920.gif' width="50%" height="50%"></img></Card.Title>
                  </Card.Body>
                </Card>
                </Col>
                <Col>
                <div style={{ height: '20%' }}></div>
                <Card className="card bg-transparent border-0">
                <Card.Body>
            <Card.Title style={{ fontSize:'160%' }}>
              {Math.round(apiData)} C
            </Card.Title>
          </Card.Body>

</Card>
                </Col>

              </Row>

            </Container>

        </Card>

          </Row>
          <div style={{ height: '10%' }}></div>
          <Row>
          <Card className="card-glass">
                <Container>
                  <Row>
                  {temperaturestring}

                  </Row>
                </Container>

              </Card>


          </Row>
          </Col>
          </Row> 

        </Container>

      </header>
    </div>
  );
}

function formatDateToISO8601Local() {
  const currentTime = new Date();
  const year = currentTime.getFullYear();
  const month = String(currentTime.getMonth() + 1).padStart(2, '0');
  const day = String(currentTime.getDate()).padStart(2, '0');
  const hours = String(currentTime.getHours()).padStart(2, '0');
  const minutes = String(currentTime.getMinutes()).padStart(2, '0');
  const seconds = String(currentTime.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day}T${hours}:${minutes}:${seconds}`;
}

// const formattedTime = formatDateToISO8601();
// console.log(formattedTime);
export default App;