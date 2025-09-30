import { useState } from "react"

export default function MoveMaker({ setFen }) {
  const [input, setInput] = useState("")

  function handleChange(e) {
    setInput(e.target.value)
  }

  function handleSubmit(e) {
    e.preventDefault()

    const params = { input: input }

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(params),
    }

    fetch("http://127.0.0.1:8000/api/input", options)
      .then(res => res.json())
      .then(data => setFen(data))
    
    setInput("")
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={input} onChange={handleChange} />
      <button>Submit</button>
    </form>
  )
}
