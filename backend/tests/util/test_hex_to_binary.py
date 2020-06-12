from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_number = 666
    # [2:] cuts off the 0x prefix 
    hex_number = hex(original_number)[2:]
    binary_number = hex_to_binary(hex_number)

    assert int(binary_number, 2) == original_number
