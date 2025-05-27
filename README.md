# 🐍 Python Function Practice and File Handling

This project demonstrates basic Python function usage, calculating sums and averages, checking for odd/even numbers, and reading Excel files using `pandas`.

---

## 📘 Contents

### 🔹 1. Sum of Two Numbers

```python
def sum_val(a, b):
    sum = a + b
    return sum

result = sum_val(10, 20)
print(result)  # Output: 30

###  A basic function that prints a greeting.

def vikas():
    print("hello vikas")

vikas()



def avrage(a, b, c, d):
    sum = a + b + c + d
    avrage = sum / 4
    print("The average of the numbers is", avrage)
    return avrage

result = avrage(10, 20, 30122, 30)
print(result)



###  This function takes four numbers, calculates their average, prints it, and returns the result.


# def odd_even():
#     num = int(input("Enter the number: "))
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
#
# odd_even()
