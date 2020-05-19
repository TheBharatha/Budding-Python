class StockSpanner:

    def __init__(self):
        self.stock = list()
        

    def next(self, price: int) -> int:
        stock, span = self.stock, 1
        while stock and stock[-1][0] <= price:
            span += stock[-1][1]
            stock.pop()
        stock.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
