tv_file = open("tunn3l_v1s10n","r+b")
num_bytes = 30
tv_file.seek(0)
tv_bytes = tv_file.read(num_bytes)

for i in range(num_bytes):
  print(f'{i:4d}: {tv_bytes[i]:4x}')

tv_file.seek(10)
tv_file.write(b'\x36\x00\x00\x00\x28\x00\x00\x00\x6e\x04\x00\x00\x32\x03')
tv_file.seek(0)
tv_bytes = tv_file.read(num_bytes)

for i in range(num_bytes):
  print(f'{i:4d}: {tv_bytes[i]:4x}')

print(tv_bytes[:2])

tv_file.close()