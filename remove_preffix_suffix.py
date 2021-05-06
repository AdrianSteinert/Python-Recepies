if __name__ == '__main__':
    # removesuffix files example
    files: list[str] = ['print.exe', 'word.exe', 'virus.exe', 'not-modified-example']
    files = [x.removesuffix('.exe') for x in files]
    print(files)