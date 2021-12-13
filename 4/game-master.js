class GameMaster {
  constructor() {
    this.boards = []
    this.lastCalledNumber = null
  }

  add(board) {
    this.boards.push(board)
  }

  remove({ id }) {
    this.boards = this.boards.filter((b) => b.id != id)
  }

  // returns the winning board or null based on the last called number
  callNumber(value) {
    const nVal = Number(value)
    this.lastCalledNumber = nVal
    for (const b of this.boards) {
      if (b.addMark(nVal) && b.isWinner) {
        // now we want to remove boards when they win,
        // but keep checking other boards for the called number
        // until only one "winner" remains
        if (this.boards.length > 1) this.remove(b)
        else return b
      }
    }
    return null
  }

  get winner() {
    return this.boards.find((b) => b.isWinner)
  }
}

module.exports = GameMaster
