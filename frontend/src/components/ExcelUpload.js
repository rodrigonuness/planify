import React, { useState } from 'react';

function ExcelUpload() {
    const [file, setFile] = useState(null);

    const handleChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);
        await fetch('/api/upload/', {
            method: 'POST',
            body: formData,
        });
        alert('Upload realizado!');
    };

    return (
        <div>
            <input type="file" accept=".xlsx,.xls" onChange={handleChange} />
            <button onClick={handleUpload} disabled={!file}>Enviar</button>
        </div>
    );
}

export default ExcelUpload;
