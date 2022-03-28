
def main():
    number = 16               # number main = 16
    number = do_thing(number) # number main = 11
    print(number)             # print 11

def do_thing(other):      # other = 16
    number = 5            # number do_thing = 5
    return other - number # 16 - 5 = 11 returned

main()
