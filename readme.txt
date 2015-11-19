实验运行环境：Ubuntu 14.04 Server语言：python 2.7依赖库：numpy

代码目录
.
├── pegasos.py
└── readme.txt

执行方式(code目录下没有数据文件，执行时将数据文件置于code目录下):
$ python pegasos.py dataset1-a8a-training.txt dataset1-a8a-testing.txt 1e-4 0
$ python pegasos.py dataset1-a8a-training.txt dataset1-a8a-testing.txt 1e-4 1
$ python pegasos.py dataset1-a9a-training.txt dataset1-a9a-testing.txt 5e-5 0
$ python pegasos.py dataset1-a9a-training.txt dataset1-a9a-testing.txt 5e-5 1
