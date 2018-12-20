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
        (step, depends_on) = parse(line)
        add_dependencies(dependencies, step, depends_on)
        add_provides(provides, depends_on, step)
    ready = find_ready_steps(dependencies)
    order = find_dependency_order(ready, dependencies, provides)
    print(order)


def parse(line):
        p = re.compile('Step (.) must be finished before step (.) can begin.')
        m = p.match(line)
        return (m[2], m[1])


def add_dependencies(deps, step, depends_on):
    if step not in deps:
        deps[step] = []
    if depends_on not in deps:
        deps[depends_on] = []
    add_edge(deps, step, depends_on)


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


def find_dependency_order(ready, deps, provides):
    order = ''
    while ready:
        step = ready.pop(0)
        order += step
        remove_dependencies(step, ready, deps, provides)
    return order


def remove_dependencies(step, ready, deps, provides):
    if step in provides:
        for dep in provides[step]:
            deps[dep].remove(step)
            if not deps[dep]:
                ready.add(dep)


if __name__ == '__main__':
    main()