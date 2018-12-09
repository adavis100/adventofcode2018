var fs = require('fs')


// console.log('dabAcCaCBAcCcaDA = ' + findMinReactions('dabAcCaCBAcCcaDA'))
fs.readFile('input.txt', 'utf8', (err, str) => {
  str = str.replace(/\n/, '')
  console.log(findMinReactions(str))
})

function findMinReactions(str) {
  var atoz = 'acdefghijklmnopqrstuvwxyz'
  var min = Number.MAX_SAFE_INTEGER

  for (letter of atoz) {

    var re = new RegExp('[' + letter + letter.toUpperCase() + ']', 'g')
    var newStr = str.replace(re, '')
    var replacedStr = reactPolymer(newStr)
    if (replacedStr.length < min) {
      min = replacedStr.length
    }
  }
  return min
}

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