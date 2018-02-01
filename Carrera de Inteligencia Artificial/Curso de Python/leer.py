

def run():
    counter = 0
    with open('/Users/lucasdaje/Library/Mobile Documents/com~apple~CloudDocs/Machine Learning/Python/aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')

    print('Breatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()
