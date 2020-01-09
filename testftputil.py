import ftputil
import warnings
warnings.filterwarnings("ignore")

host='79.96.227.163'
username='anonymous'
password=''

# Соединяемся с FTP сервером и получаем список файлов и папок

try:
    ftp_host=ftputil.FTPHost(host, username, password)
    ftp_host.use_list_a_option = False

    with ftp_host:
            list = ftp_host.listdir(ftp_host.curdir)
            for fname in list:
                # Если нашли папку то пробуем загрузить в нее файл test.txt
                if ftp_host.path.isdir(fname):
                    print(fname+' (папка)')
                    try:
                        # Закачивание
                        ftp_host.upload('test.txt', '/'+fname+'/test.txt')
                        print("Файл загружен в папку "+fname)
                    except:
                        print("Папка недоступна для записи")
                else:
                    # Если это не папка а файл то печатаем его имя
                    # Если в имени файла есть расширение .zip скачиваем этот файл
                    print(fname+' (файл)')
                    if('.zip' in fname):
                        print('Скачиваю файл '+fname)
                        # Скачивание
                        ftp_host.download(fname, 'downloads/'+fname)
                        print('Файл '+fname+' успешно скачан')
except:
    print('Сервер не отвечает')


