# 1597. Build Binary Expression Tree From Infix Expression

(https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/864596/Python-Standard-parser-implementation)

```python
class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]

    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft() # consume '('
            node = self.parse_expression(tokens)
            tokens.popleft() # consume ')'
            return node
        else:
            # Single operand
            token = tokens.popleft()
            return Node(val=token)
```