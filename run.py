import unittest
from HTMLTestRunner import HTMLTestRunner
discover=unittest.defaultTestLoader.discover(
    start_dir='case',
    pattern='test_tkorder.py'
)
with open('report/report.html','wb') as file:
    runner=HTMLTestRunner(
        stream=file,
        title="易米自动化测试报告",
        description='运行环境：win10,Chrome',
        tester='pc')
    runner.run(discover)
