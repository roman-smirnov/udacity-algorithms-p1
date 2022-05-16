""" Huffman Encoding and Decoding"""
import sys
import queue
from itertools import count

tiebreaker = count()


class Node:
    def __init__(self, freq) -> None:
        super().__init__()
        self.left = None
        self.right = None
        self.symbol = None
        self.freq = freq
        self.code = ''


def build_freq_table(data):
    freq_table = dict()
    for symbol in data:
        freq = freq_table.get(symbol, 0)
        freq_table[symbol] = freq + 1
    return freq_table


def build_freq_queue(freq_table):
    min_heap = queue.PriorityQueue()
    for symbol, freq in freq_table.items():
        node = Node(freq)
        node.symbol = symbol
        min_heap.put((freq, next(tiebreaker), node))
    return min_heap


def build_huffman_tree(min_heap: queue.PriorityQueue):
    while min_heap.not_empty:
        freq1, tb1, node1 = min_heap.get()
        if min_heap.empty():
            return node1
        freq2, tb2, node2 = min_heap.get()
        node = Node(node1.freq + node2.freq)
        node.left = node1
        node.right = node2
        min_heap.put((node.freq, next(tiebreaker), node))
    return None


def build_huffman_dict_helper(huffman_node, huffman_dict):
    if huffman_node.left is None and huffman_node.right is None:
        huffman_dict[huffman_node.symbol] = huffman_node.code
        return
    huffman_node.left.code = huffman_node.code + '0'
    huffman_node.right.code = huffman_node.code + '1'
    build_huffman_dict_helper(huffman_node.left, huffman_dict)
    build_huffman_dict_helper(huffman_node.right, huffman_dict)


def build_huffman_dict(huffman_tree_root):
    huffman_dict = dict()
    build_huffman_dict_helper(huffman_tree_root, huffman_dict)
    return huffman_dict


def encode_message(message, dictionary):
    huffman_code = ''
    for symbol in message:
        huffman_code = huffman_code + dictionary[symbol]
    return huffman_code


def huffman_encoding(data):
    if data is None or data == '':
        raise ValueError('data is None or empty')
    if len(data) < 2:
        raise ValueError('data must have at least 2 symbols')
    freq_table = build_freq_table(data)

    if len(freq_table.keys()) < 2:
        raise ValueError('data must have at least different 2 symbols')
    min_heap = build_freq_queue(freq_table)
    huffman_tree = build_huffman_tree(min_heap)
    huffman_dict = build_huffman_dict(huffman_tree)
    huffman_code = encode_message(data, huffman_dict)
    return huffman_code, huffman_tree


def huffman_decoding(data, huffman_tree_root):
    msg = ''
    # you can do this in a foor loop. travel down thre tree until reaching a terminal node, then reset to root
    cur_node = huffman_tree_root
    for symbol in data:

        if symbol == '0':
            cur_node = cur_node.left
        elif symbol == '1':
            cur_node = cur_node.right
        else:
            raise ValueError('Huffman code contains non-binary characters')

        if cur_node.left is None and cur_node.right is None:
            msg = msg + cur_node.symbol
            cur_node = huffman_tree_root

    return msg


def provided_test():
    codes = {}
    print('\n================ Test Provided by Udacity ================')
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


def my_test():
    print('\n================ My Test ================')
    a_great_sentence = 'the quick brown fox jumped over the lazy dog'
    symbol_frequency_dict = build_freq_table(a_great_sentence)
    print('symbol freq: ', [(s, f) for s, f in symbol_frequency_dict.items()])

    frequency_min_heap = build_freq_queue(symbol_frequency_dict)
    nodes = [frequency_min_heap.get()[2] for _ in range(frequency_min_heap.qsize())]
    print('freq min heap: ', [(n.freq, n.symbol) for n in nodes])

    frequency_min_heap = build_freq_queue(symbol_frequency_dict)
    root = build_huffman_tree(frequency_min_heap)
    print('root freq: ', root.freq)
    print('root left freq: ', root.left.freq)
    print('root right freq: ', root.right.freq)

    code_dictionary = build_huffman_dict(root)
    print('symbol codes: ', [(s, c) for s, c in code_dictionary.items()])

    code = encode_message(a_great_sentence, code_dictionary)
    print('encoded message: ', code)

    message = huffman_decoding(code, root)
    print('decoded message: ', message)


def test1():
    try:
        _ = huffman_encoding('')
    except ValueError as e:
        print(str(e))


def test2():
    try:
        code, tree = huffman_encoding('A')
        msg = huffman_decoding(code, tree)
        print(msg)
    except ValueError as e:
        print(str(e))


def test3():
    try:
        code, tree = huffman_encoding('AAAAAAAAAAAA')
        msg = huffman_decoding(code, tree)
        print(msg)
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    provided_test()
    my_test()
    test1()
    test2()
    test3()

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or§ very large values

# Test Case 1

# Test Case 2

# Test Case 3
