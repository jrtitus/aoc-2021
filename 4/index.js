const fs = require('fs')
const readline = require('readline')
const BingoBoard = require('./bingo-board')
const GameMaster = require('./game-master')

const inputFile = 'input.txt'

const lines = []
const gm = new GameMaster()

const file = readline.createInterface({
  input: fs.createReadStream(inputFile),
  terminal: false,
})

file.on('line', (line) => {
  lines.push(line)
})

file.on('close', () => {
  const [calledNumbers, ...rest] = lines

  // Build each board and add to the game master
  let board = null
  let boardCounter = 0
  rest.forEach((line) => {
    if (line.length == 0) {
      if (board != null) {
        gm.add(board)
      }
      board = new BingoBoard(boardCounter++)
    } else {
      board.addRow(line.trim().split(/\s+/))
    }
  })
  // add the last board
  gm.add(board)

  for (const n of calledNumbers.split(',')) {
    const winningBoard = gm.callNumber(n)
    if (winningBoard) {
      console.log(`The losing board is board #${winningBoard.id}:`)
      winningBoard.print()
      console.log(
        `The losing score is ${winningBoard.sumOfUnmarked} * ${
          gm.lastCalledNumber
        } = ${winningBoard.sumOfUnmarked * gm.lastCalledNumber}`
      )
      break
    }
  }
})
