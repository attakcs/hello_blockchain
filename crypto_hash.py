import hashlib
import json

# for stringify data, 'json' has been imported
# def stringify(data):
#     return json.dumps(data)

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    # map() applying the given function to each item of a given iterable
    # lambda is a anonymous function for a single expression.
    stringified_args = sorted(map(lambda data : json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    # encode() : Converts the string into bytes to be acceptable by hash function.
    # hexdigest() : Returns the encoded data in hexadecimal format.
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(
        f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])} ")
    print(
        f"crypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])} ")

if __name__ == "__main__":
    main()
