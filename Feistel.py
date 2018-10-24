from Scrembler import Scrembler

class Feistel:
    def __init__(self, block_size, type_key, type_func, num_rounds):
        self.__block_size = block_size
        self.__type_key = type_key
        self.__num_rounds = num_rounds
        self.__functions_dict = { "single" : self.__single,
                                  "scrembler" : self.__scrembler
        }
        self.__key_dict = { "cycle" : self.__get_key_cycle,
                                  "scrembler" : self.__get_key_scrembler
        }
        self.get_key = self.__key_dict[type_key]
        self.F = self.__functions_dict.get(type_func, self.__scrembler)


    def __scrembler(self, V, X):
        seq = Scrembler(init_value=[1,1,1,0,1,0,1], polynom=[0,1,14]).GetSequence(len(X))
        S = [i^j for i,j in  zip(seq,X)]
        return [i^j for i,j in  zip(S,V)]

    def __single(self, V, X):
        return V

    def __get_key_cycle(self,key, i  ):
        if (i + self.__block_size // 2) < len(key):
            return key[i:i + self.__block_size // 2]
        else:
            return key[i:] + key[:i + self.__block_size // 2 - len(key)]

    def __get_key_scrembler(self, key, i):
        if (i + 8) < len(key):
            tmp = key[i:i + 8]
        else:
            tmp = key[i:] + key[:i + 8 - len(key)]
        return Scrembler(init_value=tmp, polynom=[0,1]).GetSequence(self.__block_size)
    def __make_format(self, value, n_bit=15):
        _format = '0' + str(n_bit) + 'b'
        value.encode('utf-8')
        return [int(j) for j in ''.join(format(ord(i), _format) for i in value)]


    def make_round(self, left, right,  key):
        N= max(len(right), len(left))
        s = self.F(key, left)
        print(s)
        temp = [right[k]^s[k] for k in range(N)]
        right = left.copy()
        left = temp.copy()
        return left, right


    def encoding(self, message, key):
        key = self.__make_format(key)
        bit_message = self.__make_format(message)
        length_mess = len(bit_message)
        code = []
        print(len(bit_message))
        print(bit_message)
        NN = 0
        while len(bit_message)% self.__block_size != 0:
            bit_message.append(1)
            NN += 1
        for n in range(0,length_mess, self.__block_size):
            block = bit_message[n: n + self.__block_size]
            N = len(block)//2
            Right = block[N:]
            Left = block[:N]
            print(n)
            for i in range(self.__num_rounds):
                Right, Left = self.make_round(Left, Right, self.get_key(key,i))
            code += Left + Right
        code = code[:-NN]
        print(code)
        res = ""
        for i in range(0, len(code), 15):
            tmp = ''.join(str(j) for j in code[i: i + 15])
            res += chr(int(tmp, 2))
        print(len(res))
        print(res)
        return res






    def decoding(self, code, key):
        key = self.__make_format(key)
        bit_code = self.__make_format(code)
        length_code = len(bit_code)
        mess = []
        print(len(bit_code))
        print(bit_code)
        NN = 0
        while len(bit_code) % self.__block_size != 0:
            bit_code.append(0)
            NN += 1
        for n in range(0,length_code, self.__block_size):
            block = bit_code[n: n + self.__block_size]
            N = len(block)//2
            Right = block[N:]
            Left = block[:N]

            for i in range(self.__num_rounds-1,-1,-1):
                Right, Left = self.make_round(Left, Right, self.get_key(key,i))
            mess += Left + Right
        print(len(mess))
        print(mess)
        mess = mess[:-NN]
        res = ""
        for i in range(0, len(mess), 15):
            tmp = ''.join(str(j) for j in mess[i: i + 15])
            res += chr(int(tmp, 2))

        print(res)
            #code.append(Right)
        return res