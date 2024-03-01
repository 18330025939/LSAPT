from ftplib import FTP


class FTPClient:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.ftp = FTP()

    def connect(self):
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.username, self.password)

    def disconnect(self):
        self.ftp.quit()

    def upload_file(self, local_file, remote_file):
        with open(local_file, 'rb') as f:
            self.ftp.storbinary('STOR ' + remote_file, f)

    def download_file(self, remote_file, local_file):
        with open(local_file, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remote_file, f.write)

    def delete_file(self, remote_file):
        self.ftp.delete(remote_file)

    def list_directory(self):
        return self.ftp.nlst()

# 示例用法
# ftp_client = FTPClient('ftp.example.com', 'username', 'password')
# ftp_client.connect()
# ftp_client.upload_file('local_file.txt', 'remote_file.txt')
# ftp_client.download_file('remote_file.txt', 'local_file.txt')
# ftp_client.delete_file('remote_file.txt')
# directory_contents = ftp_client.list_directory()
# ftp_client.disconnect()
