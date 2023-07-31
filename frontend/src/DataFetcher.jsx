// file: /0XY_healthcare_data_analysis/frontend/src/DataFetcher.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

function DataFetcher() {
    const [data, setData] = useState(null);
    
    useEffect(() => {
        axios.get('http://localhost:5000/records')
        .then(response => {
            setData(response.data);
        })
        .catch(error => {
            console.error('Error Fetching Data: ', error);
        });
    }, []);
    
    return (
        <dir>
        {data ? (
            <dir>{JSON.stringify(data)}</dir>
        ) : (
        <dir>Loading...</dir>
        )}
        </dir>
    );
}

export default DataFetcher;