var fs = require('fs')
 
var counter = 0
fs.readFile('input.txt', 'utf8', (err, contents) => {
  contents.split('\n').forEach(line => counter += Number(line))
  console.log(counter)
    
})

