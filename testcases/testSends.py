# 给爷好好学，花特么5000多买的呢
# @TIME：2021/10/6
# @File:testSends.py
# _*_coding:uft-8_*-
import pytest


class TestSends:
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_get_token(self):
        print("获取access_token")

    @pytest.mark.run(order=4)
    def test_select_flag(self):
        print("查询接口信息")

    @pytest.mark.run(order=3)
    def test_edit_flag(self):
        print("编辑接口")

    @pytest.mark.run(order=2)
    def test_file_upload(self):
        print("文件上传")