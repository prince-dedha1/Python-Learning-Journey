import random

# Run an infinite loop until the user chooses to stop
while True:
    optn = input('Enter whether you want to code or decode message (write "0" to stop): ').lower()

    # Exit condition
    if optn == "0":
        print("Program stopped.")
        break

    # Encoding block
    elif optn == "code":
        to_code = input("Enter your message to code:\n")
        word_lst = to_code.split()
        coded_msg = ""

        for word in word_lst:
            # If word length < 3, just reverse it
            if len(word) < 3:
                coded_msg += word[::-1] + " "
            else:
                # Generate random 3-letter prefix
                prefix = ""
                for i in range(3):
                    x = random.randint(1, 26)
                    prefix += chr(64 + x).lower()

                # Move first letter of the word to the end and add prefix/suffix
                encoded_core = word[1:] + word[0]

                # Generate random 3-letter suffix
                suffix = ""
                for k in range(3):
                    y = random.randint(1, 26)
                    suffix += chr(64 + y).lower()

                # Combine prefix + encoded core + suffix
                coded_msg += prefix + encoded_core + suffix + " "

        print(f"Your coded message is {coded_msg.strip()}")

    # Decoding block
    elif optn == "decode":
        to_decode = input("Enter the message that you want to decode:\n")
        word_lst = to_decode.split()
        decoded_message = ""

        for word in word_lst:
            # If word length < 3, just reverse it back
            if len(word) < 3:
                decoded_message += word[::-1] + " "
            else:
                # Remove 3 random letters from start and end
                core_word = word[3:-3]
                # Move last letter to front to get original word
                decoded_message += core_word[-1] + core_word[:-1] + " "

        print(f"Your Decoded message is {decoded_message.strip()}")

    # Invalid input handling
    else:
        print("Please enter a valid input (code / decode / 0).")
