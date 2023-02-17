# Learning Language as AI

通过基本词汇的维基百科组成语料，供以学习语言和百科。

当前只发布英语版。

## 背景
通常说的词汇量是指词干数量。有的研究表明认识98%的文本才能基本理解句意。然而统计发现十万词（非词干）不足以覆盖英语98%。AI模型通常2^15=32768词表便已足够。所以尝试人类按照AI模型训练的办法学习。

筛选基本词汇，构建百科语料，学会语言和百科知识。

本文中的词UnicodeTokenizer分词后的词，变形基本是小写化，不包括词干化。

定义词汇等级=-lg(词频)

## 语料
    维基百科(https://en.wikipedia.org/wiki/Ai)
    BookCorpus(https://github.com/soskek/bookcorpus)
    arxiv abstract(https://www.kaggle.com/datasets/Cornell-University/arxiv) 
    词典ecdict(https://github.com/skywind3000/ECDICT)

## 依赖工具
    Wiki2txt(https://github.com/laohur/wiki2txt) :wikipedia解析器
    UnicodeTokenizer(https://github.com/laohur/UnicodeTokenizer):分词器

## 词表
等级五内,7k，覆盖87.4%; 等级六内,33k，覆盖95.2%

某些测试称需要几千词汇，是指圈定的几千词干。本项目的此表是频率筛选的绝对词表。

产出freq.txt  词频统计，至5.99级，约3.2万词

##  产出
术语筛选策略 ：标题纯英文单词、且六级词汇以内、有合适释文。

产出22章，每章一百个篇，每篇解释一个术语，词频降序。每篇包括术语标题、释文、单词释义。

正文包含五级词汇:7103、六级词汇:17540、六级之外的生僻词:15474，覆盖92%词频。正文全长63万词。

##  排版样例
只释义首句
### <a href=https://en.wikipedia.org/wiki/Cycling>Cycling</a>
<font size=3>Cycling, also, when on a two-wheeled bicycle, called bicycling or biking, is the use of cycles for transport, recreation, exercise or sport. </font>
<font size=2>
word | phonetic | definition | translation | root | lemma | degre
---- | ---- | ---- | ---- | ---- | ---- | ----
<b>cycling</b> | 'saikliŋ | n. the sport of traveling on a bicycle or motorcycle | <a href=https://en.wikipedia.org/wiki/cycling>n. 骑脚踏车兜风, 骑脚踏车消遣<br>[机] 循环操作</a> |  | cycle | 5.04
<b>wheeled</b> | hwi:ld | a. having wheels; often used in combination | <a href=https://en.wikipedia.org/wiki/wheeled>a. 有轮的；轮式的</a> |  | wheel | 5.42</font>

## 用法
翻阅各篇看术语，确定自己词汇量，从不会的开始。

每篇文章可以只看首句。

蓝字含扩展链接。