class GameMaster {
  constructor() {
    this.boards = []
    this.lastCalledNumber = null
  }

  add(board) {
    this.boards.push(board)
  }

  // returns the winning board or null based on the last called number
  callNumber(value) {
    const nVal = Number(value)
    this.lastCalledNumber = nVal
    for (const b of this.boards) {
      if (b.addMark(nVal) && b.isWinner) {
        return b
      }
    }
    return null
  }

  get winner() {
    return this.boards.find((b) => b.isWinner)
  }
}

module.exports = GameMaster
