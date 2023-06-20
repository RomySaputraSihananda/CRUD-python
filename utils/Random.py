import random;
import string;

def random_id(n):
    data = ''.join(random.choice(string.ascii_letters) for i in range(6));
    return data;