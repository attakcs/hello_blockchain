from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # it should create the same hash, regardless of
    # the args data type and the order.
    assert crypto_hash(1, [2], 'three') == crypto_hash([2], 'three', 1)