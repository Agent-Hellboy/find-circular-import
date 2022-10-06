import re

OBJECTS = []


def get_class_str(node_repr):
    node_str = type(node_repr)
    ptrn = re.search(r"<(.*?)>", str(node_str))
    return ptrn[1].split("'")[1]


class AST:
    @classmethod
    def parse_node(cls, obj):
        pass


class Add:
    @classmethod
    def parse_node(cls, obj):
        pass


class And:
    @classmethod
    def parse_node(cls, obj):
        pass


class AnnAssign:
    @classmethod
    def parse_node(cls, obj):
        if obj.target:
            AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        if obj.annotation:
            AST_NODES[get_class_str(obj.annotation)].parse_node(obj.annotation)


class Assert:
    @classmethod
    def parse_node(cls, obj):
        if obj.test:
            AST_NODES[get_class_str(obj.test)].parse_node(obj.test)
        if obj.msg:
            AST_NODES[get_class_str(obj.msg)].parse_node(obj.msg)


class Assign:
    @classmethod
    def parse_node(cls, obj):
        if obj.targets:
            for node in obj.targets:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class AsyncFor:
    @classmethod
    def parse_node(cls, obj):
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.orelse:
            for node in obj.orelse:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.target:
            AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        if obj.iter:
            AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)


class AsyncFunctionDef:
    @classmethod
    def parse_node(cls, obj):
        if obj.args:
            AST_NODES[get_class_str(obj.args)].parse_node(obj.args)
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.decorator_list:
            for node in obj.decorator_list:
                AST_NODES[get_class_str(node)].parse_node(node)
        OBJECTS.append(obj.name)


class AsyncWith:
    @classmethod
    def parse_node(cls, obj):
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.items:
            for node in obj.items:
                AST_NODES[get_class_str(node)].parse_node(node)


class Attribute:
    @classmethod
    def parse_node(cls, obj):
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        OBJECTS.append(obj.attr)


class AugAssign:
    @classmethod
    def parse_node(cls, obj):
        if obj.target:
            AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class AugLoad:
    @classmethod
    def parse_node(cls, obj):
        pass


class AugStore:
    @classmethod
    def parse_node(cls, obj):
        pass


class Await:
    @classmethod
    def parse_node(cls, obj):
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class BinOp:
    @classmethod
    def parse_node(cls, obj):
        if obj.left:
            AST_NODES[get_class_str(obj.left)].parse_node(obj.left)
        if obj.right:
            AST_NODES[get_class_str(obj.right)].parse_node(obj.right)


class BitAnd:
    @classmethod
    def parse_node(cls, obj):
        pass


class BitOr:
    @classmethod
    def parse_node(cls, obj):
        pass


class BitXor:
    @classmethod
    def parse_node(cls, obj):
        pass


class BoolOp:
    @classmethod
    def parse_node(cls, obj):
        if obj.values:
            for node in obj.values:
                AST_NODES[get_class_str(node)].parse_node(node)


class Break:
    @classmethod
    def parse_node(cls, obj):
        pass


class Bytes:
    @classmethod
    def parse_node(cls, obj):
        pass


class Call:
    @classmethod
    def parse_node(cls, obj):
        if obj.args:
            for node in obj.args:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.keywords:
            for node in obj.keywords:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.func:
            AST_NODES[get_class_str(obj.func)].parse_node(obj.func)


class ClassDef:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.name)
        if obj.bases:
            for node in obj.bases:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.keywords:
            for node in obj.keywords:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.decorator_list:
            for node in obj.decorator_list:
                AST_NODES[get_class_str(node)].parse_node(node)
        #if obj.starargs:
        #    AST_NODES[get_class_str(obj.starargs)].parse_node(obj.starargs)
        #if obj.kwargs:
        #    AST_NODES[get_class_str(obj.kwargs)].parse_node(obj.kwargs)


class Compare:
    @classmethod
    def parse_node(cls, obj):
        if obj.comparators:
            for node in obj.comparators:
                AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(node)].parse_node(node)


class Constant:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.value)


class Continue:
    @classmethod
    def parse_node(cls, obj):
        pass


class Del:
    @classmethod
    def parse_node(cls, obj):
        pass


class Delete:
    @classmethod
    def parse_node(cls, obj):
        if obj.targets:
            for node in obj.targets:
                AST_NODES[get_class_str(node)].parse_node(node)


class Dict:
    @classmethod
    def parse_node(self, obj):
        if obj.keys:
            for node in obj.keys:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.values:
            for node in obj.values:
                AST_NODES[get_class_str(node)].parse_node(node)


