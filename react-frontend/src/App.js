import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
import './App.css';
import { Card, Container, Row, Col} from 'react-bootstrap'
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
        <Container>
          <Row>
            <Col> </Col>
            <Col>
        <Card> 
          <Card.Body>
            <Card.Title>
              Temperature
            </Card.Title>
            <Card.Text>
              {apiData}
            </Card.Text>
          </Card.Body>
        </Card>
            </Col>
          </Row>

          <Row>
          <Col> Hello </Col>
          <Col>    </Col>
          </Row>

          <Row>
            <Col> </Col>
            <Col>
        <Card> 
          <Card.Body>
            <Card.Title>
              Forecast
            </Card.Title>
            <Card.Text>
              Sample temp
            </Card.Text>
          </Card.Body>

        </Card>
            </Col>
          </Row>
        </Container>
      </header>
    </div>
  );
}

export default App;
