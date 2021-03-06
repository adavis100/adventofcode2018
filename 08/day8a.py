
def main():
    with open("input.txt") as file:
        input = file.read()
    nums = [int(val) for val in input.split()]
    head = build_tree(nums)
    print(head)
    print('metadata = {}'.format(head.get_metadata_count()))


def build_tree(nums):
    num_children = nums.pop(0)
    num_metadata  = nums.pop(0)
    children = []
    metadata = []
    for _ in range(num_children):
        children.append(build_tree(nums))
    for _ in range(num_metadata):
        metadata.append(nums.pop(0))
    return Node(children, metadata)


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def get_metadata_count(self):
        child_metadata = 0
        for child in self.children:
            child_metadata += child.get_metadata_count()
        return sum(self.metadata) + child_metadata

    def __repr__(self):
        return('( children = {} metadata = {} )'.format(self.children, self.metadata))


if __name__ == '__main__':
    main()