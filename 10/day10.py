import re

def main():
    with open('input.txt') as file:
        lines = [line for line in file.readlines() if line]
    lights = parse(lines)
    move_lights(lights)


def parse(lines):
    lights = []
    for line in lines:
        pattern = re.compile(r'position=<([ \-\d]+), ([ \-\d]+)> velocity=<([ \-\d]+), ([ \-\d]+)>')
        match = pattern.match(line)
        lights.append(Light(match[1], match[2], match[3], match[4]))
    return lights


def move_lights(lights):
    time = 0
    found = False
    while not found:
        for light in lights:
            light.move()
        time += 1
        if lights_are_close(lights):
            print('After {} seconds'.format(time))
            print_lights(lights)
            print()
            found = True


def lights_are_close(lights):
    max_x = max(light.x for light in lights)
    min_x = min(light.x for light in lights)
    max_y = max(light.y for light in lights)
    min_y = min(light.y for light in lights)
    return (max_x - min_x) < 80 and (max_y - min_y) < 80 and has_lines(lights)


def has_lines(lights):
    light_set = set()
    for light in lights:
        light_set.add((light.x, light.y))
    lines = 0
    for (x, y) in light_set:
        if has_line(x, y, light_set):
            lines += 1
    return lines > 1


def has_line(x, y, light_set):
    for y_index in range(y+1, y+8):
        if not (x, y_index) in light_set:
            return False
    return True


def print_lights(lights):
    max_x = max(light.x for light in lights)
    min_x = min(light.x for light in lights)
    max_y = max(light.y for light in lights)
    min_y = min(light.y for light in lights)
    for y in range(max_y - min_y + 1):
        for x in range(max_x - min_x + 1):
            if (has_light(lights, min_x + x, min_y + y)):
                print('#', end='')
            else:
                print('.', end='')
        print()


def has_light(lights, x, y):
    return any(light.x == x and light.y == y for light in lights)
    

class Light:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = int(x)
        self.y = int(y)
        self.velocity_x = int(velocity_x)
        self.velocity_y = int(velocity_y)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def __repr__(self):
        return('position=<{}, {}> velocity=<{}, {}>'.format(self.x, self.y, self.velocity_x, self.velocity_y))


if __name__ == '__main__':
    main()