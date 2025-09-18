def split_and_join(line):
    # write your code here
    parts=line.split(" ")
    sol='-'.join(parts)
    return sol

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
