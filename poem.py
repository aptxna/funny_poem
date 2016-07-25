# -*- coding: utf-8 -*-

import random
from random import randint
import time
import re
import json

twochar_words = ['朱砂', '天下', '杀伐', '人家', '韶华', '风华', '繁华', '血染', '墨染', '白衣', '素衣', '嫁衣', 
'倾城', '孤城', '空城', '旧城', '旧人', '伊人', '心疼', '春风', '古琴', '无情', '迷离', '奈何', '断弦', '焚尽', 
'散乱', '陌路', '乱世', '笑靥', '浅笑', '明眸', '轻叹', '烟火', '一生', '三生', '浮生', '桃花', '梨花', '落花', 
'烟花', '离殇', '情殇', '爱殇', '剑殇', '灼伤', '仓皇', '匆忙', '陌上', '清商', '焚香', '墨香', '微凉', '断肠', 
'痴狂', '凄凉', '黄梁', '未央', '成双', '无恙', '虚妄', '凝霜', '洛阳', '长安', '江南', '忘川', '千年', '纸伞', 
'烟雨', '回眸', '公子', '红尘', '红颜', '红衣', '红豆', '红线', '青丝', '青史', '青冢', '白发', '白首', '白骨', 
'黄土', '黄泉', '碧落', '紫陌']

fourchar_words = ['情深缘浅', '情深不寿', '莫失莫忘', '阴阳相隔', '如花美眷', '似水流年', 
'眉目如画', '曲终人散', '繁华落尽', '不诉离殇', '一世长安']

sentence_model = ['xx，xx，xx了xx。', 'xxxx，xxxx，不过是一场xxxx。', '你说xxxx，我说xxxx，最后不过xxxx。', 
'xx，xx，许我一场xxxx。', '一x一x一xx，半x半x半xx。', '你说xxxxxxxx，后来xxxxxxxx。', 'xxxx，xxxx，终不敌xxxx。']

def get_sentence():
	model = sentence_model[randint(0, len(sentence_model)-1)]

	while 'xxxx' in model:
		temp = model
		substring = re.compile('xxxx')
		model = substring.sub(fourchar_words[randint(0, len(fourchar_words)-1)], temp, 1)

	while 'xx' in model:
		temp = model
		substring = re.compile('xx')
		model = substring.sub(twochar_words[randint(0, len(twochar_words)-1)], temp, 1)

	while 'x' in model:
		temp = model
		substring = re.compile('x')
		subword = random.choice(twochar_words)
		model = substring.sub(subword[randint(0,1)], temp, 1)

	print json.dumps(model, encoding="utf-8", ensure_ascii=False)

while (1):
	get_sentence()
	time.sleep(1)