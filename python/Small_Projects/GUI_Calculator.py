#!/usr/bin/env python3
"""
calculator.py
Simple desktop calculator using Tkinter with a safe expression evaluator.
Features:
 - Buttons for digits, + - * / %, parentheses, ., =, C (clear), ← (backspace)
 - Keyboard support for digits, operators, Enter, Backspace, Escape (clear)
 - Safe evaluation using Python ast (only arithmetic nodes allowed)
"""

import tkinter as tk
from tkinter import ttk
import ast
import operator

# ---------- Safe evaluator ----------
# Allows only arithmetic operations and parentheses
_allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


class EvalError(Exception):
    pass


def safe_eval(expr: str):
    """
    Evaluate arithmetic expression safely using ast.
    Supports: +, -, *, /, %, **, unary +/-, parentheses, numbers.
    Raises EvalError on invalid input or math errors.
    """
    try:
        node = ast.parse(expr, mode="eval")
    except Exception as e:
        raise EvalError("Invalid expression") from e

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):  # Python 3.8+: numbers are Constant
            if isinstance(node.value, (int, float)):
                return node.value
            raise EvalError("Only numbers allowed")
        if isinstance(node, ast.Num):  # compatibility
            return node.n
        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in _allowed_operators:
                raise EvalError("Operator not allowed")
            left = _eval(node.left)
            right = _eval(node.right)
            try:
                return _allowed_operators[op_type](left, right)
            except Exception as e:
                raise EvalError("Math error") from e
        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in _allowed_operators:
                raise EvalError("Operator not allowed")
            operand = _eval(node.operand)
            return _allowed_operators[op_type](operand)
        if isinstance(node, ast.Call):
            raise EvalError("Function calls not allowed")
        raise EvalError("Expression not allowed")

    return _eval(node)


# ---------- GUI ----------
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(padx=8, pady=8)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.entry_var = tk.StringVar()
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        # Display
        entry = ttk.Entry(self, textvariable=self.entry_var, font=(
            "Segoe UI", 20), justify="right", width=24)
        entry.grid(row=0, column=0, columnspan=4, sticky="we", pady=(0, 8))
        entry.focus_set()

        # Button layout
        btns = [
            ("C", self._clear), ("(", lambda: self._add_text("(")), (")",
                                                                     lambda: self._add_text(")")), ("←", self._backspace),
            ("7", lambda: self._add_text("7")), ("8", lambda: self._add_text(
                "8")), ("9", lambda: self._add_text("9")), ("/", lambda: self._add_text("/")),
            ("4", lambda: self._add_text("4")), ("5", lambda: self._add_text(
                "5")), ("6", lambda: self._add_text("6")), ("*", lambda: self._add_text("*")),
            ("1", lambda: self._add_text("1")), ("2", lambda: self._add_text(
                "2")), ("3", lambda: self._add_text("3")), ("-", lambda: self._add_text("-")),
            ("0", lambda: self._add_text("0")), (".", lambda: self._add_text(
                ".")), ("%", lambda: self._add_text("%")), ("+", lambda: self._add_text("+")),
            ("=", self._calculate),
        ]

        # Place buttons in grid
        r = 1
        c = 0
        for label, cmd in btns:
            if label == "=":
                btn = ttk.Button(self, text=label, command=cmd)
                btn.grid(row=r, column=c, columnspan=4,
                         sticky="nsew", padx=4, pady=4)
                r += 1
                c = 0
                continue
            btn = ttk.Button(self, text=label, command=cmd)
            btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
            c += 1
            if c > 3:
                c = 0
                r += 1

        # make buttons expand evenly
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(1, r+1):
            self.grid_rowconfigure(i, weight=1)

    def _add_text(self, txt: str):
        cur = self.entry_var.get()
        self.entry_var.set(cur + txt)

    def _clear(self):
        self.entry_var.set("")

    def _backspace(self):
        cur = self.entry_var.get()
        self.entry_var.set(cur[:-1])

    def _calculate(self):
        expr = self.entry_var.get().strip()
        if not expr:
            return
        try:
            # Replace unicode division sign if any, just in case
            safe_expr = expr.replace("÷", "/").replace("×", "*")
            result = safe_eval(safe_expr)
            # Format result: show int if whole number
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.entry_var.set(str(result))
        except EvalError as e:
            self.entry_var.set("Error")
        except Exception:
            self.entry_var.set("Error")

    def _bind_keys(self):
        # digits and operators
        for key in "0123456789+-*/().%":
            self.bind(f"<Key-{key}>", lambda e, k=key: self._add_text(k))
        # decimal with period
        self.bind("<Key-.>", lambda e: self._add_text("."))
        self.bind("<Return>", lambda e: self._calculate())
        self.bind("<KP_Enter>", lambda e: self._calculate())
        self.bind("<BackSpace>", lambda e: self._backspace())
        self.bind("<Escape>", lambda e: self._clear())
        # allow Ctrl+C to copy selection from entry
        self.bind_all("<Control-c>", lambda e: self.event_generate("<<Copy>>"))


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
