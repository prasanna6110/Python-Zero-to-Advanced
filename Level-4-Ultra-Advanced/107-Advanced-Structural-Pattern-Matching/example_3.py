# 107 · Advanced Structural Pattern Matching — Example 3: A tiny expression evaluator using matching
# Run: python example_3.py

from dataclasses import dataclass

@dataclass
class Num:
    value: float
@dataclass
class BinOp:
    op: str
    left: object
    right: object
@dataclass
class Neg:
    operand: object

def evaluate(node):
    match node:
        case Num(v):
            return v
        case Neg(operand):
            return -evaluate(operand)
        case BinOp("+", l, r): return evaluate(l) + evaluate(r)
        case BinOp("-", l, r): return evaluate(l) - evaluate(r)
        case BinOp("*", l, r): return evaluate(l) * evaluate(r)
        case BinOp("/", l, Num(0)): raise ZeroDivisionError("division by literal zero")
        case BinOp("/", l, r): return evaluate(l) / evaluate(r)
        case _: raise ValueError(f"bad node {node}")

def simplify(node):
    match node:
        case BinOp("*", x, Num(1)) | BinOp("*", Num(1), x): return simplify(x)
        case BinOp("+", x, Num(0)) | BinOp("+", Num(0), x): return simplify(x)
        case BinOp(op, l, r): return BinOp(op, simplify(l), simplify(r))
        case _: return node

expr = BinOp("+", BinOp("*", Num(4), Num(1)), Neg(BinOp("+", Num(2), Num(0))))
print(evaluate(expr), "| simplified:", simplify(expr))
