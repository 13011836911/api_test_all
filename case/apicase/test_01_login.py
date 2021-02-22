"""
__time__:2021/2/20 15:48
__author__:songshijie
"""

import pytest
import allure
from case.config_test import api_data
from base.logger import logger
import requests
import json

url = "https://nx-v8-g1-trail.ntalker.com/platform/user/login"

@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():

    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{password}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, except_code, except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        data = {
            'loginId': username,
            'password': password
        }
        result = requests.post(url=url, data=json.dumps(data))
        step_1(username)
        assert result.json().get('code') == 200
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        assert except_msg in result.json().get('message')
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])
