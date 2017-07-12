
class UrlMiddleware:
    def process_view(self,request, view_func, view_args, view_kwargs):
        # print '-----------------%s'%request.path
        if request.path not in ['/usr/register/',
                                '/usr/register_handle/',
                                '/usr/uname_confm/',
                                '/usr/login/',
                                '/usr/logout/',
                                '/usr/login_handle/',
                                '/islogin/',
                                'cart_save']:

            request.session['lastpath']=request.get_full_path()