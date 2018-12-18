import bisect
import re
import string


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    deps = {}
    for line in lines:
        (step, dependsOn) = parse(line)
        add_dep(deps, step, dependsOn)
    findDependencyOrder(deps)
    print()


def parse(line):
        p = re.compile('Step (.) must be finished before step (.) can begin.')
        m = p.match(line)
        return (m[2], m[1])


def add_dep(deps, step, dependsOn):
    if step not in deps:
        deps[step] = []
    if dependsOn not in deps:
        deps[dependsOn] = []
    add_edge(deps, step, dependsOn)


def add_edge(deps, step, dependsOn):
      bisect.insort(deps[step], dependsOn)


def findDependencyOrder(deps):
    while deps:
        removeDep(deps)


def removeDep(deps):
    for letter in string.ascii_uppercase:
        if letter in deps and not deps[letter]:
            print(letter, end='')
            del deps[letter]
            removeStep(deps, letter)
            return


def removeStep(deps, letter):
    for step in deps:
        if letter in deps[step]:
            deps[step].remove(letter)


if __name__ == '__main__':
    main()