
import binascii

def hexStr_to_str(hex_str):
    hex = hex_str.encode('utf-8')
    str_bin = binascii.unhexlify(hex)
    return str_bin.decode('utf-8')
def hesStr_to_asi(str):
    return chr(int(str))

#16进制转字符串
if __name__ == "__main__":

	hex_str = '65626d61726168'
	print(hexStr_to_str(hex_str))