class DictComp:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.key)].parse_node(obj.key)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class Div:
    @classmethod
    def parse_node(cls, obj):
        pass


class Ellipsis:
    @classmethod
    def parse_node(cls, obj):
        pass


class Eq:
    @classmethod
    def parse_node(cls, obj):
        pass


class ExceptHandler:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.type)].parse_node(obj.type)
        OBJECTS.append(obj.name)


class Expr:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class Expression:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.body)].parse_node(obj.body)


class ExtSlice:
    @classmethod
    def parse_node(cls, obj):
        pass


class FloorDiv:
    @classmethod
    def parse_node(cls, obj):
        pass


class For:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)


class FormattedValue:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class FunctionDef:
    @classmethod
    def parse_node(cls, obj):
        if obj.args:
            AST_NODES[get_class_str(obj.args)].parse_node(obj.args)
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)
        if obj.decorator_list:
            for node in obj.decorator_list:
                AST_NODES[get_class_str(node)].parse_node(node)
        OBJECTS.append(obj.name)


class FunctionType:
    @classmethod
    def parse_node(cls, obj):
        pass


class GeneratorExp:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)


class Global:
    @classmethod
    def parse_node(cls, obj):
        for name in obj.names:
            OBJECTS.append(name)


class Gt:
    @classmethod
    def parse_node(cls, obj):
        pass


class GtE:
    @classmethod
    def parse_node(cls, obj):
        pass


class If:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)


class IfExp:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)
        AST_NODES[get_class_str(obj.body)].parse_node(obj.body)
        AST_NODES[get_class_str(obj.orelse)].parse_node(obj.orelse)


class Import:
    @classmethod
    def parse_node(cls, obj):
        pass


class ImportFrom:
    @classmethod
    def parse_node(cls, obj):
        pass


class In:
    @classmethod
    def parse_node(cls, obj):
        pass


class Index:
    @classmethod
    def parse_node(cls, obj):
        pass


class Interactive:
    @classmethod
    def parse_node(cls, obj):
        pass


class Invert:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.operand)].parse_node(obj.operand)


class Is:
    @classmethod
    def parse_node(cls, obj):
        pass


class IsNot:
    @classmethod
    def parse_node(cls, obj):
        pass


class JoinedStr:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.values:
            AST_NODES[get_class_str(node)].parse_node(node)


class LShift:
    @classmethod
    def parse_node(cls, obj):
        pass


class Lambda:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.args)].parse_node(obj.args)


class List:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)


class ListComp:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)


class Load:
    @classmethod
    def parse_node(cls, obj):
        pass


class Lt:
    @classmethod
    def parse_node(cls, obj):
        pass


class LtE:
    @classmethod
    def parse_node(cls, obj):
        pass


class MatMult:
    @classmethod
    def parse_node(cls, obj):
        pass


class Mod:
    @classmethod
    def parse_node(cls, obj):
        pass


class Module:
    @classmethod
    def parse_node(cls, obj):
        if obj.body:
            for node in obj.body:
                AST_NODES[get_class_str(node)].parse_node(node)


class Mult:
    @classmethod
    def parse_node(cls, obj):
        pass


class Name:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.id)


class NameConstant:
    @classmethod
    def parse_node(cls, obj):
        pass


class NamedExpr:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)


class NodeTransformer:
    @classmethod
    def parse_node(cls, obj):
        pass


class NodeVisitor:
    @classmethod
    def parse_node(cls, obj):
        pass


class Nonlocal:
    @classmethod
    def parse_node(cls, obj):
        for name in obj.names:
            OBJECTS.append(name)


class Not:
    @classmethod
    def parse_node(cls, obj):
        pass


class NotEq:
    @classmethod
    def parse_node(cls, obj):
        pass


class NotIn:
    @classmethod
    def parse_node(cls, obj):
        pass


class Num:
    @classmethod
    def parse_node(cls, obj):
        pass


class Or:
    @classmethod
    def parse_node(cls, obj):
        pass


class Param:
    @classmethod
    def parse_node(cls, obj):
        pass


class Pass:
    @classmethod
    def parse_node(cls, obj):
        pass


class Pow:
    @classmethod
    def parse_node(cls, obj):
        pass


class RShift:
    @classmethod
    def parse_node(cls, obj):
        pass


class Raise:
    @classmethod
    def parse_node(cls, obj):
        if obj.exec:
            AST_NODES[get_class_str(obj.exec)].parse_node(obj.exec)
        if obj.cause:
            AST_NODES[get_class_str(obj.cause)].parse_node(obj.cause)


