var fs = require('fs')
 
var guardMap = new Map()

fs.readFile('input.txt', 'utf8', (err, contents) => {
  let lines = contents.split('\n')
  lines = lines.sort()
  processLines(lines)
  var sleepiestGuard = findSleepiest()
  var sleepiestMinute = findSleepiestMinute(sleepiestGuard)
  console.log('Guard = ' + sleepiestGuard)
  console.log('Minute = ' + sleepiestMinute)
  console.log('Result = ' + (sleepiestGuard * sleepiestMinute))
})

function processLines(lines) {
  var i = 0
  while (i < lines.length) {
    var guardRe = /\[.*\] Guard #(\d+) begins shift/
    var match = lines[i].match(guardRe)
    if (match) {
      var guardId = match[1]
      if (!guardMap.has(guardId)) {
          guardMap.set(guardId, {sleeps: new Array(60).fill(0), total: 0})
      }
      var guard = guardMap.get(guardId)
      var sleepRe = /\[[\d-]* 00:(\d\d)\] falls asleep/
      var wakeRe = /\[[\d-]* 00:(\d\d)\] wakes up/ 
      i++
      var sleepMatch = lines[i].match(sleepRe)
      while (sleepMatch) {
        var sleepMin = Number(sleepMatch[1])
        var wakeMatch = lines[++i].match(wakeRe)
        var wakeMin = Number(wakeMatch[1])
        setSleepTime(guard, sleepMin, wakeMin)
        i++
        if (!lines[i]) {
            break
        }
        var sleepMatch = lines[i].match(sleepRe)
      }
    } else {
        i++
    }
  }
}

function setSleepTime(guard, sleepMin, wakeMin) {
  guard.total += wakeMin - sleepMin
  for (var i = sleepMin; i < wakeMin; i++) {
    guard.sleeps[i]++
  } 
}

function findSleepiest() {
  var max = 0
  var id
  for (var key of guardMap.keys()) {
    let sleep = guardMap.get(key).total;
    if (sleep > max) {
        max = sleep
        id = key
    }
  }
  return id
}

function findSleepiestMinute(guardId) {
  var max = 0
  var minute
  for (var i = 0; i < 60; i++) {
    let sleepCount = guardMap.get(guardId).sleeps[i]
    if (sleepCount > max) {
        max = sleepCount
        minute = i
    }
  }
  return minute
}