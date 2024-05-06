import React from 'react';
import { useState } from 'react';
import { Button, Form } from 'react-bootstrap'

const Login = () => {
    const [userEntered, setUserEntered]= useState('');

    const handleUserEntered = (event) =>{
        var letraO = event.target.value.toLowerCase().includes('o');

        if (letraO)
            alert("Por favor, ¡Nombres de usuario sin la letra o!");        

        setUserEntered(event.target.value);
        
        console.log(event.target.value);
    }

    const handleLoginSubmit =(event)=> {
        event.preventDefault();

        var letraO = userEntered.toLowerCase().includes('o');
        
        if (userEntered === "" || letraO){
            alert("Usuario inválido para registrarse");
            return;
        }

        alert("¡Usuario registrado correctamente!");

        setUserEntered('');
    }

    return (
        <div>
            <Form onSubmit={handleLoginSubmit}>
                <Form.Group controlId="-name">
                    <Form.Label className='text-light'>User Name: </Form.Label>
                    <Form.Control
                        type="text"
                        placeholder='User...'
                        onChange={handleUserEntered}
                        value={userEntered}
                    />
                </Form.Group>
                <br/>
                <Button type='submit' variant='warning' className="mb-3 mt-2 ps-5 pe-5">Registrar</Button>
            </Form>
        <p>Nombre de usuario: {userEntered}</p>
        </div>
  );
};

export default Login;
