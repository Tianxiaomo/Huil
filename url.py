import sys
import os
from six.moves import urllib

import Hutil

def download(url, path):
    filename = path.split('/')[-1]
    if not Hutil.io.exists(path):
      def _progress(count, block_size, total_size):
        sys.stdout.write('\r-----Downloading %s %.1f%%' % (filename,
            float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()
      path, _ = urllib.request.urlretrieve(url, path, _progress)
      print()
      statinfo = os.stat(path)
      print('Successfully downloaded', filename, statinfo.st_size, 'bytes.')
    
def mdownload(urls, paths, pool_size = 4):
    # assert len(urls) == len(paths)
    pool = Hutil.thread.ThreadPool(pool_size)
    for url, path in zip(urls, paths):
        pool.add(download, [url, path])
    pool.join()

if __name__ == '__main__':
    mdownload('https://dlc2.pconline.com.cn/filedown_359038_12637630/SHg7MKSI/WeChatSetup.exe',paths='data/winxin')