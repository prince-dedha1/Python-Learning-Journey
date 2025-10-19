# 🔐 Message Encoder & Decoder (Beginner Python Project)

A simple text-based Python project that encodes and decodes secret messages using basic string manipulation and randomization.

---

## 🚀 Features

- Encode any message into a coded form  
- Decode your message back to its original text  
- Automatically handles short words (<3 letters)  
- Random letters are added for obfuscation  
- Fully interactive command-line tool  

---

## 🧩 How It Works

1. **Coding (Encryption):**
   - For words shorter than 3 letters → reverses the word.
   - For longer words →  
     - Adds 3 random letters at the start and end.  
     - Moves the first letter of the word to the end.

   Example:  
   ```
   hello → abchelloaxy → encoded
   ```

2. **Decoding (Decryption):**
   - Removes random letters (first 3 and last 3).  
   - Moves the last letter back to the front.  
   - Reconstructs the original sentence.

---

## 🧠 Example Usage

```
Enter whether you want to code or decode message (write "0" to stop): code
Enter your message to code:
hello world
Your coded message is: abcellohaef xyzorldwqrs
```

```
Enter whether you want to code or decode message (write "0" to stop): decode
Enter the message that you want to decode:
abcellohaef xyzorldwqrs
Your Decoded message is: hello world
```

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Modules Used:** `random` (for random letters)

---

## 💡 Future Ideas

- Add option to save encoded messages to a file  
- Add GUI using `tkinter` or `PyQt`  
- Option to set custom prefix/suffix length  
- Password-based encoding logic  

---

## 👨‍💻 Author
**Prince Dedha**  
Beginner Python developer learning by building fun projects.

---

## ⚙️ How to Run

1. Clone this repository  
2. Open terminal in the folder  
3. Run:  
   ```
   python message_encoder_decoder.py
   ```

---

## 🏷️ License

This project is open-source. Feel free to modify and improve it.

---