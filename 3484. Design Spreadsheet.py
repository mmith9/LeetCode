from collections import defaultdict

#simple
class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        a,b = formula[1:].split('+')
        a = int(a) if a[0].isnumeric() else self.cells[a]
        b = int(b) if b[0].isnumeric() else self.cells[b]
        return a+b

#Naive
class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = defaultdict(lambda: defaultdict(int))
        self.max_row = rows

    def setCell(self, cell: str, value: int) -> None:
        self.rows[cell[1:]][cell[0]] = value

    def resetCell(self, cell: str) -> None:
        row = cell[1:]; col = cell[0]
        if row in self.rows:
            if col in self.rows[row]:
                del self.rows[row][col]                
            if not self.rows[row]:
                del self.rows[row]

    def getValue(self, formula: str) -> int:
        a,b = formula[1:].split('+')
        if a[0].isnumeric():
            a = int(a)
        else:
            a = self.rows[a[1:]][a[0]]

        if b[0].isnumeric():
            b = int(b)
        else:
            b = self.rows[b[1:]][b[0]]

        return a+b

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)