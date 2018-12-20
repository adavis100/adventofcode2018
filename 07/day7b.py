import bisect
import re
import string
from sortedcontainers import SortedSet


WORKER_COUNT = 5
BASE_WORK_TIME = 60


def main():
    with open("input.txt") as file:
        lines = file.readlines()
    dependencies = {}
    provides = {}
    for line in lines:
        (step, depends_on) = parse(line)
        add_dependencies(dependencies, step, depends_on)
        add_provides(provides, depends_on, step)
    ready = get_ready_steps(dependencies)
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


def get_ready_steps(deps):
    ready = SortedSet()
    for step in deps:
        if not deps[step]:
            ready.add(step)
    return ready


def find_dependency_order(ready, deps, provides):
    done = ''
    time = 0
    workers  = [Worker() for _ in range(WORKER_COUNT)]

    while ready or any(worker.is_assigned() for worker in workers):
        assign_workers(workers, time, ready)
        done += remove_done(workers, time, ready, deps, provides)
        print('{} workers = {} done = {}'.format(time, workers, done))
        time += 1
    print('Total time = {}'.format(time))
    return done


class Worker:
    def __init__(self):
        self.id = None
        self.start = 0

    def assign(self, id, start):
        self.id = id
        self.start = start

    def is_assigned(self):
        return self.id

    def is_done(self, time):
        return time == self.start + BASE_WORK_TIME + ord(self.id) - ord('A')

    def free(self):
        self.id = None

    def __repr__(self):
        return self.id if self.id else '-'


def assign_workers(workers, time, ready):
    for worker in workers:
        if not worker.is_assigned() and ready:
            worker.assign(ready.pop(0), time)
    return


def remove_done(workers, time, ready, deps, provides):
    done = ''
    for worker in workers:
        if worker.is_assigned() and worker.is_done(time):
            done += worker.id
            remove_deps(worker.id, ready, deps, provides)
            worker.free()
    return done


def remove_deps(step, ready, deps, provides):
    if step in provides:
        for dep in provides[step]:
            deps[dep].remove(step)
            if not deps[dep]:
                ready.add(dep)


if __name__ == '__main__':
    main()