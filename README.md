# 董玉民学术网站

这是一个基于 Python Flask 框架构建的现代化学术个人网站，参考 https://sites.google.com/view/chaoh 网站设计，采用了更加精美的布局和交互效果。

## 功能特点

- 现代化响应式设计，适配各种设备
- 精美的个人资料展示，包括头像、联系信息和社交媒体链接
- 结构化的学术论文列表，按年份分类
- 详细的研究项目展示，包括时间线、合作伙伴和研究内容
- 教育背景和最新动态展示
- 丰富的交互效果，包括滚动动画、悬停效果和平滑过渡

## 视觉与交互特点

- 清晰的视觉层次结构，突出重要信息
- 平滑的滚动和淡入效果
- 悬停时的微妙动画效果
- 返回顶部按钮
- 按钮点击波纹效果
- 导航栏滚动时的样式变化
- 社交媒体图标和链接

## 技术栈

- Python 3.8+
- Flask 2.3.3
- Flask-Bootstrap 3.3.7.1
- HTML5/CSS3
- JavaScript (ES6+)
- Bootstrap 4.6
- Font Awesome 5.15.3
- Google Fonts (Roboto, Noto Sans SC)
- Waitress (生产环境 WSGI 服务器)

## 安装与运行

1. 克隆仓库
```
git clone <repository-url>
cd scholar_web
```

2. 安装依赖
```
pip install -r requirements.txt
```

3. 开发环境运行
```
python app.py
```

4. 生产环境运行 (使用 Waitress)
```
python run_server.py
```

5. 在浏览器中访问
```
开发环境: http://127.0.0.1:5000/
生产环境: http://127.0.0.1:8000/
```

## 项目结构

```
scholar_web/
├── app.py                  # Flask 应用主文件
├── run_server.py           # 生产环境启动脚本 (Waitress)
├── requirements.txt        # 项目依赖
├── README.md               # 项目说明
├── static/                 # 静态文件
│   ├── css/                # CSS 样式文件
│   │   └── style.css       # 主样式文件
│   ├── js/                 # JavaScript 文件
│   │   └── main.js         # 主脚本文件
│   └── images/             # 图片文件
│       └── profile.jpg     # 个人头像 (需要添加)
└── templates/              # HTML 模板
    ├── base.html           # 基础模板
    ├── home.html           # 首页模板
    ├── publications.html   # 发表论文页面
    └── projects.html       # 项目页面
```

## 自定义指南

1. **个人信息**: 修改 `templates/home.html` 中的个人信息、教育背景和最新动态。
2. **论文列表**: 在 `templates/publications.html` 中更新您的论文信息。
3. **研究项目**: 在 `templates/projects.html` 中编辑您的研究项目详情。
4. **样式定制**: 通过修改 `static/css/style.css` 自定义网站外观。
5. **交互效果**: 在 `static/js/main.js` 中调整或添加交互功能。
6. **头像图片**: 将您的个人头像添加到 `static/images/profile.jpg`，建议尺寸为 400x400 像素。

## 部署建议

### 使用 Waitress (Windows 兼容)

```
python run_server.py
```

### 使用 Gunicorn (Linux/Mac)

```
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### 完整生产环境部署

对于完整的生产环境部署，建议：

1. 使用 Nginx 或 Apache 作为前端代理
2. 配置 SSL/TLS 证书实现 HTTPS
3. 使用进程管理工具如 Supervisor 或 systemd
4. 设置环境变量 `FLASK_ENV=production`

## 许可证

MIT 