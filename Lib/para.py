import inspect


class FtpServer:
    def __init__(self):
        self.object = {'ftpServer': None}
        self.parameter = {'ip': None,
                          'port': None,
                          'login': None,
                          'password': None,
                          'path': None}

    def handle_ip(self, arg):
        pass
    def get_port(self, arg):
        pass

    def get_login(self, arg):
        pass

    def get_password(self, arg):
        pass

    def get_path(self, ):
        pass

    def switch_parameter_handle(self, para, arg):
        cases = {
                "ip": self.get_ip(arg),
                "port": self.get_port(),
                "login": self.get_login(),
                "password": self.get_password(),
                "path": self.get_path()
            }
        cases.get(para, self.get_ip)()

# class Config

# data = {
#     "system": {
#         "startTime": time,
#         "avoidLogin": avoid,
#         "login": login,
#         "password": password,
#         "version": ver,
#     }
# }
#
# data = {
#     "model": model,
#     "version": ver,
#     "mode": mode,
# }
#
#
#
# def get_variable_name(variable):
#     frame = inspect.currentframe()
#     frame_info = inspect.getframeinfo(frame.f_back)
#     return frame_info.code_context[0].strip().split()[1]
#
# if __name__ == '__main__':
#     ftp = FtpServer()
#     # 测试代码
#     # x = 42
#     variable_name = get_variable_name(ftp.object_name)
#     print(getattr(ftp, ftp.object_name.__str__()))
#     print(variable_name)  # 输出: x
