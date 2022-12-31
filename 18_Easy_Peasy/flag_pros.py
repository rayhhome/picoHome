enc_flag_hex = "5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c"
enc_flag_bytes = bytes.fromhex(enc_flag_hex)
enc_flag_str = enc_flag_bytes.decode('ASCII')

print("a"*(50000-32))
print(enc_flag_str)