var fs = require('fs')
 
fs.readFile('input.txt', 'utf8', (err, contents) => {
  var coords = parseInput(contents)
  var m = Math.max(...coords.map(p => p.x)) + 1
  var n = Math.max(...coords.map(p => p.y)) + 1
  console.log(m + 'x' + n + ' grid')
  var grid = findAllClosest(coords, m, n)
  console.log('max = ' + findLargestArea(coords, grid, m, n))
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

function findAllClosest(coords, m, n) {
  var grid = new Array(m)
  for (let i = 0; i < m; i++) {
    grid[i] = new Array(n)
    for (let j = 0; j < n; j++) {
      let location = {x: i, y: j}
      grid[i][j] = findClosest(coords, location)
    }
    // console.log(grid[i])
  }
  return grid
}

function findClosest(coords, location) {
  var min = Number.MAX_SAFE_INTEGER
  var index, multiple
  for (let i = 0; i < coords.length; i++) {
    let distance = dist(location, coords[i])
    if (distance < min) {
      min = distance
      index = i
      multiple = false
    } else if (distance == min) {
      multiple = true
    }
  }
  if (multiple) {
    return null
  } else {
    return index
  }
}

function dist(p1, p2) {
  return Math.abs(p2.x - p1.x) + Math.abs(p2.y - p1.y)
}

function findLargestArea(coords, grid, m, n) {
  var valid = (new Array(coords.length)).fill(true)
  var area = (new Array(coords.length)).fill(0)
  for(let i = 0; i < m; i++) {
    for (let j = 0; j < n;  j++) {
      if (((i == 0 || i == m - 1 || j == 0 || j == n-1)) && grid[i][j]) {
        valid[grid[i][j]] = false
        area[grid[i][j]] = 0
      } else if (grid[i][j] && valid[grid[i][j]]) {
        area[grid[i][j]]++
      }
    }
  }
  return Math.max(...area)
}