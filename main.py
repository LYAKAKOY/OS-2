import time
from hashlib import sha256
from itertools import product
from multiprocessing import Pool, cpu_count
from string import ascii_lowercase


def encode(words: list[str]) -> dict:
    hashes = {
        '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad',
        '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
        '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f',
    }

    results = {}
    for word in words:
        word_sha256 = sha256(word.encode('utf-8')).hexdigest()
        if word_sha256 in hashes:
            results[word] = word_sha256

    return results


def multy_mode(words: list[str]) -> None:
    k = len(words)//(cpu_count()*100)
    pieces = [words[i:i + k] for i in range(0, len(words), k)]
    with Pool() as p:
        result = p.map(encode, pieces)
        print(*filter(lambda d: len(d) > 0, result))


def main():
    generate_words = [''.join(word) for word in product(ascii_lowercase, repeat=5)]
    # print('Start single mode!')
    # start_time = time.time()
    # print(encode(generate_words))
    # print(f'Finished for {time.time() - start_time}s')

    print('Start multy mode!')
    start_time = time.time()
    multy_mode(generate_words)
    print(f'Finished for {time.time() - start_time}s')


if __name__ == '__main__':
    main()
