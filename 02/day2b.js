var fs = require('fs')
 
fs.readFile('input.txt', 'utf8', (err, contents) => {
  let lines = contents.split('\n')
  for (let line of lines) {
    for (let other of lines) {
        if (other != line && line.length > 0 && areCorrectBoxes(line, other)) {
            return 0
        }
    }
  }
})

function areCorrectBoxes(box1, box2) {
    var commonChars = ''
    var differs = 0;
    for (var i = 0; i < box1.length; i++) {
        if (box1.charAt(i) === box2.charAt(i)) {
            commonChars += box1.charAt(i)
        } else {
            differs++
        }
        if (differs === 2) {
            return false
        }
    }
    console.log('Found match! Common chars = ' + commonChars)
    return true
}