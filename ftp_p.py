import ftplib
import socket

ftp = ftplib.FTP('ftp.cse.buffalo.edu')


def ftp_upload(ftp_obj, path, ftype='TXT'):

    if ftype == 'TXT':
        with open(path) as fobj:
            ftp.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp.storbinary('STOR ' + path, fobj, 1024)


if __name__ == '__main__':
    ftp = ftplib.FTP('ftp.cse.buffalo.edu')
    ftp.login()

    path = r'C:\Users\vladyslav.hnatchenko\PycharmProjects\theory\something.txt'
    ftp_upload(ftp, path)

    pdf_path = r'C:\Users\vladyslav.hnatchenko\PycharmProjects\theory\something.pdf'
    ftp_upload(ftp, pdf_path, ftype='PDF')

    ftp.quit()

# from ftplib import FTP
#
#
# ftp = FTP('ftp.debian.org')
# ftp.login()
#
# ftp.cwd('debian')
# # out = 'C:\\Users\\vladyslav.hnatchenko\\PycharmProjects\\theory\\README.html'
# out = 'C:\\files\\README_123.html'
#
# with open(out, 'wb') as f:
#     ftp.retrbinary('RETR ' + 'README.html', f.write)


# from ftplib import FTP
#
#
# ftp = FTP('ftp.cse.buffalo.edu')
# ftp.login()
#
# ftp.cwd('mirror')
#
# data = ftp.retrlines('LIST')
#
# print(data)

# ftp = FTP()
# HOST = 'ftp.cse.buffalo.edu'
# PORT = 12345
# ftp.connect(HOST, PORT)
