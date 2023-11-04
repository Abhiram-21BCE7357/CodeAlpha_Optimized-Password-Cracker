import hashlib
import pyfiglet
import sys
import click

def crack_hash(hash_type, wordlist_location, hash_to_crack):
    """
    Crack a hash using the specified hash type and wordlist.
    """
    # Define a dictionary to map hash types to hashlib functions
    hash_algorithms = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA224": hashlib.sha224,
        "SHA512": hashlib.sha512,
        "SHA384": hashlib.sha384,
    }

    # Check if the selected hash type is valid
    if hash_type not in hash_algorithms:
        print("Invalid hash type. Please choose from the given options.")
        return

    try:
        with open(wordlist_location, "r") as word_list_file:
            for word in word_list_file:
                word = word.strip()  # Remove trailing newline
                # Calculate the hash of the word using the selected hash algorithm
                hash_object = hash_algorithms[hash_type](word.encode('utf-8'))
                hashed = hash_object.hexdigest()
                # Check if the calculated hash matches the target hash
                if hash_to_crack == hashed:
                    return word
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_location}")

    return None

@click.command()
@click.option('--hash-type', prompt="Hash type (MD5/SHA1/SHA224/SHA512/SHA384)", type=click.Choice(['MD5', 'SHA1', 'SHA224', 'SHA512', 'SHA384']))
@click.option('--wordlist', prompt="Wordlist location", type=click.Path(exists=True))
@click.option('--target-hash', prompt="Target hash")
def main(hash_type, wordlist, target_hash):
    """
    Hash Cracker: Crack a hash using a wordlist.
    """
    ascii_banner = pyfiglet.figlet_format("Hash Cracker")
    print(ascii_banner)
    
    result = crack_hash(hash_type, wordlist, target_hash)
    
    if result:
        print(f"\033[1;32m HASH FOUND: {result}\n")
    else:
        print("Hash not found in the wordlist.")

if __name__ == "__main__":
    main()
