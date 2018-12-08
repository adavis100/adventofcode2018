var fs = require('fs')
 
var counter = 0
var values = new Set([0])
fs.readFile('input.txt', 'utf8', (err, contents) => {
  var lines = contents.split('\n')
  while(true) {
    for(let line of lines) {
      var num = parseInt(line)
      if(!isNaN(num)) {
        counter += num
        if (values.has(counter)) {
          console.log(counter)
          return false
        } else {
          values.add(counter)
        }
      }
    }
  }
})
  
