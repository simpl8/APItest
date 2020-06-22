import pytest
import yaml
from testSuites import marketInfo
import allure


@allure.feature('市场信息菜单接口')  # 用于生成测试报告的模块说明
class TestMarketInfo:

    # 注意！此时yml文件中的格式必须是mapping格式，不然不能进行**解包
    with open('../testData/marketinfo.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    @allure.story('新闻资讯-获取资讯类型')  # 用于生成测试报告的功能说明
    @pytest.mark.parametrize('body', data['newsinfo_getType'])
    def test_newsinfo_getType(self, login, body):  # login参数为conftest文件的用户登录接口
        response = marketInfo.newsinfo_getType(body, login)  # login即：send函数中cookies=login，base中提到的**kwages作用显现
        pytest.assume(response.status_code == 200)  # 此处换成项目需要进行的断言语句

