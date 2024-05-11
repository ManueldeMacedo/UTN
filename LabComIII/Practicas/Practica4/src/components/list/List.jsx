import React from 'react'
import { useState } from 'react';
import { ListGroup, Form, Button } from 'react-bootstrap';

const List = ({ tasks, statusTask, deleteTask }) => {
  return (
    <ListGroup>
      {tasks.map((task, index) => (
        <ListGroup.Item key={index} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <Form.Check aria-label="option 1" onClick={() => statusTask(task.id)}/>
          <div style={{ textDecoration: task.state ? 'line-through' : 'none', color: task.state ? 'grey' : 'inherit' }}>{task.text}</div>
          <Button variant="danger" onClick={() => deleteTask(task.id)} className="ms-2">Eliminar</Button>
        </ListGroup.Item>
      ))}
    </ListGroup>
  )
}

export default List