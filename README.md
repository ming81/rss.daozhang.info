### RSS Factory

***

Fork from: <https://github.com/zhu327/rss>

demo: <http://rss.daozhang.info>

RSS Factory 是用于生成 微博 微信公众号 知乎日报 RSS 的Web APP。  

部署在DigitalOcean的VPS上，使用Nginx作为HTTP服务器，使用supervisor管理进程。部署过程可见这篇博客：
[Deploy a tornado projects in production using github and DigitalOcean](http://daozhang.info/deploy-tornado-with-github-digitalocean/)

模版引擎为jinja2, html解析改为lxml

新增memcahed缓存，加速访问微信，知乎 rss  

（qiwihui）

2015.06.30 解决sogou请求url加密问题

（作者zhu327）

2015.02.05 搜狗微信公众号已启用反爬虫，我在代码中已添加针对反爬虫的措施，但是不保证一定有效，间歇性的500是不可避免的

2015.02.14 更新了定时任务，每6个小时更新一次cookie，获取10个有效cookie，微信公众�号api随机使用可用cookie，基本解决搜狗反爬虫问题
