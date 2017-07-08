
class UrlMiddleware:
    def process_request(self,request):
        # print '-----------------%s'%request.path
        if request.path not in ['/usr/register/',
                                '/usr/register_handle/',
                                '/usr/uname_confm/',
                                '/usr/login/',
                                '/usr/logout/',
                                '/usr/login_handle/',]:

            request.session['lastpath']=request.get_full_path()