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
    order = find_dependency_order(ready, dependencies, provides)
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


def find_dependency_order(ready, deps, provides):
    done = ''
    time = 0
    workers  = [None] * 5
    while ready or any(workers):
        assign_workers(workers, time, ready, deps, provides)
        done += remove_done(workers, time, ready, deps, provides)
        print('{} workers = {} done = {}'.format(time, workers, done))
        time += 1
    print('Total time = {}'.format(time))
    return done


class Worker:
    def __init__(self, id, start):
        self.id = id
        self.start = start
        self.end = start + 60 + self.time_to_process_letter(id)
    def time_to_process_letter(self, letter):
        return ord(letter) - ord('A')
    def __repr__(self):
        return self.id


def assign_workers(workers, time, ready, deps, provides):
    for i, worker in enumerate(workers):
        if not worker and ready:
            workers[i] = Worker(ready.pop(0), time)
    return


def remove_done(workers, time, ready, deps, provides):
    done = ''
    for i, worker in enumerate(workers):
        if worker and is_done(worker, time):
            done += worker.id
            remove_deps(worker.id, ready, deps, provides)
            workers[i] = None
    return done


def is_done(worker, time):
    return time == worker.end


def remove_deps(step, ready, deps, provides):
    if step in provides:
        for dep in provides[step]:
            deps[dep].remove(step)
            if not deps[dep]:
                ready.add(dep)


if __name__ == '__main__':
    main()