"""订单金额计算（装配联调用）。"""


def solve(payload):
    """按 sku 单价 × 数量算金额，满 200 减 20，未知 sku 报错。

    payload: {"skuId": "sku_ai_tiao", "count": 2}
    返回: {"amount": 98, "discount": 0, "total": 98}
    """
    prices = {"sku_ai_tiao": 49, "sku_pen": 12, "sku_book": 35}
    sku = (payload or {}).get("skuId")
    count = int((payload or {}).get("count") or 0)
    if sku not in prices:
        raise ValueError("未知商品: %r" % (sku,))
    if count <= 0:
        raise ValueError("数量必须为正")
    amount = prices[sku] * count
    discount = 20 if amount >= 200 else 0
    return {"amount": amount, "discount": discount, "total": amount - discount}
