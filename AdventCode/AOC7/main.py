# You have a shiny gold bag. If you wanted to carry it in at least one other bag,
# how many different bag colors would be valid for the outermost bag?
# (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# Part 2
# How many individual bags are required inside your single shiny gold bag?

import re

bag_pattern = re.compile("^[a-z]+ [a-z]+ ")
child_bag_pattern = re.compile("\d+ [a-z]+ [a-z]+ bag")
child_bag_split_pattern = re.compile("[a-z]+")
child_bag_num_pattern = re.compile("\d+")
shiny_gold = 'shiny gold'


class Node(object):
    def __init__(self, bag):
        self.bag = bag
        self.num_bags = 0
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def add_bag_num(self, obj):
        self.num_bags = obj


def traverse_bags(check):
    bags = []
    for entry in check:
        first_bag_match = re.findall(bag_pattern, entry)
        first_bag = None
        if len(first_bag_match) == 1:
            first_bag = Node(first_bag_match[0].strip())
            first_bag.num_bags = 1
            matches = re.findall(child_bag_pattern, entry)
            for bag_match in matches:
                bag_split = re.findall(child_bag_split_pattern, bag_match)
                bag_split.remove('bag')
                bag = Node(' '.join([item for item in bag_split]))
                num = re.findall(child_bag_num_pattern, bag_match)
                bag.add_bag_num(int(num[0]))
                first_bag.add_child(bag)
        bags.append(first_bag)
    return bags


def get_init_gold(tree):
    gold_count = 0
    node_gold = []
    for tree_node in tree:
        for node_child in tree_node.children:
            if node_child.bag == shiny_gold:
                gold_count += 1
                del tree[tree.index(tree_node)]
                node_gold.append(tree_node.bag)
                break
    node_gold_check = len(node_gold)

    while node_gold_check > 0:
        node_gold_check = 0
        for tree_node in tree:
            for node_child in tree_node.children:
                if node_child.bag in node_gold:
                    gold_count += 1
                    node_gold_check += 1
                    del tree[tree.index(tree_node)]
                    node_gold.append(tree_node.bag)
                    break

    return gold_count


def recursive_child_get(node, tree):
    current_sum = 1
    for node_value in tree:
        # find value in tree
        if node_value.bag == node:
            if len(node_value.children) > 0:
                # if node has children
                for child in node_value.children:
                    current_sum += child.num_bags * recursive_child_get(child.bag, tree)

            return current_sum


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]
    bag_tree = traverse_bags(entries)
    # answer1 = get_init_gold(bag_tree)
    answer2 = recursive_child_get(shiny_gold, bag_tree) - 1
    print("answer: ", answer2)
