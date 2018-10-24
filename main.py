import Feistel
import argparse
import sys

type_key_list = ["cycle", "scrembler"]
type_func_list = ["single", "scrembler"]
change_bit_mode = ["messege", "key"]

parser = argparse.ArgumentParser()
parser.add_argument("-encode", "-encode", action='store_true',
                    help="input file", required=False)
parser.add_argument("-decode","-decode",  action='store_true',
                    help="input file", required=False)
parser.add_argument("-input_file", type=str,
                    help="file with input message")
parser.add_argument("-output_file", type=str,
                    help="file with output message")
parser.add_argument("-key_file", type=str,
                    help="file with key for Feistel net")

parser.add_argument("-block_size", type=int,
                    help="block_size",default=64)
parser.add_argument("-num_rounds", type=int,
                    help="num_rounds",default=10)
parser.add_argument("-type_key", type=str,
                    help="type_key  default cycle", choices=type_key_list,default="cycle")
parser.add_argument("-type_func", type=str,
                    help="type_func  default single",choices=type_func_list,default="single")
parser.add_argument("-change_bit_mode", type=str,
                    help="change_bit_mode",choices=change_bit_mode,default="key")
parser.add_argument("-bit_index", type=int,
                    help="bit_index default 5", default=5)



namespace = parser.parse_args(sys.argv[1:])


try:
    if not namespace.decode and not namespace.encode:
        raise ValueError("must have decode or encode param")
    if namespace.decode and namespace.encode:
        raise ValueError("must have only one of encode and deocde param")

    with open(namespace.input_file, "r", encoding="utf-8") as f:
        messege = f.read()

    with open(namespace.key_file, "r", encoding="utf-8") as f:
        key = f.read()

    block_size = namespace.block_size
    type_key = namespace.type_key
    type_func = namespace.type_func
    num_rounds = namespace.num_rounds
    change_bit_mode = namespace.change_bit_mode
    change_bit_index = namespace.bit_index

    coder = Feistel.Feistel(block_size=block_size, type_key=type_key, type_func=type_func, num_rounds=num_rounds,change_bit_mode=change_bit_mode, change_bit_index=change_bit_index)

    if namespace.encode:
        encoded_mes = coder.encoding(messege,key)
        print("Закодированное сообщение: '{}'".format(encoded_mes))
       # decoded_mes = coder.decoding(encoded_mes,key)
      #  print(decoded_mes)
        with open(namespace.output_file, "w", encoding="utf-8") as f:
            f.write(encoded_mes)
        coder.make_plot(list(range(len(coder.graph_info))), coder.graph_info)
    elif namespace.decode:
        decoded_mes = coder.decoding(messege,key)
        print("Расшифрованное сообщение: '{}'".format(decoded_mes))


        with open(namespace.output_file, "w", encoding="utf-8") as f:
            f.write(decoded_mes)


except Exception as e:
    print(str(e))
    exit("err")





























