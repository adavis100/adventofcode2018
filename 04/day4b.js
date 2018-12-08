var fs = require('fs')
 
var guardMap = new Map()

fs.readFile('input.txt', 'utf8', (err, lines) => {
  processLines(lines)
  result = findSleepiestGuardMinute()
  console.log('Guard = ' + result.guardId)
  console.log('Minute = ' + result.minute)
  console.log('Result = ' + (result.guardId * result.minute))
})

function processLines(lines) {
  var i = 0
  while (i < lines.length) {
    var guardRe = /\[.*\] Guard #(\d+) begins shift/
    var match = lines[i].match(guardRe)
    if (match) {
      var guardId = match[1]
      if (!guardMap.has(guardId)) {
          guardMap.set(guardId, {sleeps: new Array(60).fill(0)})
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

function findSleepiestGuardMinute() {
  var minute
  var id
  var max = 0
  for (var key of guardMap.keys()) {
    for (var i = 0; i < 60; i++) {
      let sleepCount = guardMap.get(key).sleeps[i]
      if (sleepCount > max) {
          id = key
          minute = i
          max = sleepCount
      }
    }
  }
  return {guardId: id, minute: minute}
}