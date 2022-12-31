dec_flag_hex = "3766396461323966343034393961393864623232303338306135373734366134"
dec_flag_bytes = bytes.fromhex(dec_flag_hex)
dec_flag_str = dec_flag_bytes.decode('ASCII')

print(dec_flag_bytes)
print(dec_flag_str)