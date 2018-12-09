var fs = require('fs')
 

//console.log('aA = '  + removeReactions('aA').length)
//console.log('abBA = ' + removeReactions('abBA').length)
//console.log('abAB = ' + removeReactions('abAB').length)
//console.log('dabAcCaCBAcCcaDA = ' + removeReactions('dabAcCaCBAcCcaDA').length)
fs.readFile('input.txt', 'utf8', (err, str) => {
  str = str.replace(/\n/, '')
  console.log(removeReactions(str).length)
})

function removeReactions(inStr) {
  var anyReactions = true
  var str = inStr
  while (anyReactions) {
    var newStr = ''
    anyReactions = false
    for (var i = 0; i < str.length; i++) {
      if (i < str.length - 1 && hasReaction(str.charAt(i), str.charAt(i+1))) {
        i++
        anyReactions = true
      } else {
        newStr += str.charAt(i)
      }
    }
    str = newStr
  }
  return str
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
