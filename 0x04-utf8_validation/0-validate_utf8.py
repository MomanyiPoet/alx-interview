#!/usr/bin/pyhon3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Loop through each integer in the data list
    for num in data:
        # Get the binary representation of the current byte
        binary = format(num, '#010b')[-8:]
        
        # If the current byte is part of a UTF-8 character...
        if num_bytes > 0:
            # If the current byte does not start with the bit pattern "10", it's not a valid continuation byte
            if not binary.startswith("10"):
                return False
            
            # Decrement the number of bytes remaining in the current UTF-8 character
            num_bytes -= 1
        else:
            # Count the number of bytes in the current UTF-8 character based on the leading bits
            if binary.startswith("0"):
                num_bytes = 0
            elif binary.startswith("110"):
                num_bytes = 1
            elif binary.startswith("1110"):
                num_bytes = 2
            elif binary.startswith("11110"):
                num_bytes = 3
            else:
                # Invalid leading bits
                return False
    
    # If we have any remaining bytes in the current UTF-8 character, it's not a valid encoding
    return num_bytes == 0

