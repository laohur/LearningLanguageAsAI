# Learning Language as AI

通过基本词汇的维基百科组成语料，供以学习语言和百科。

## 背景
通常说的词汇量是指词干数量。有的研究表明认识98%的文本才能基本理解句意。然而统计发现十万词（非词干）不足以覆盖英语98%。AI模型通常2^15=32768词表便已足够。所以尝试人类按照AI模型训练的办法学习。

筛选基本词汇，构建百科语料，学会语言和百科知识。

本文中的词UnicodeTokenizer分词后的词，变形基本是小写化，不包括词干化。

定义词汇等级=-lg(词频)

## 依赖工具
* Wiki2txt(https://github.com/laohur/wiki2txt) :wikipedia解析器
* UnicodeTokenizer(https://github.com/laohur/UnicodeTokenizer):分词器

## 语料
维基百科
Wiki2text解析wikipedia

## 词表
维基百科+维基古书
统计词频 
等级五内,7k，覆盖87.4%; 等级六内,33k，覆盖95.2%
某些测试称需要几千词汇，是指圈定的几千词干。本项目的此表是频率筛选的绝对词表。
* 产出freq.tsv  词频统计，至5.99级，约3.2万词

