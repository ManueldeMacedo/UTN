import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Table from './components/Table'

function App() {
  const [count, setCount] = useState(0)

  const netIncomes = [
    { brand: 'McDonalds', income: 1291283 },
    { brand: 'Burger King', income: 1927361 },
    { brand: 'KFC', income: 1098463 }
  ];

  // const totalIncome = netIncomes.reduce((total, item) => total + item.income, 0);
  // const averageIncome = (totalIncome / netIncomes.length).toFixed(2);

  return (
    <>
      <Table data={netIncomes} />
    </>
  )
}

export default App
