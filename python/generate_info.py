import sys
import phrase_maker.phrase_maker as phrase_maker
import git_command

phrase_maker.load_module(git_command)

def main():
    if len(sys.argv) < 2:
        print(sys.argv)
    elif len(sys.argv) < 3:
        print(phrase_maker.make(sys.argv[1], 'ERROR', capitalize=False))
    else:
        print(phrase_maker.make(sys.argv[1], sys.argv[2], capitalize=False))

if __name__ == '__main__':
    main()