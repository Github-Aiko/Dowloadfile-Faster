import gdown

def dowloadfile(url, output):
    gdown.download(url, output, quiet=False)

def inputfile():
    url = input('Enter URL: ')
    id = url.split('/')[-2]
    outurl = 'https://drive.google.com/uc?export=download&id=' + id
    output = input('Enter output file name: ')
    dowloadfile(outurl, output)

def main():
    inputfile()

if __name__ == '__main__':
    main()