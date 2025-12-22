""" Build a cart system using composition.
Requirements:
    Create class Product → name, price, category
    Create class Cart → contains list of Product objects
Implement methods:
    add_product(product)
    remove_product(product_name)
    get_total_price()
    apply_coupon(code)
Coupons:
    "NEW10" → 10% off
    "FLAT50" → ₹50 off
Show final bill with discount applied. """


class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

    def __str__(self):
        return f"{self.name} ({self.category}) - ₹ {self.price}"
        
class Cart:

    # list of items
    # concept of composition is used cart holds the object of product class
    def __init__(self):
        self.items=[]
        self.discount=0
        self.coupon_code=None

    #  add items to the list 
    def add_products(self,Product):
        self.items.append(Product)
        print("item added")
        return True

    #  remove items from the list

    def remove_product(self,Product):
         if Product in self.items:
            self.items.remove(Product)
            print("item removed")
            return True
         return False
        
    # getting the total price
    def get_total_price(self):
        return sum(Product.price for Product in self.items)

    
    def apply_coupons(self,code):
        code=code.upper()
        subtotal= self.get_total_price()

        if code== "NEW10":
            self.discount=0.10*subtotal
            self.coupon_code=code
            return True
        
        elif code== "FLAT50":
            self.discount=50
            self.coupon_code=code
            return True
        
        else:
            self.discount = 0
            self.coupon_code = None
            return False

         
    def show_bill(self):
        print("="*30)
        print("FINAL BILL")

        if not self.items:
            print("cart is empty")

        for Product in self.items:
            print(Product) # minimal polymorphism call the __str__ function

    
        subtotal=self.get_total_price()
        discount=min(self.discount,subtotal)
        final_total= subtotal-discount
        print("="*30)
        print(f"Subtotal: ₹{subtotal:.2f}")

        # coupon info

        if self.coupon_code:
            print(f"coupon  applied: {self.coupon_code}")
            print(f"Discount: -INR {discount:.2f}")

        else:
            print(f"coupon applied: NONE")
            print(f"Discount: - INR {0.00}")
        
        print(f"finaltotal: INR {final_total:.2f}")


# creating objects

p1=Product("Milk",35,"grocery")
p2=Product("detergent",35,"grocery")
cart=Cart()

cart.add_products(p1)
cart.add_products(p2)
cart.remove_product(p2)
cart.get_total_price()
cart.apply_coupons("NEW10")
cart.show_bill()

# oops concept used 

# 1. class and object 
# 2. encapsulation
# 3. composition
# 4. polymorphism
# 5. abstraction minimal 
        







