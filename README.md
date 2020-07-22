# babistep_relation

数据获取阶段：
- scrapy爬取browse和special目录下的所有商品的json字符，总共19716条商品记录，json字符内共有83个关于商品feature的字段，大部分为NaN
- 网站同时提供recipe，爬取完成后收到1997条recipe信息

数据处理：
- 从Nested json的83个商品字段中提取8个features。
- 处理商品description，ingredient等描述性字段：Stopword移除，大小写还原，词性还原


特征处理：
- 对于没有description的商品，依次用ingredient，所属目录，name来填充，作为description
- EDA数据增强处理商品description字段
- 用TF-IDF提取description中5个关键词


建模：
- K-mean文本聚类：对处理完的商品的description字段，用TF-IDF算法计算description内所有单词的TF-IDF值，形成稀疏矩阵，在用K-mean对矩阵聚类
- 基于于商品的大类有13钟，中类103个，小类456个，K值选取区间设定在100-300之间，人工审核聚类效果。
- Apriori算法未能实现应用


备注：
scrapy_shop_countdown上传了整个项目的文件，只需要在IDE直接运行：
- browse_spider.py
- specials_spider.py
- recipes_spider.py
三个文件即可运行爬虫，不需要在terminal使用scrapy的命令来运行爬虫
     
     
