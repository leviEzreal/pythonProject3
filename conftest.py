# 给爷好好学，花特么5000多买的呢
# @TIME：2021/10/6
# @File:conftest.py
# _*_coding:uft-8_*-
import pytest
@pytest.fixture(scope="function",autouse=True)
def execute_sql():
    print("进入数据库")
    yield
    print("退出数据")