class Return:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class Set:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)


class SetComp:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.generators:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.elt)].parse_node(obj.elt)


class Slice:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.lower)].parse_node(obj.lower)
        AST_NODES[get_class_str(obj.upper)].parse_node(obj.upper)
        AST_NODES[get_class_str(obj.step)].parse_node(obj.step)


class Starred:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class Store:
    @classmethod
    def parse_node(cls, obj):
        pass


class Str:
    @classmethod
    def parse_node(cls, obj):
        pass


class Sub:
    @classmethod
    def parse_node(cls, obj):
        pass


class Subscript:
    @classmethod
    def parse_node(cls, obj):
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)
        if obj.slice:
            AST_NODES[get_class_str(obj.slice)].parse_node(obj.slice)


class Suite:
    @classmethod
    def parse_node(cls, obj):
        pass


class Try:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.handlers:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.finalbody:
            AST_NODES[get_class_str(node)].parse_node(node)


class Tuple:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.elts:
            AST_NODES[get_class_str(node)].parse_node(obj.node)


class TypeIgnore:
    @classmethod
    def parse_node(cls, obj):
        pass


class UAdd:
    @classmethod
    def parse_node(cls, obj):
        pass


class USub:
    @classmethod
    def parse_node(cls, obj):
        pass


class UnaryOp:
    @classmethod
    def parse_node(cls, obj):
        AST_NODES[get_class_str(obj.operand)].parse_node(obj.operand)


class While:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.orelse:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.test)].parse_node(obj.test)


class With:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.body:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.items:
            AST_NODES[get_class_str(node)].parse_node(node)


class Yield:
    @classmethod
    def parse_node(cls, obj):
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class YieldFrom:
    @classmethod
    def parse_node(cls, obj):
        if obj.value:
            AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class _ABC:
    @classmethod
    def parse_node(cls, obj):
        pass


class alias:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.name)
        OBJECTS.append(obj.asname)


class arg:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.arg)
        if obj.annotation:
            AST_NODES[get_class_str(obj.annotation)].parse_node(obj.annotation)


class arguments:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.posonlyargs:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.kwonlyargs:
            AST_NODES[get_class_str(node)].parse_node(node)
        for node in obj.args:
            AST_NODES[get_class_str(node)].parse_node(node)
        if obj.vararg:
            AST_NODES[get_class_str(obj.vararg)].parse_node(obj.vararg)
        if obj.kwarg:
            AST_NODES[get_class_str(node.kwarg)].parse_node(node.kwarg)


class boolop:
    @classmethod
    def parse_node(cls, obj):
        pass


class cmpop:
    @classmethod
    def parse_node(cls, obj):
        pass


class comprehension:
    @classmethod
    def parse_node(cls, obj):
        for node in obj.ifs:
            AST_NODES[get_class_str(node)].parse_node(node)
        AST_NODES[get_class_str(obj.target)].parse_node(obj.target)
        AST_NODES[get_class_str(obj.iter)].parse_node(obj.iter)


class excepthandler:
    @classmethod
    def parse_node(cls, obj):
        pass


class expr:
    @classmethod
    def parse_node(cls, obj):
        pass


class expr_context:
    @classmethod
    def parse_node(cls, obj):
        pass


class keyword:
    @classmethod
    def parse_node(cls, obj):
        OBJECTS.append(obj.arg)
        AST_NODES[get_class_str(obj.value)].parse_node(obj.value)


class mod:
    @classmethod
    def parse_node(cls, obj):
        pass


class operator:
    @classmethod
    def parse_node(cls, obj):
        pass


class slice:
    @classmethod
    def parse_node(cls, obj):
        pass


class stmt:
    @classmethod
    def parse_node(cls, obj):
        pass


class type_ignore:
    @classmethod
    def parse_node(cls, obj):
        pass


class unaryop:
    @classmethod
    def parse_node(cls, obj):
        pass


class withitem:
    @classmethod
    def parse_node(cls, obj):
        if obj.context_expr:
            AST_NODES[get_class_str(obj.context_expr)].parse_node(obj.context_expr)
        if obj.optional_vars:
            AST_NODES[get_class_str(obj.optional_vars)].parse_node(obj.optional_vars)


