import _ast
import ast
from typing import List, Any

import click

from nodes import AST_NODES, OBJECTS, get_class_str


def find_ast_class(body: Any, nodes: List) -> None:
    """
    Recursivly iterate over nodes and add all occurences of ast node to nodes
    """
    if "body" not in dir(body):
        nodes.append(body)
    else:
        for node in body.body:
            nodes.append(node)
            if "body" in dir(node):
                find_ast_class(node, nodes)


def iter_node(nodes: List) -> None:
    """
    Iterate over all the ast nodes present inside the file
    and process it to get the relevent info
    """
    for node in nodes:
        AST_NODES[get_class_str(node)].parse_node(node)


def get_source_ast(name: str) -> _ast.Module:
    """
    Return ast of source code
    """
    with open(name, "r") as f:
        data = f.read()
    return ast.parse(data)


def check_circular(modules):
    for module in modules:
        module = module.replace('.','/')
        source_ast = get_source_ast(f'{str(module)}.py')
        imported_obj = []
        for node in source_ast.body:
            if type(node) == _ast.Import:
                imported_obj.append(node.names[0].name)
            elif type(node) == _ast.ImportFrom:
                imported_obj.extend(name.name for name in node.names)
    return imported_obj

def find_imported_obj(body):
    imported_obj = []
    modules_to_check = []
    for node in body:
        if type(node) == _ast.Import:
            imported_obj.append(node.names[0].name)
        elif type(node) == _ast.ImportFrom:
            modules_to_check.append(node.module)
            imported_obj.extend(name.name for name in node.names)
    return imported_obj, modules_to_check

@click.command()
@click.option("--name", help="Name of the file", required=True)
def find_circular_import(name: str) -> None:
    nodes = []
    source_ast = get_source_ast(name)
    for node in source_ast.body:
        if type(node) not in [_ast.Import,_ast.ImportFrom]:
            nodes.append(node)
            find_ast_class(node, nodes)
    imported_obj, modules = find_imported_obj(source_ast.body)
    iter_node(nodes)
    p = check_circular(modules)
    for i in p:
        if i in OBJECTS:
            print(f"There is circular import {i} in  is the culprit")


if __name__ == "__main__":
    find_circular_import()