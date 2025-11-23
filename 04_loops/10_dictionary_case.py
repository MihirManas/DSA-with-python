users = [
    {"id" : 1, "Total": 100, "coupon": "P10"},
    {"id" : 2, "Total": 150, "coupon": "F18"},
    {"id" : 3, "Total": 200, "coupon": "P20"},
]

discount = {
    "P10": (0.10, 0),
    "P20": (0.20, 0),
    "F18": (0, 18)
}

for user in users:
    percent, fixed = discount.get(user["coupon"], (0,0))
    discount = user["Total"] * percent + fixed
    print(f"User {user['id']} has a total of {user['Total']}, with coupon {user['coupon']} gets discount of {discount}")