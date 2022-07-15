from cryptography.fernet import Fernet

decryption_key = "d82sX4d-y9G0bS7utB1-S3efbvQZO0JqWe6WT5KRnzs="
system_information_e = "e_system.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_logged.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]

for index, decrypt_file in enumerate(encrypted_files):

    with open(encrypted_files[index], 'rb') as f:
        data = f.read()

    fernet = Fernet(decryption_key)
    decrypted_data = fernet.decrypt(data)

    with open(encrypted_files[index], 'wb') as f:
        f.write(decrypted_data)
