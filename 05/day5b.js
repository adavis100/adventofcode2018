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
    var replacedStr = removeReactions(newStr)
    if (replacedStr.length < min) {
      min = replacedStr.length
    }
  }
  return min
}

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