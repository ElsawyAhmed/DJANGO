from django.utils.deprecation import MiddlewareMixin

logfile = open('logfile.txt','at')


class LogsMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print(request)
        logfile.writelines(str(f'user {request.user.username}, requested the url  {request} \n'))