XOR Decryption Tool

This Python script is a simple XOR decryption tool that takes a Base64-encoded ciphertext and an ASCII incomplete plaintext to decrypt a message. It uses the XOR operation and assumes that the plaintext can help derive the decryption key.

Features

Converts Base64-encoded ciphertext to hexadecimal.

Derives the XOR key using an incomplete plaintext.

Decrypts the ciphertext block by block.

Outputs the final decrypted message.

Requirements

Python 3.x

Installation

Clone this repository and ensure you have Python installed on your system.

# Clone the repository
git clone <repository-url>
cd <repository-directory>

Usage

Run the script using Python:

python xor_decryption_tool.py

Inputs

Base64-encoded ciphertext: The encoded ciphertext you want to decrypt.

ASCII incomplete plaintext: The known part of the plaintext that helps derive the key.

Example

When prompted, provide:

Base64-encoded ciphertext.

ASCII incomplete plaintext.

The script will output the decrypted message.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Feel free to open issues or submit pull requests to improve the tool.

Disclaimer

This tool is for educational purposes only. Use it responsibly and ensure you have permission to decrypt any ciphertext.

Contact

For any questions, reach out to the repository owner.
