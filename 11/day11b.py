GRID_SERIAL_NO = 1309
GRID_SIZE = 300


def main():
    power_dict = get_power_grid()
    max_coord = get_grid_maxes(power_dict)
    print(max_coord)
    return


def get_power_grid():
    power_dict = {}
    for x in range(1, GRID_SIZE - 1):
        for y in range(1, GRID_SIZE - 1):
            power_dict[(x, y, 1)] = get_power_level(x, y)
    return power_dict


def get_grid_maxes(power_dict):
    max_power = 0
    max_coord = (0, 0, 0)
    for box_size in range(2, GRID_SIZE):
        max_box_start = GRID_SIZE - box_size
        for x in range(1, max_box_start):
            for y in range(1, max_box_start):
                if box_size % 2 == 0:
                    half = int(box_size / 2)
                    power_dict[(x, y, box_size)] = (power_dict[(x, y, half)] +
                                                    power_dict[(x, y + half, half)] +
                                                    power_dict[(x + half, y, half)] +
                                                    power_dict[(x + half, y + half, half)])
                else:
                    power_dict[(x, y, box_size)] = (power_dict[(x+1, y+1, box_size -1)] +
                                                    power_dict[(x, y, 1)] +
                                                    sumxs(x + 1, y, box_size - 1, power_dict) +
                                                    sumys(x, y + 1, box_size - 1, power_dict))
                if power_dict[(x, y, box_size)] > max_power:
                    max_power = power_dict[(x, y, box_size)]
                    max_coord = (x, y, box_size)
                    print('New max power {} at {}'.format(max_power, max_coord))
    return max_coord


def sumxs(x, y, size, power_dict):
    total = 0
    for i in range(size):
        total += power_dict[(x + i, y, 1)]
    return total


def sumys(x, y, size, power_dict):
    total = 0
    for i in range(size):
        total += power_dict[(x, y + i, 1)]
    return total


def get_power_level(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += GRID_SERIAL_NO
    power *= rack_id
    power = int(power / 100) % 10 - 5
    return power


if __name__ == '__main__':
    main()