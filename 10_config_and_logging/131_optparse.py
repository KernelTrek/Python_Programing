# import sys
#
# print(sys.argv)

# test 는 .\131_optparse.py -- help
# test 는 .\131_optparse.py -f test.txt
from optparse import OptionParser
from optparse import OptionGroup

def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-t', '--text', action='store', type='string',
                      dest='text', help='File name')
    parser.add_option('-v', action='store_false', dest='verbose', default=True)
    parser.add_option('-q', action='store_true', dest='verbose', default=False)

    # -r 을 넣으면 user_name 이 root 가 되고 안넣으면 None 이 된다.
    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    # callback
    parser.add_option('-e', dest='env')

    def is_relase(option, opt_str, value, parser):
        # product 인경우 불가하다고 알림
        if parser.values.env == 'prd':
            raise parser.error("Can't release")
        # product 가 아닌 경우 True 값을 줌.
        setattr(parser.values, option.dest, True)

    parser.add_option('--release', action='callback', callback=is_relase, dest='release')

    # group 으로 나눠서 출력도 가능하다.
    group = OptionGroup(parser, 'Dagerous option')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    options, args = parser.parse_args()
    print(options)
    print(args)

if __name__ == '__main__':
    main()