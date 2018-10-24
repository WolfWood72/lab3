import Feistel



messege = "Всего ничего"
print(len(messege))
key = "12345678564654654546564564646464556446"
coder = Feistel.Feistel(block_size=64, type_key="scrembler", type_func="scrembler", num_rounds=16)
code = coder.encoding(messege,key)


mess = coder.decoding(code , key)

print(mess)

#a =  [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
#
#
#def __make_format( value, n_bit=15):
#    _format = '0' + str(n_bit) + 'b'
#    value.encode('utf-8')
#    return [int(j) for j in ''.join(format(ord(i), _format) for i in value)]
#
#
#a = __make_format("asdadsasdasd!! вываы ыва#")
#res = ""
#for i in range(0, len(a),15):
#    tmp = ''.join(str(j) for j in a[i: i + 15])
#    res += chr(int(tmp, 2))
#print(res)