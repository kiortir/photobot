def long_compute():
    return 99 * 99 * 99 * 99 ** 99 ** 99 ** 99 ** 99

def main():
    lc_1 = long_compute()
    print(lc_1)
    lc_2 = long_compute()
    print(lc_2)
    
    
if __name__ == "__main__":
    main()