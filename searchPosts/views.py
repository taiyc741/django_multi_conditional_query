from django.shortcuts import render
from .models import PostData
# Create your views here.




def index(request):
    """
    首页路由
    :param request:
    :return:
    """
    return render(request, 'searchPosts/index.html')


def search(request):
    """
    搜索路由
    :param request:
    :return:
    """
    # 判断请求是否为post请求
    if request.method == "POST":
        search_where = dict()
        # 将用户提交得数据取出
        language = request.POST["language"]
        city = request.POST["city"]
        xueli = request.POST["xueli"]
        salary_min = request.POST["salary_min"]
        exp_min = request.POST["exp_min"]
        # 判断提交信息是否为空？空不做操作
        if language:
            search_where["language"] = language.capitalize()
        if city:
            search_where["city"] = city
        if xueli:
            search_where["xueli"] = xueli
        if salary_min:
            screen = PostData.objects.filter(salary_min__gte=salary_min)
        if exp_min:
            # search_where["exp_min"] = exp_min
            if salary_min:
                screen = screen.filter(exp_min__lte=exp_min)
            else:
                screen = PostData.objects.filter(exp_min__lte=exp_min)
        if language or city or xueli or salary_min or exp_min:
            # del search_where["salary_min"]
            # del search_where["exp_min"]
            if exp_min or salary_min:
                search_info = screen.filter(**search_where)
            else:
                search_info = PostData.objects.filter(**search_where)
            # search_info = PostData.objects.filter(**search_where)
            if len(search_info):
                context = {
                    "status": 200,
                    "fieds": ["语言", "城市", "公司", "规模", "学历", "纬度", "经度", "职位", "薪资", "经验", "福利"],
                    "search_info": search_info
                }
            else:
                context = {
                    "status": 404,
                    "fieds": "未找到合适职位"
                }
        else:
            context = {
                "status": 000,
                "fieds": "请输入查询条件",
                "search_info": None
            }
            print(len(search_where))
        return render(request, 'searchPosts/result.html', context)
