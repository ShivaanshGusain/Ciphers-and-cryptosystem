from itertools import cycle

def char_to_num(c):
    return ord(c.upper()) - ord("A")

def num_to_char(n):
    return chr(n + ord("A"))

msg = "thismessagecontinsaveryimportantwordthatstartswiththeletteraandnthenendswiththeletterbobviously"
key = "thevectorequationofthewordisthat"
ciphertext = ""
for (msg_char, key_char) in zip(msg, cycle(key)):
    msg_char_num = char_to_num(msg_char)
    key_char_num = char_to_num(key_char)
    
    ciphertext_num = (msg_char_num + key_char_num) % 26 # %26 "wraps around" if the addition goes too far
    ciphertext_char = num_to_char(ciphertext_num)
    ciphertext += ciphertext_char
print(ciphertext)
