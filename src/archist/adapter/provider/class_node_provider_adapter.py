import ast
from typing import cast

from archist.port.provider.ast_provider_port import ModuleNodeWithAst
from archist.port.provider.class_node_provider_port import ClassNodeProviderPort, ModuleWithClassNodes, ClassNode


class ClassNodeProviderAdapter(ClassNodeProviderPort):
    def process(self, module_node: ModuleNodeWithAst) -> ModuleWithClassNodes:
        ast_classdef_statements = [
            statement
            for statement in module_node.ast.body
            if isinstance(statement, ast.ClassDef)
        ]

        ret = cast(ModuleWithClassNodes, module_node)
        ret.class_nodes = [
            ClassNode(
                module_node=module_node,
                name=classdef.name
            )
            for classdef in ast_classdef_statements
        ]
        return ret
