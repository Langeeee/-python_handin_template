import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


class TextComparer:
    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url):
        try:
            download = requests.get(url)
            url_content = download.content
            csv = open(url[-10:-6].replace('/', '') +'.txt', 'wb')
            csv.write(url_content)
            csv.close()
            return url[-10:-6].replace('/', '') +'.txt'
        except Exception as e:
            print(e)

    def multi_download(self, download, listOfUrls, workers):
        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(download, listOfUrls)
        return list(res)

    def url_list_generator(self, url_list):
        num = 0
        while num < len(url_list):
            yield url_list[num]
            num +=1
        return self
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.url_list is None:
            raise StopIteration
        returnval = self.url_list.item
        self.url_list = self.url_list.next
        return returnval
    
    def avg_vowels(self, book):
        count = 0
        vowels = ['a', 'e', 'i','o','u','A','E','I','O','U']
        in_file = open(book, 'r')
        txt = in_file.read()
        total_words = txt.split()
        for char in txt:
            if char in vowels:
                count = count+1
        avg_vow = count/len(total_words)
        return [book, avg_vow]
    
    def hardest_read(self, func, args, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(func, args)
        #return next(res)
        return max(list(res),key=lambda item:item[1])[0]