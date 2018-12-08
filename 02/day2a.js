var fs = require('fs')
 
fs.readFile('input.txt', 'utf8', (err, contents) => {
  let twos = 0
  let threes = 0
  let lines = contents.split('\n').forEach(line => {
    var counts = getCounts(line)
    if (hasTwo(counts)) {
        twos++
    } 
    if (hasThree(counts)) {
        threes++
    }
  })
  console.log('Twos = ' + twos)
  console.log('Threes = ' + threes)
  console.log('Checksum = ' + (twos * threes))
})

function getCounts(line) {
    var map = new Map()
    for (let letter of line) {
        if (!map.has(letter)) {
            map.set(letter, 1)
        } else {
            map.set(letter, map.get(letter) + 1)
        }
    }
    return map   
}

function hasTwo(counts) {
    for (let val of counts.values()) {
        if (val === 2) {
            return true
        }
    }
}

function hasThree(counts) {
    for (let val of counts.values()) {
        if (val === 3) {
            return true
        }
    }
}