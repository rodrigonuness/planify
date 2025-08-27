import React from 'react';
import ExcelUpload from './components/ExcelUpload';
import TodayChecklist from './components/TodayChecklist';

function App() {
    return (
        <div>
            <h1>Planify</h1>
            <ExcelUpload />
            <TodayChecklist />
        </div>
    );
}

export default App;
