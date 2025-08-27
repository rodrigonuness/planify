import React, { useEffect, useState } from 'react';

function TodayChecklist() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetch('/api/tasks/today/')
            .then(res => res.json())
            .then(data => setTasks(data));
    }, []);

    const handleCheck = async (id, completed) => {
        await fetch(`/api/tasks/${id}/complete/`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed }),
        });
        setTasks(tasks.map(t => t.id === id ? { ...t, completed } : t));
    };

    return (
        <div>
            <h2>Tarefas de hoje</h2>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        <input
                            type="checkbox"
                            checked={task.completed}
                            onChange={e => handleCheck(task.id, e.target.checked)}
                        />
                        {task.time} - {task.description}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TodayChecklist;
