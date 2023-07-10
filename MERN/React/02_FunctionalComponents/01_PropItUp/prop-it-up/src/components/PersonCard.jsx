import React from 'react'

export default function PersonCard(props) {
    const {firstName, lastName, age, hairColor} = props;
    return (
    <div>
        <h2>{lastName}, {firstName}</h2>
        <p>Age: {age}</p>
        <p>Hair: {hairColor}</p>
    </div>
  )
}
