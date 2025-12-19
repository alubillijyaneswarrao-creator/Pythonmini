def add(**args):
    return sum(args.values())
print(add(a=1, b=2, c=3 ,d=4))

def address(**kwargs):
    return ', '.join(f"{key}: {value}" for key, value in kwargs.items())
print(address(street="123 Main St", city="Anytown", state="CA", zip="12345"))