def get_hash(key):
    # This is the hash function Fh(x)
    h = 0
    for char in key:
        h += ord(char)
    return h%100
# %10 since we want the index range to be 0 to 99

if __name__ == "__main__":
    print(get_hash('march 6'))
    print(get_hash('february 29'))
    print(get_hash('august 1'))