AST_NODES = {
    "ast.AST": AST,
    "ast.Add": Add,
    "ast.And": And,
    "ast.AnnAssign": AnnAssign,
    "ast.Assert": Assert,
    "ast.Assign": Assign,
    "ast.AsyncFor": AsyncFor,
    "ast.AsyncFunctionDef": AsyncFunctionDef,
    "ast.AsyncWith": AsyncWith,
    "ast.Attribute": Attribute,
    "ast.AugAssign": AugAssign,
    "ast.AugLoad": AugLoad,
    "ast.AugStore": AugStore,
    "ast.Await": Await,
    "ast.BinOp": BinOp,
    "ast.BitAnd": BitAnd,
    "ast.BitOr": BitOr,
    "ast.BitXor": BitXor,
    "ast.BoolOp": BoolOp,
    "ast.Break": Break,
    "ast.Bytes": Bytes,
    "ast.Call": Call,
    "ast.ClassDef": ClassDef,
    "ast.Compare": Compare,
    "ast.Constant": Constant,
    "ast.Continue": Continue,
    "ast.Del": Del,
    "ast.Delete": Delete,
    "ast.Dict": Dict,
    "ast.DictComp": DictComp,
    "ast.Div": Div,
    "ast.Ellipsis": Ellipsis,
    "ast.Eq": Eq,
    "ast.ExceptHandler": ExceptHandler,
    "ast.Expr": Expr,
    "ast.Expression": Expression,
    "ast.ExtSlice": ExtSlice,
    "ast.FloorDiv": FloorDiv,
    "ast.For": For,
    "ast.FormattedValue": FormattedValue,
    "ast.FunctionDef": FunctionDef,
    "ast.FunctionType": FunctionType,
    "ast.GeneratorExp": GeneratorExp,
    "ast.Global": Global,
    "ast.Gt": Gt,
    "ast.GtE": GtE,
    "ast.If": If,
    "ast.IfExp": IfExp,
    "ast.Import": Import,
    "ast.ImportFrom": ImportFrom,
    "ast.In": In,
    "ast.Index": Index,
    "ast.Interactive": Interactive,
    "ast.Invert": Invert,
    "ast.Is": Is,
    "ast.IsNot": IsNot,
    "ast.JoinedStr": JoinedStr,
    "ast.LShift": LShift,
    "ast.Lambda": Lambda,
    "ast.List": List,
    "ast.ListComp": ListComp,
    "ast.Load": Load,
    "ast.Lt": Lt,
    "ast.LtE": LtE,
    "ast.MatMult": MatMult,
    "ast.Mod": Mod,
    "ast.Module": Module,
    "ast.Mult": Mult,
    "ast.Name": Name,
    "ast.NameConstant": NameConstant,
    "ast.NamedExpr": NamedExpr,
    "ast.NodeTransformer": NodeTransformer,
    "ast.NodeVisitor": NodeVisitor,
    "ast.Nonlocal": Nonlocal,
    "ast.Not": Not,
    "ast.NotEq": NotEq,
    "ast.NotIn": NotIn,
    "ast.Num": Num,
    "ast.Or": Or,
    "ast.Param": Param,
    "ast.Pass": Pass,
    "ast.Pow": Pow,
    "ast.RShift": RShift,
    "ast.Raise": Raise,
    "ast.Return": Return,
    "ast.Set": Set,
    "ast.SetComp": SetComp,
    "ast.Slice": Slice,
    "ast.Starred": Starred,
    "ast.Store": Store,
    "ast.Str": Str,
    "ast.Sub": Sub,
    "ast.Subscript": Subscript,
    "ast.Suite": Suite,
    "ast.Try": Try,
    "ast.Tuple": Tuple,
    "ast.TypeIgnore": TypeIgnore,
    "ast.UAdd": UAdd,
    "ast.USub": USub,
    "ast.UnaryOp": UnaryOp,
    "ast.While": While,
    "ast.With": With,
    "ast.Yield": Yield,
    "ast.YieldFrom": YieldFrom,
    "ast._ABC": _ABC,
    "ast.alias": alias,
    "ast.arg": arg,
    "ast.arguments": arguments,
    "ast.boolop": boolop,
    "ast.cmpop": cmpop,
    "ast.comprehension": comprehension,
    "ast.excepthandler": excepthandler,
    "ast.expr": expr,
    "ast.expr_context": expr_context,
    "ast.keyword": keyword,
    "ast.mod": mod,
    "ast.operator": operator,
    "ast.slice": slice,
    "ast.stmt": stmt,
    "ast.type_ignore": type_ignore,
    "ast.unaryop": unaryop,
    "ast.withitem": withitem,
}