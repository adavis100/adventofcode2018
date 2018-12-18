import bisect
import re
import string
from sortedcontainers import SortedSet


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    dependencies = {}
    provides = {}
    for line in lines:
        (step, dependsOn) = parse(line)
        add_dependencies(dependencies, step, dependsOn)
        add_provides(provides, dependsOn, step)
    ready = find_ready_steps(dependencies)
    order = findDependencyOrder(ready, dependencies, provides)
    print(order)


def parse(line):
        p = re.compile('Step (.) must be finished before step (.) can begin.')
        m = p.match(line)
        return (m[2], m[1])


def add_dependencies(deps, step, dependsOn):
    if step not in deps:
        deps[step] = []
    if dependsOn not in deps:
        deps[dependsOn] = []
    add_edge(deps, step, dependsOn)


def add_provides(provides, provider, step):
    if provider not in provides:
        provides[provider] = []
    add_edge(provides, provider, step) 


def add_edge(graph, node, neighbor):
      bisect.insort(graph[node], neighbor)


def find_ready_steps(deps):
    ready = SortedSet()
    for step in deps:
        if not deps[step]:
            ready.add(step)
    return ready


def findDependencyOrder(ready, deps, provides):
    order = ''
    while ready:
        step = ready.pop(0)
        order += step
        removeDeps(step, ready, deps, provides)
    return order


def removeDeps(step, ready, deps, provides):
    if step in provides:
        for dep in provides[step]:
            deps[dep].remove(step)
            if not deps[dep]:
                ready.add(dep)


if __name__ == '__main__':
    main()