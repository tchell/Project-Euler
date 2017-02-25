# Project Euler - Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    # repeat until all three digit numbers are multiplied
    x = 100

    while x < 1000:
        y = 100
        while y < 1000:
            # Multiply two 3 digit numbers
            product = x * y

            # check if the product is a palindrome
            product_string = str(product)
            product_len = len(product_string)
                # if a palindrome and larger than the previous, store it over the previous
                    continue
                else:
                    break


            y += 1

        x += 1


main()
