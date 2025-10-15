class product :
    def __init__(self, name="codetree", code="50") :
        self.name = name
        self.code = code
product1 = product()
print(f"product {product1.code} is {product1.name}")
product_name, product_code = input().split()
product_code = int(product_code)

product2 = product(product_name, product_code)
print(f"product {product2.code} is {product2.name}")