const fs = require('fs')
const readline = require('readline')

const nbits = 12

// create something to hold the count of each bit
const bitCounter = []
for (b = 0; b < nbits; b++) {
  bitCounter.push([0, 0])
}

// read the file and record bits of each line
const file = readline.createInterface({
  input: fs.createReadStream('input.txt'),
  terminal: false,
})

file.on('line', (line) => {
  const i = parseInt(line, 2)
  // IMPORTANT: need to reverse bits afterwards; bitCounter[0] is the 12th bit
  for (let c = nbits - 1; c >= 0; c--) {
    ++bitCounter[c][(i >> c) & 1]
  }
})

file.on('close', () => {
  const bits = bitCounter.reverse().map((val) => (val[0] > val[1] ? 0 : 1))
  const gammaRate = parseInt(bits.join(''), 2)
  const epsilonRate = gammaRate ^ 0xfff

  console.log(`Gamma rate: ${gammaRate}`)
  console.log(`Epsilon rate: ${epsilonRate}`)
  console.log(`Submarine power consumption: ${gammaRate * epsilonRate}`)
})
