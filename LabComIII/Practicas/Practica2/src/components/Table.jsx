import React from 'react';

const Table = ({ data }) => {
  const totalIncome = data.reduce((total, item) => total + item.income, 0);
  const averageIncome = (totalIncome / data.length).toFixed(2);

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Marca</th>
            <th>Ingreso Neto</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.brand}</td>
              <td>{item.income}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <br />
      <p>Ingreso promedio: ${averageIncome}</p>
    </div>
  );
};

export default Table;
