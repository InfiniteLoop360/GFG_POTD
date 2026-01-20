class Solution:
    def __init__(self):
        self.doc = []        # document content
        self.undo_stack = [] # stack for undo
        self.redo_stack = [] # stack for redo

    def append(self, x):
        self.doc.append(x)
        self.undo_stack.append(x)
        self.redo_stack.clear()

    def undo(self):
        if self.doc:
            ch = self.doc.pop()
            self.redo_stack.append(ch)

    def redo(self):
        if self.redo_stack:
            ch = self.redo_stack.pop()
            self.doc.append(ch)
            self.undo_stack.append(ch)

    def read(self):
        return "".join(self.doc)
