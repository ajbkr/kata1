class CheckOut():
    def scan(self, item: str) -> None:
        pass

    def total(self) -> int:
        return 0


def price(items: list) -> int:
    co = CheckOut()

    for item in items:
        co.scan(item)

    return co.total()
