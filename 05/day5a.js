var fs = require('fs')
 

// console.log('aA = '  + reactPolymer('aA').length + ' expect 0')
// console.log('abBA = ' + reactPolymer('abBA').length + ' expect 0')
// console.log('abAB = ' + reactPolymer('abAB').length + ' expect 4')
// console.log('dabAcCaCBAcCcaDA = ' + reactPolymer('dabAcCaCBAcCcaDA').length + ' expect 10')
fs.readFile('input.txt', 'utf8', (err, str) => {
  str = str.replace(/\n/, '')
  console.log(reactPolymer(str).length)
})

function reactPolymer(str) {
  var accumulator = str.charAt(0)
  var remaining = str.substring(1)
  while (remaining) {
    if (accumulator && hasReaction(accumulator.charAt(accumulator.length - 1), remaining.charAt(0))) {
      accumulator = accumulator.substring(0, accumulator.length - 1)
      remaining = remaining.substring(1)
    } else {
      accumulator += remaining.charAt(0)
      remaining = remaining.substring(1)
    }
  }
  return accumulator
}

function hasReaction(first, second) {
  return ((isLower(first) && isUpper(second) && first == second.toLowerCase()) ||
          (isUpper(first) && isLower(second) && first == second.toUpperCase()))
} 

function isLower(c) {
  return c === c.toLowerCase()
}

function isUpper(c) {
  return c === c.toUpperCase()
} 
