def count_words(input_text):
    """
    Count the number of words in the given text.
 
    Args:
        input_text (str): The input text to analyze.
 
    Returns:
        int: Number of words in the input text.
    """
    # Check for empty input
    if not input_text.strip():
        raise ValueError("Error: Empty input. Please enter a sentence or paragraph.")
 
    # Split the input text into words
    words = input_text.split()
 
    return len(words)
 
def main():
    try:
        # Prompt user for input
        user_input = input("Enter a sentence or paragraph: ")
 
        # Calculate word count using the defined function
        word_count = count_words(user_input)
 
        # Display the word count
        print("Word count:", word_count)
 
    except ValueError as ve:
        # Handle errors (e.g., empty input)
        print(ve)
 
if __name__ == "__main__":
    # Run the main function
    main()