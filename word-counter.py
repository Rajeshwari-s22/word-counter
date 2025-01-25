def count_words(text):
    """
    Function to count the number of words in the given text.
    :param text: The input text (str) provided by the user.
    :return: Integer representing the word count.
    """
    # Splitting the text into words based on spaces
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input, process word count, and display the result.
    """
    print("Welcome to the Word Counter Program!")
    print("=====================================")
    
    # Prompting user input
    text = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not text:
        print("Error: No input provided. Please enter valid text.")
        return
    
    # Calling the word count function
    word_count = count_words(text)
    
    # Displaying the word count
    print(f"The number of words in the given text is: {word_count}")
    print("Thank you for using the Word Counter Program!")

if __name__ == "__main__":
    main()
