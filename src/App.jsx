import React ,{useState,useEffect} from 'react';
import './App.css';

function App() {
  const [variable,setVariable] = useState(0);

  useEffect(()=>{
    fetch('/variable').then(response=>response.json()).then(data=>{
      setVariable(data.variable);
    });
  },[]);

  return (
    <div className="App">
      <header className="App-header">
        <p>{variable}</p>
      </header>
    </div>
  );
}

export default App;
