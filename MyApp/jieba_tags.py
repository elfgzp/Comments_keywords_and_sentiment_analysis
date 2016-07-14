# -*- coding: utf-8 -*-
import jieba.analyse


def jieba_tags(comment):
    tags = jieba.analyse.textrank(comment, topK=20, withWeight=False,
                                  allowPOS=('n',
                                            'a', 'ad', 'ag', 'an', 'al',
                                            'vd', 'vn',
                                            'uyy',))
    return tags
