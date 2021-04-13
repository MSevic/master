import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'

class App extends Component {
    state = {
        today: {
            Date: "",
            CLose: 0,
            High: 1,
            Low: 0,
            Prediction: 0
        }
    }

    componentDidMount() {
        axios.get('http://localhost:8000/predictor/predictions/GLD/1')
            .then(response => {
                var data = response.data
                var keys = Object.keys(data)
                var thekey = keys.reduce(function (p, v) {
                    return (p > v ? p : v);
                });

                this.setState({
                    today: {
                        Date: response.data[thekey].Date,
                        Close: response.data[thekey].Close,
                        High: response.data[thekey].High,
                        Low: response.data[thekey].Low,
                        Prediction: response.data[thekey].prediction_d3
                    }
                })
            })
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Predikcija cene zlata za sutrašnji dan</h1>
                </header>
                <p className="App-intro">
                    Date : {this.state.today.Date} <br/>
                    High : {this.state.today.High} <br/>
                    <b>Close : {this.state.today.Close}</b> <br/>
                    Low : {this.state.today.Low} <br/>
                    Prediction for next day close : {this.state.today.Prediction} <br/>
                </p>
            </div>
        );
    }
}

export default App;
