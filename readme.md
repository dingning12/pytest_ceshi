# 环境
- python 3.7
- pytest 7.1.1
#依赖包
- pip 安装requirement.txt依赖包
> pip install -r requirement.txt
#安装allure，配置环境变量（xx/xx/bin）
- https://github.com/allure-framework/allure2/releases
#项目描述

#执行测试用例
- pytest -s -v
#查看测试报告
- allure测试报告
> 1.pytest --alluredir ./report/result --clean-alluredir

> 2.allure generate ./report/result -o ./report/html --clean
