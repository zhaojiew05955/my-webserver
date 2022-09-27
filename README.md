# my-webserver
webserver for test

## server

使用bootle框架实现的简单测试webserver，不需要依赖

目前已经有的接口

- /log，测试日志，在当前目录创建infolog.txt日志文件
- /test/<name>，测试基本请求，返回ip等信息
- /json，测试json
- /sns，测试sns订阅
- /template，模板实现的json
- /response，测试打印响应
- /static/<filename>，测试静态文件，包括两张图片class.jpg和child.jpg，例如访问/static/class.jpg
- /，健康检查
- 404，错误跳转
- 默认监听80端口

## 镜像

Docker文件打包

```
FROM python:latest
WORKDIR /opt/web
COPY . .
EXPOSE 80
ENTRYPOINT python ./web.py
```

## efs更新

```
\#!/bin/bash
 while true; do
  python /efsweb/web.py &
  sleep 60
  kill -9 $! 
 done
```

auto-change.sh实现了60秒动态刷新

目前的用法是存储在efs中使用userdata挂载目录并运行auto-change.sh，后面只需要修改efs中的文件就能在多台实例上热更新

