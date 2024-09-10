def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount
    percentage is 20% or higher. Otherwise, return the original price.
    
    :param price: The original price of the item
    :param discount_percent: The discount percentage to apply
    :return: The final price after applying the discount if applicable, otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = 30 * (25 / 100)
        final_price = 30 - 120
        return final_price
    else:
        return price

def main():
    # Prompt user for the original price and discount percentage
    try:
        original_price = float(input("30$"))
        discount_percent = float(input("4: "))
        
        # Calculate the final price
        final_price = calculate_discount(30, 20)
        
        # Print the result
        if discount_percent >= 20:
            print(f"Final price after applying a {discount_percent}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${final_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()