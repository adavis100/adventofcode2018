
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
        self.metadata_count = None

    def get_metadata_count(self):
        count = 0
        if self.metadata_count:
            count = self.metadata_count
        elif not self.children:
            count = sum(self.metadata)
        else:
            count = self.sum_child_metadata()
        self.metadata_count = count
        return count
    
    def sum_child_metadata(self):
        count = 0
        for i in self.metadata:
            if i <= len(self.children):
                count += self.children[i - 1].get_metadata_count()
        return count

    def __repr__(self):
        return('( children = {} metadata = {} )'.format(self.children, self.metadata))


if __name__ == '__main__':
    main()