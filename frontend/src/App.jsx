// /0XY_healthcare_data_analysis/frontend/src/App.jsx
import { useState } from 'react'
import './App.css'
import DataFetcher from './DataFetcher.jsx'

function App() {
  const [count, setCount] = useState(0); // consider for later use
  

  return (
    <>
      <div id='body' className="flex-column min-100-vh">
        <header className='hero'>
          <h1 className='app-title'>Healthcare Analysis Tool</h1>
          <p>Analyse and visualise healthcare data to gain insights.</p>
        </header>
        <main className='flex-row justify-space-between'>
          <div className="card">
          <button onClick={() => {/* load or analyse data here */}}>
            Load Latest Data
          </button>
          <p>
          Select parameters fro the options above/drop down and click "Load Latest Data" to begin analysis.
          </p>
        </div>
        {/* Adding visual elements Charts/tables here */}
        
        <DataFetcher/>
      </main>
    </div>
    </>
  );
}

export default App;
