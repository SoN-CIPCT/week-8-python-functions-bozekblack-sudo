def make_sandwich(*ingredients):
    """Print the list of ingredients that have been requested for the sandwich."""
    print("\nMaking a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print("Your sandwich is ready!")
make_sandwich("Turkey", "Lettuce", "Cheese", "Mayo")
make_sandwich("Peanut Butter", "Jelly")