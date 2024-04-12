import heapq

class StockPrice:
    def __init__(self):
        self.prices = {}
        self.max_heap = []
        self.min_heap = []
    def update(self, timestamp, price):
        self.prices[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
    def current(self):
        return self.prices[max(self.prices.keys())]
    def maximum(self):
        while True:
            price, timestamp = heapq.heappop(self.max_heap)
            if timestamp in self.prices and self.prices[timestamp] == -price:
                heapq.heappush(self.max_heap, (price, timestamp))
                return -price
    def minimum(self):
        while True:
            price, timestamp = heapq.heappop(self.min_heap)
            if timestamp in self.prices and self.prices[timestamp] == price:
                heapq.heappush(self.min_heap, (price, timestamp))
                return price
inputs = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
values = [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
stockPrice = None
output = []
for i in range(len(inputs)):
    if inputs[i] == "StockPrice":
        stockPrice = StockPrice()
        output.append(None)
    elif inputs[i] == "update":
        stockPrice.update(values[i][0], values[i][1])
        output.append(None)
    elif inputs[i] == "current":
        output.append(stockPrice.current())
    elif inputs[i] == "maximum":
        output.append(stockPrice.maximum())
    elif inputs[i] == "minimum":
        output.append(stockPrice.minimum())

print("Output:", output)
