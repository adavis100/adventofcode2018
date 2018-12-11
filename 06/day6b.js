var fs = require('fs')
 
var RANGE_LIMIT = 10000

fs.readFile('input.txt', 'utf8', (err, contents) => {
  var coords = parseInput(contents)
  var m = Math.max(...coords.map(p => p.x)) + 1
  var n = Math.max(...coords.map(p => p.y)) + 1
  console.log(m + 'x' + n + ' grid')
  var grid = findAllDistances(coords, m, n)
  console.log('size = ' + findAreaWithinRange(coords, grid, m, n))
})


function parseInput(inStr) {
  var coords = []
  var lines = inStr.split('\n')
  for (let line of lines) {
    var match = line.match(/(\d+), (\d+)/)
    if (match) {
      coords.push({
        x: match[1],
        y: match[2]
      })
    }
  }
  return coords
}

function findAllDistances(coords, m, n) {
  var grid = new Array(m)
  for (let i = 0; i < m; i++) {
    grid[i] = new Array(n)
    for (let j = 0; j < n; j++) {
      let location = {x: i, y: j}
      grid[i][j] = findDistance(coords, location)
    }
    // console.log(grid[i])
  }
  return grid
}

function findDistance(coords, location) {
  var sum = 0
  for (let i = 0; i < coords.length; i++) {
    let distance = dist(location, coords[i])
    sum += distance
  }
    return sum
}

function dist(p1, p2) {
  return Math.abs(p2.x - p1.x) + Math.abs(p2.y - p1.y)
}

function findAreaWithinRange(coords, grid, m, n) {
  var area = 0
  for(let i = 0; i < m; i++) {
    for (let j = 0; j < n;  j++) {
      if (grid[i][j] < RANGE_LIMIT) {
        area++
      }
    }
  }
  return area
}