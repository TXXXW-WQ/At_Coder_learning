class Spreadsheet:

    def __init__(self, rows: int):
        self.sp = {}

    def setCell(self, cell: str, value: int) -> None:
        self.sp[cell] = value

    def resetCell(self, cell: str) -> None:
        del self.sp[cell]

    def getValue(self, formula: str) -> int:
        i = formula.index("+")
        p1 = formula[1:i]
        p2 = formula[i+1:]
        val1 = self.sp.get(p1,0) if p1[0].isalpha() else int(p1)
        val2 = self.sp.get(p2,0) if p2[0].isalpha() else int(p2)

        return val1 + val2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)