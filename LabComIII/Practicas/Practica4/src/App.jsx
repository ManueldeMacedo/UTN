import './App.css'
import List from './components/list/List'
import 'bootstrap/dist/css/bootstrap.min.css';
import Task from './components/task/Task';
import { useState } from 'react';

function App() {
  const [counter, setCounter] = useState(3);
  const [tasks, setTasks] = useState([
    { id: 0, text: 'Tarea 1', state: false },
    { id: 1, text: 'Tarea 2', state: false },
    { id: 2, text: 'Tarea 3', state: false }
  ]);

  const incrementCounter = () => {
    setCounter(counter + 1);
  };

  const deleteTask = (id) => {
    const updatedTasks = tasks.filter(task => task.id !== id);
    setTasks(updatedTasks);
  };

  const addTask = (text) => {
    incrementCounter();
    const newTask = {
      id: counter,
      text: `${text}`,
      state: false
    };
    setTasks([...tasks, newTask]);
  };

  const statusTask = (id) => {
    const updatedTasks = tasks.map(task => {
      if (task.id === id) {
        return { ...task, state: !task.state };
      }
      return task;
    });
    setTasks(updatedTasks);
  };

  return (
    <>
      <h1>Lista de Tareas</h1>
      <Task addTask={addTask}></Task>
      <br></br>
      <List tasks={tasks} statusTask={statusTask} deleteTask={deleteTask}></List>
    </>
  )
}

export default App
