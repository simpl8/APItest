# APItest
一个不太成熟的接口测试框架记录
- baseAPI: 用于封装公共调用的模块
- report: 用于存放测试报告，这里是使用的allure插件
          生成allure测试报告方法：
          1，pytest testCase/ --alluredir ./report/allure_ori  (测试执行原始数据)
          2，allure generate ./report/allure_ori -o ./report/allure_report --clean (allure测试报告生成，index.html文件可以打开浏览器进行查看报告)
- testCase: 测试用例存放文件
- testData: 测试数据存放目录，yml格式，可以根据项目需求改成excel或其他类型文件
- testSuites: 测试套件，收集测试集（测试接口集）, 主要作用是分离测试用例使项目
  更清晰

- 使用到的包：requests，pyyaml, allure-pytest pymsssql（SqlServer）,或者
  使用MySQL数据库的就用pymsql
- 本框架还有很多可以扩展的部分，大家也可以根据自己的项目需求进行扩展改写