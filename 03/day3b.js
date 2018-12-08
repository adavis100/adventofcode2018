var fs = require('fs')
 
var claims = []

fs.readFile('input.txt', 'utf8', (err, contents) => {
  let re = /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/
  let lines = contents.split('\n').forEach(line => {
    var matches = line.match(re)
    if (matches) {
      claims.push({
        id: Number(matches[1]),
        x: Number(matches[2]),
        y: Number(matches[3]),
        width: Number(matches[4]),
        height: Number(matches[5])
      })
    }
  })
  findNonOverlapping()
})

function findNonOverlapping() {
  var width = max(claims.map(it => it.x)) + max(claims.map(it => it.width))
  var height = max(claims.map(it => it.y)) + max(claims.map(it => it.height))
  console.log(width + ' x ' + height + ' matrix')
  var rectangle = initMatrix(width, height)

  for (var i = 0; i < claims.length; i++) {
    addFabric(rectangle, i)
  }

  for (i = 0; i < claims.length; i++) {
    if (isNonOverlapping(rectangle, i)) {
      console.log(claims[i].id + ' does not overlap')
    }
  }
}

function max(arr) {
  return arr.reduce((a, b) => Math.max(a, b))  
}

function initMatrix(width, height) {
  var matrix = []
  for (var i = 0; i < width; i++) {
    let row = []
    for (var j = 0; j < height; j++) {
      row[j] = 0
    }
    matrix[i] = row 
  }
  return matrix
}

function addFabric(matrix, index) {
  for (var i = claims[index].x; i < (claims[index].x + claims[index].width); i++) {
    for(var j = claims[index].y; j < (claims[index].y + claims[index].height); j++) {
      matrix[i][j]++
    }
  }
}

function isNonOverlapping(matrix, index) {
  for (var i = claims[index].x; i < (claims[index].x + claims[index].width); i++) {
    for(var j = claims[index].y; j < (claims[index].y + claims[index].height); j++) {
      if(matrix[i][j] != 1) {
        return false
      }
    }
  }
  return true
}