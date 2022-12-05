#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd4

    text = dir(hd4)
    for i in text:
        if i.startswith('_'):
            pass
        else:
            print(i)
