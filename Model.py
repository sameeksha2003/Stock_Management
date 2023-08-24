from dataclasses import dataclass


@dataclass
class Product:
    pid: str
    pname: str
    price: float
    stock: int


class Pen(Product):
    def __init__(self, pid, pname, price, stock):
        super().__init__("P1", pname, price, stock)


class Pencil(Product):
    def __init__(self, pid, pname, price, stock):
        super().__init__("P2", pname, price, stock)


class Eraser(Product):
    def __init__(self, pid, pname, price, stock):
        super().__init__("P3", pname, price, stock)
        self.pid = "P3"


class Scale(Product):
    def __init__(self, pid, pname, price, stock):
        super().__init__("P4", pname, price, stock)


class Sharpener(Product):
    def __init__(self, pid, pname, price, stock):
        super().__init__("P5", pname, price, stock)
