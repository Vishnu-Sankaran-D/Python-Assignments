# Online Shopping Discount Eligibility

# Get input from the user
amount = float(input("Enter the order amount: ₹"))
membership = input("Are you a member? (yes/no): ").strip().lower()

# Validate order amount
if amount < 0 or amount > 100000:
    print("\nInvalid order amount!")

else:
    # Determine discount
    if amount >= 5000:
        discount = 15

    elif membership == "yes" and amount >= 2000:
        discount = 10

    else:
        discount = 0

    # Calculate discount and final amount
    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount

    # Display results
    print("\n----- Shopping Discount Details -----")
    print("Original Amount: ₹", amount)
    print("Membership Status:", membership)
    print("Discount Percentage:", discount, "%")
    print("Discount Amount: ₹", discount_amount)
    print("Final Payable Amount: ₹", final_amount)

    if discount > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: Not eligible for discount")
