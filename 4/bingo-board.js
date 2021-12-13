class Cell {
  constructor(value) {
    this.marked = false
    this.value = Number(value)
  }

  toString() {
    const base = this.value < 10 ? ` ${this.value}` : `${this.value}`
    return this.marked ? base + '*' : base
  }
}

class BingoBoard {
  constructor(id) {
    this.id = id
    this.rows = []
  }

  addRow(cells) {
    this.rows.push(cells.map((c) => new Cell(c)))
  }

  // returns a boolean value if a cell was marked or not
  addMark(value) {
    for (let r = 0; r < this.rows.length; r++) {
      for (let c = 0; c < this.rows[r].length; c++) {
        if (this.rows[r][c].value == value) {
          this.rows[r][c].marked = true
          return true
        }
      }
    }
    return false
  }

  // for debugging
  print() {
    for (let r = 0; r < this.rows.length; r++) {
      console.log(...this.rows[r].map((c) => c.toString()))
    }
    console.log('')
  }

  // get the sum of all unmarked cells
  get sumOfUnmarked() {
    let sum = 0
    for (let r = 0; r < this.rows.length; r++) {
      sum = this.rows[r].reduce((pv, c) => (c.marked ? pv : pv + c.value), sum)
    }
    return sum
  }

  get isWinner() {
    // check each row
    for (const r of this.rows) {
      // if none of the cells in the row are unmarked
      if (!r.some((c) => !c.marked)) {
        return true
      }
    }
    // check each column
    const numCols = this.rows[0].length
    for (let c = 0; c < numCols; c++) {
      let foundUnmarked = false
      for (const r of this.rows) {
        if (!r[c].marked) {
          foundUnmarked = true
          break
        }
      }
      if (!foundUnmarked) return true
    }
    // check each diagonal
    let foundUnmarked = false

    // top-left to bottom-right
    for (let idx = 0; idx < numCols; idx++) {
      if (!this.rows[idx][idx].marked) {
        foundUnmarked = true
        break
      }
    }

    if (!foundUnmarked) return true

    // top-right to bottom-left
    for (let c = numCols - 1, r = 0; c >= 0; c--, r++) {
      if (!this.rows[r][c].marked) {
        foundUnmarked = true
        break
      }
    }

    return !foundUnmarked
  }
}

module.exports = BingoBoard
