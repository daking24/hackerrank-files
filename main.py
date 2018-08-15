def main(n):
    new_list = []
    for i in range(n):
        t = input().strip().split()
        new_t = [int(n) if n.isdigit() else n for n in t]
        if new_t[0] == 'insert':
            new_list.insert(new_t[1], new_t[2])
        elif new_t[0] == 'print':
            neww_list = new_list
        elif new_t[0] == 'remove':
            new_list.remove(new_t[1])
        elif new_t[0] == 'append':
            new_list.append(new_t[1])
        elif new_t[0] == 'sort':
            new_list.sort()
        elif new_t[0] == 'pop':
            new_list.pop()
        elif new_t[0] == 'reverse':
            new_list.reverse()
        else:
            return 
        
        
if __name__ == '__main__':
    n = int(input())

    main(n)
