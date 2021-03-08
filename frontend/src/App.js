import React, { useState, useEffect } from "react";
import Card from "./components/Card/Card";
import Button from "./components/Button/Button";
import Select from "./components/Select/Select";
import SelectDestiny from './components/SelectDestiny/SelectDestiny'
import { Row, Col } from "react-grid-system";
import axios from 'axios';
import "./styles.css";
import Space from "./components/Space/Space";

export default function App() {
  const [balance, setBalance] = useState(0);
  const [ticketOptions, setTicketOptions] = useState([{ name: "Selecione o cartão", value: 0 }]);
  const [originOptions, setOriginOptions] = useState([{ name: "Selecione a origem", id: 0, region: 0 }]);
  const [destinyOptions, setDestinyOptions] = useState([{ name: "Selecione o destino", id: 0, region: 0 }]);
  const [lineOptions, setLenOptions] = useState([{ name: "Selecione a linha", id: "0" },{ name: "Comum", id: "1" },{ name: "Executiva", id: "2" }]);
  const [busLine, setBusLine] = useState(0);
  const [originRegion, setOriginRegion] = useState(0);
  const [destinyRegion, setDestinyRegion] = useState(0);
  const [ticketId, setTicketId] = useState(0);
  const [total, setTotal] = useState(0);

  const apiUrl = "http://localhost:8000"

  const getTickets = () => {
    try {
      axios.get(`${apiUrl}/ticket/`, {auth: {username: 'admin', password: 'admin'}}).then(res => {
        setTicketOptions(prevState => [ ...prevState, ...res.data ]);
      })
    } catch (error) {}
  };
  
  const updateTicket = () =>{
    try {
      const defaulState = [{ name: "Selecione o cartão", value: 0 }]
      axios.get(`${apiUrl}/ticket/`, {auth: {username: 'admin', password: 'admin'}}).then(res => {
        setTicketOptions([ ...defaulState, ...res.data ]);
      })
    } catch (error) {}
  }

  const getTravelData = () =>{
    axios.get(`${apiUrl}/district/`, {auth: {username: 'admin', password: 'admin'}}).then(res => {
      setOriginOptions(prevState => [ ...prevState, ...res.data ]);
      setDestinyOptions(prevState => [ ...prevState, ...res.data ]);
    })
    setLenOptions([{ name: "Selecione a linha", id: "0" },{ name: "Comum", id: "1" },{ name: "Executiva", id: "2" }])
  }


  useEffect(() => {
    getTickets();
    getTravelData();
  }, []);

  const pay = () => {
    const data = {
      "bus_type": busLine,
      "origin_region": originRegion,
      "destiny_region": destinyRegion,
      "ticket_bus": ticketId
    }
    axios.post(`${apiUrl}/journey/`, {data}, {auth: {username: 'admin', password: 'admin'}}).then(res => {
      setOriginOptions([{ name: "Selecione a origem", id: 0, region: 0 }])
      setDestinyOptions([{ name: "Selecione o destino", id: 0, region: 0}])
      setLenOptions([{ name: "Selecione a linha", id: "0" }])
      setBusLine(0)
      setOriginRegion(0)
      setDestinyRegion(0)
      getTravelData();
      updateTicket();
      setClient(ticketId)
      setTotal(0)
    })
    
  }

  const setClient = (value) => {
    const client = ticketOptions.find(x => x.id === value)
    setBalance(parseFloat(client.value))
    setTicketId(client.id)
  }

  const getTotal = (bus, destiny, origin) => {
    let price = bus == 1 ? 4 : 7 
    const additional = 0.60
    if(destiny &&  origin){
      if(origin != destiny){
        if(origin == 1){
          price = price + additional
        }else if(origin == 2 && destiny !=  1){
          price = price + (additional * 2)
        }else if(origin == 3 && destiny !=  1 && destiny !=  5){
          price = price + (additional * 2)
        }else if(origin == 4 && destiny !=  1 && destiny !=  5){
          price = price + (additional * 2)
        }else if(origin == 5 && destiny ==  2){
          price = price + (additional * 2)
        }else{
          price = price + additional
        }
      }
    }
    setTotal(price)
  }

  const updateBusline = (value) =>{
    setBusLine(value)
    getTotal(value, destinyRegion, originRegion )
  }

  const updateOriginRegion = (value) =>{
    setOriginRegion(value)
    getTotal(busLine, destinyRegion, value )
  }

  const updateDestinyRegion = (value) =>{
    setDestinyRegion(value)
    getTotal(busLine, value, originRegion )
  }

  return (
    <Card>
      <Row>
        <Col sm={2}>Cartão:</Col>
        <Col>
          <Select
            id={"card"}
            name="Ticket Bus"
            options={ticketOptions}
            onChange={(e) => setClient(parseInt(e.target.value))}
          />
        </Col>
      </Row>
      <Space />
      <Row>
        <Col>
          Saldo: <strong>R$ {balance.toFixed(2) || "0.00"}</strong>
        </Col>
      </Row>
      <Space />
      <Row>
        <Col>
          Linha <Select id={"line"} options={lineOptions} onChange={(e) => updateBusline(e.target.value)}/>
        </Col>
      </Row>
      <Space />
      <Row>
        <Col>
          Origem <SelectDestiny id={"origin"} options={originOptions} onChange={(e) => updateOriginRegion(e.target.value)}/>
        </Col>
      </Row>
      <Space />
      <Row>
        <Col>
          Destino <SelectDestiny id={"destiny"} options={destinyOptions} onChange={(e) => updateDestinyRegion(e.target.value)} />
        </Col>
      </Row>
      <Space />
      <Row>
        <Col sm={8}>
          <strong>Total: R$ {total}</strong>
        </Col>
        <Col>
          <Button id={"pagar"} outlined onClick={pay}>
            Pagar
          </Button>
        </Col>
      </Row>
    </Card>
  );
}
