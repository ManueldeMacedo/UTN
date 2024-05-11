import React from 'react';
import { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const Task = ({addTask }) => {
  const [showForm, setShowForm] = useState(false);
  const [taskText, setTaskText] = useState('');

  const handleButtonClick = () => {
    setShowForm(true);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();

    addTask(taskText);
    setShowForm(false);

    setTaskText('');
  };

  return (
    <>
      <Button variant="success" onClick={handleButtonClick}>Agregar Tarea</Button>
      <br></br>
      {showForm && (
        <Form onSubmit={handleFormSubmit}>
          <br></br>
          <Form.Group controlId="taskForm">
            <Form.Control
              type="text"
              value={taskText}
              onChange={(e) => setTaskText(e.target.value)}
              placeholder="Ingrese el texto de la tarea"
            />
          </Form.Group>
          <br></br>
          <Button variant="primary" type="submit">
            Agregar
          </Button>
        </Form>
      )}
    </>
  )
}

export default Task