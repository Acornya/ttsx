# class UrlMiddleware:
#     def process_request(self,request):
#         if request.path not in ['/register/','/register_handle/','/uname_confm/','/login/','/logout/','/login_handle/'
#         ,'/close/']:
#
#             request.session['lastpath'] = request.get_full_path()
class UrlMiddleware:
    def process_request(self,request):
        # print '-----------------%s'%request.path
        if request.path not in ['/user/register/',
                                '/user/register_handle/',
                                '/user/uname_confm/',
                                '/user/login/',
                                '/user/logout/',
                                '/user/login_handle/',]:
            request.session['lastpath']=request.get_full_path()