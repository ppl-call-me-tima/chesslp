import { useState } from "react"
import { ChessBoard } from "react-fen-chess-board"

import MoveMaker from "./MoveMaker"

export default function App() {
  const [fen, setFen] = useState("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

  return (
    <>
      <ChessBoard fen={fen} />
      <MoveMaker setFen={setFen} />
    </>
  )
}
