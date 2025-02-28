def decrypt_code(encrypted_code):
    """
    Decrypt the encrypted code by interchanging each consecutive digit.

    Args:
        encrypted_code (str): The encrypted code.

    Returns:
        str: The decrypted code.
    """
    decrypted_code = ""
    i = 0
    while i < len(encrypted_code):
        if i + 1 < len(encrypted_code):
            decrypted_code += encrypted_code[i + 1] + encrypted_code[i]
            i += 2
        else:
            decrypted_code += encrypted_code[i]
            i += 1
    return decrypted_code


encrypted_code = "123456"
print("Encrypted Code:", encrypted_code)
print("Decrypted Code:", decrypt_code(encrypted_code))