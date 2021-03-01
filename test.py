try:
    import os
    from speedtest import Speedtest
except ImportError:
    os.system('pip install speedtest-cli')

speedTest = Speedtest()
logo="""
.'     ....      '
,.', .,.  .'' .,..'
' ,. ',    .,  ,'.'    Program Speed Test
'...  .'...'.  ..'.
 .      .,       .   Author : Tegar Sabila
        .,
        .,           Github : kelas-kode
        .'
        .,
     ........
"""
class Speedtest:
    def __init__(self, download, upload):
        self.download=download
        self.upload=upload
    def test(self):
        print('Download =',self.download)
        print('Upload =',self.upload)
if __name__=="__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    download=speedTest.download()
    upload=speedTest.upload()
    Speedtest(download, upload).test()