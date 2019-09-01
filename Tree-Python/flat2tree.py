#!/usr/bin/env python

import json

raw_nodes = [
    {'id': 1, 'parent': -1, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 2, 'parent': 1, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 3, 'parent': -1, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 4, 'parent': 1, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 5, 'parent': 1, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 6, 'parent': 2, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 7, 'parent': 2, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 8, 'parent': 2, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id': 9, 'parent': 3, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id':10, 'parent': 3, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id':11, 'parent': 10, 'prop1': 'blarg', 'prop2': 'blarg2'},
    {'id':12, 'parent': 11, 'prop1': 'blarg', 'prop2': 'blarg2'},
]

def build_tree(raw_nodes, parent_name):
    # modified from: https://stackoverflow.com/a/43984479/274549

    nodes = {}
    for i in raw_nodes:
        id, obj = (i['id'], i)
        nodes[id] = obj

    forest = []
    for i in raw_nodes:
        id, parent_id, obj = (i['id'], i[parent_name], i)
        node = nodes[id]

        if parent_id == -1:
            forest.append(node)
        else:
            parent = nodes[parent_id]
            if not 'children' in parent:
                parent['children'] = []
            parent['children'].append(node)

    return forest

print(json.dumps(build_tree(raw_nodes, 'parent'), indent=4))