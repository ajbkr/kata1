class CheckOut():
    PRICES = {
        'A': 50,
        'a': 130,  # AAA -> a
        'B': 30,
        'b': 45,  # BB -> b
        'C': 20,
        'D': 15,
    }

    def __init__(self):
        self._items = ''

    def scan(self, item: str) -> None:
        self._items += item

    def total(self) -> int:
        return sum([
            # group SKUs consecutively: ABAB -> AABB then...
            # get price for each SKU; default to 0
            CheckOut.PRICES.get(sku, 0) for sku in ''.join(sorted(self._items))
            # substitute 3 item As with multiprice SKU for item A (a)
            .replace('AAA', 'a')
            # substitute 2 item Bs with multiprice SKU for item B (b)
            .replace('BB', 'b')
        ], 0)  # initial subtotal = 0


def price(items: list) -> int:
    co = CheckOut()

    for item in items:
        co.scan(item)

    return co.total()
