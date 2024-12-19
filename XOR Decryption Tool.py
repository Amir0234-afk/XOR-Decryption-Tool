import base64
import binascii


def decode_base64_to_hex(ciphertext: str) -> str:
    """
    Decodes a Base64 string into ASCII-encoded hexadecimal representation.
    """
    decoded_bytes = base64.b64decode(ciphertext)
    ascii_hex = decoded_bytes.decode('ascii')
    return ascii_hex


def ascii_to_hex(ascii_string: str) -> str:
    """
    Converts an ASCII string into its hexadecimal representation.
    """
    return ''.join(format(ord(char), '02x') for char in ascii_string)


def divide_hex_into_blocks(hex_string: str, block_size: int) -> list:
    """
    Divides a hexadecimal string into blocks of a specified size.
    """
    return [hex_string[i:i + block_size] for i in range(0, len(hex_string), block_size)]


def xor_bytes(byte_sequence1: bytes, byte_sequence2: bytes) -> bytes:
    """
    XORs two byte sequences while restricting the result to ASCII-compatible values.
    """
    return bytes((b1 ^ b2) & 0x7F for b1, b2 in zip(byte_sequence1, byte_sequence2))


def derive_key(first_block: str, hex_flag: str) -> bytes:
    """
    Derives the XOR key by XORing the first block with the hexadecimal flag.
    """
    first_block_bytes = binascii.unhexlify(first_block)
    flag_bytes = binascii.unhexlify(hex_flag)
    return xor_bytes(flag_bytes, first_block_bytes)


def decrypt_blocks(blocks: list, key: bytes) -> bytes:
    """
    Decrypts a list of blocks using the provided XOR key.
    """
    decrypted_data = b""
    for block in blocks:
        block_bytes = binascii.unhexlify(block)
        decrypted_data += xor_bytes(key, block_bytes)
    return decrypted_data


def main():
    """
    Main function for the XOR Decryption Tool.
    """
    print("=" * 50)
    print("Welcome to the XOR Decryption Tool")
    print("=" * 50)

    # Input ciphertext and flag
    ciphertext = input("\nEnter the Base64-encoded ciphertext: ").strip()
    flag = input("\nEnter the ASCII incomplete plaintext: ").strip()

    # Convert inputs into the necessary formats
    hex_ciphertext = decode_base64_to_hex(ciphertext)
    hex_flag = ascii_to_hex(flag)

    # Divide ciphertext into blocks
    block_size = len(hex_flag)
    hex_blocks = divide_hex_into_blocks(hex_ciphertext, block_size)

    # Derive the XOR key using the first block and the flag
    xor_key = derive_key(hex_blocks[0], hex_flag)

    # Decrypt the remaining blocks
    decrypted_data = decrypt_blocks(hex_blocks[1:], xor_key)

    # Combine the flag and decrypted data
    final_result = binascii.unhexlify(hex_flag) + decrypted_data

    # Display the result
    print("\n" + "-" * 50)
    print("Decrypted message:")
    print(final_result.decode('ascii'))
    print("-" * 50)

    # Wait for a key press before exiting
    input("\nPress any key to close.")


if __name__ == "__main__":
    main()
