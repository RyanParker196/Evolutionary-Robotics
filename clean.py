import os

# Clear files
def clean():
    if os.path.exists('brain*.nndf'):
        print(1)
        os.remove('brain*.nndf')
    if os.path.exists('fitness*.txt'):
        print(1)
        os.remove('fitness*.txt')
    if os.path.exists('tmp*.txt'):
        print(1)
        os.remove('tmp*.txt')

if __name__ == '__main__':
    clean()