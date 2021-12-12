const fs = require('fs')
const readline = require('readline')
// need to keep lines in memory for part b
const lines = []
const inputFile = 'input.txt'
const nBits = 12

function getCommonBits(lines, tiebreaker) {
  const bitCounter = []
  // initialize a new bit counter
  for (b = 0; b < nBits; b++) {
    bitCounter.push([0, 0])
  }

  lines.forEach((line) => {
    for (let c = 0; c < nBits; c++) {
      ++bitCounter[c][line.charAt(c)]
    }
  })

  const tbInverse = Number(!tiebreaker)
  // want most common if tiebreaker is 1
  if (tiebreaker == 1)
    return bitCounter.map((val) =>
      val[tiebreaker] >= val[tbInverse] ? tiebreaker : tbInverse
    )
  // want least common if tiebreaker is 0
  return bitCounter.map((val) =>
    val[tiebreaker] <= val[tbInverse] ? tiebreaker : tbInverse
  )
}

function getRating(currentBit, valuesLeft, pos, tiebreaker) {
  if (valuesLeft.length === 1) {
    return parseInt(valuesLeft[0], 2)
  }

  const nextValues = valuesLeft.filter((val) => val.charAt(pos) == currentBit)
  return getRating(
    getCommonBits(nextValues, tiebreaker)[pos + 1],
    nextValues,
    pos + 1,
    tiebreaker
  )
}

// read the file and record bits of each line
const file = readline.createInterface({
  input: fs.createReadStream(inputFile),
  terminal: false,
})

file.on('line', (line) => {
  lines.push(line)
})

file.on('close', () => {
  const bits = getCommonBits(lines, 1)
  const gammaRate = parseInt(bits.join(''), 2)
  const epsilonRate = gammaRate ^ 0xfff

  console.log(`Gamma rate: ${gammaRate}`)
  console.log(`Epsilon rate: ${epsilonRate}`)
  console.log(`Submarine power consumption: ${gammaRate * epsilonRate}`)

  const ogr = getRating(bits[0], lines, 0, 1)
  const cdsr = getRating((epsilonRate >> (nBits - 1)) & 1, lines, 0, 0)

  console.log(`Oxygen generator rating: ${ogr}`)
  console.log(`CO2 scrubber rating: ${cdsr}`)
  console.log(`Life support rating: ${ogr * cdsr}`)
})
