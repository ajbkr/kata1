# Kata 1
Implement the code for a checkout system that handles pricing schemes such as `apples cost 50p, three apples cost £1.30`.

Let’s implement the code for a supermarket checkout that calculates the total price of a number of items. In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. In our store, we’ll use individual letters of the alphabet (A, B, C, and so on). Our goods are priced individually. In addition, some items are multipriced: buy n of them, and they’ll cost you y. For example, item ‘A’ might cost 50p individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you £1.30. In fact this week's prices are:

| Item | Unit Price | Special Price |
| ---- | ---------- | ------------- |
| A    | 50         | 3 for 130     |
| B    | 30         | 2 for 45      |
| C    | 20         |               |
| D    | 15         |               |

To run:

```python
python3 test.py
```

You can modify anything in the main.py file, however you will need to keep the interface of the `price(items: list) -> int:` function in order for the tests to work.
