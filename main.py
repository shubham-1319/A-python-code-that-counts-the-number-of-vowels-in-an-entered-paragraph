#made by shubham
def count_vowels(paragraph):
    # Convert the paragraph to lowercase to simplify the vowel check
    paragraph = paragraph.lower()
    
    # Define vowels
    vowels = "aeiou"
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the paragraph
    for char in paragraph:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Get user input for the paragraph
user_paragraph = input("Enter a paragraph: ")

# Call the function to count vowels
result = count_vowels(user_paragraph)

# Display the result
print(f"Number of vowels in the paragraph: {result}")
