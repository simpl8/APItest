from baseAPI.base import send


# 获取资讯类型信息
def newsinfo_getType(request_body, cookie):
    response = send(request_body, cookies=cookie)
    return response

