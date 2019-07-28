import pprint
import feedparser

url = 'http://arxiv.org/rss/cs.CV'

d = feedparser.parse(url)

pprint.pprint(d, depth=1)
# {'bozo': 0,
#  'encoding': 'us-ascii',
#  'entries': [...],
#  'etag': '"Fri, 26 Jul 2019 00:30:00 GMT", "1564101000"',
#  'feed': {...},
#  'headers': {...},
#  'href': 'http://export.arxiv.org/rss/cs.CV',
#  'namespaces': {...},
#  'status': 301,
#  'updated': 'Fri, 26 Jul 2019 00:30:00 GMT',
#  'updated_parsed': time.struct_time(tm_year=2019, tm_mon=7, tm_mday=26, tm_hour=0, tm_min=30, tm_sec=0, tm_wday=4, tm_yday=207, tm_isdst=0),
#  'version': 'rss10'}

print(type(d['entries']))
# <class 'list'>

print(len(d['entries']))
# 67

print(type(d['entries'][0]))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(d['entries'][0], width=100)
# {'author': '<a href="http://arxiv.org/find/cs/1/au:+Kurmi_V/0/1/0/all/0/1">Vinod Kumar Kurmi</a>, '
#            '<a href="http://arxiv.org/find/cs/1/au:+Bajaj_V/0/1/0/all/0/1">Vipul Bajaj</a>, <a '
#            'href="http://arxiv.org/find/cs/1/au:+Subramanian_V/0/1/0/all/0/1">Venkatesh K '
#            'Subramanian</a>, <a '
#            'href="http://arxiv.org/find/cs/1/au:+Namboodiri_V/0/1/0/all/0/1">Vinay P '
#            'Namboodiri</a>',
#  'author_detail': {'name': '<a href="http://arxiv.org/find/cs/1/au:+Kurmi_V/0/1/0/all/0/1">Vinod '
#                            'Kumar Kurmi</a>, <a '
#                            'href="http://arxiv.org/find/cs/1/au:+Bajaj_V/0/1/0/all/0/1">Vipul '
#                            'Bajaj</a>, <a '
#                            'href="http://arxiv.org/find/cs/1/au:+Subramanian_V/0/1/0/all/0/1">Venkatesh '
#                            'K Subramanian</a>, <a '
#                            'href="http://arxiv.org/find/cs/1/au:+Namboodiri_V/0/1/0/all/0/1">Vinay '
#                            'P Namboodiri</a>'},
#  'authors': [{'name': '<a href="http://arxiv.org/find/cs/1/au:+Kurmi_V/0/1/0/all/0/1">Vinod Kumar '
#                       'Kurmi</a>, <a '
#                       'href="http://arxiv.org/find/cs/1/au:+Bajaj_V/0/1/0/all/0/1">Vipul '
#                       'Bajaj</a>, <a '
#                       'href="http://arxiv.org/find/cs/1/au:+Subramanian_V/0/1/0/all/0/1">Venkatesh '
#                       'K Subramanian</a>, <a '
#                       'href="http://arxiv.org/find/cs/1/au:+Namboodiri_V/0/1/0/all/0/1">Vinay P '
#                       'Namboodiri</a>'}],
#  'id': 'http://arxiv.org/abs/1907.10628',
#  'link': 'http://arxiv.org/abs/1907.10628',
#  'links': [{'href': 'http://arxiv.org/abs/1907.10628', 'rel': 'alternate', 'type': 'text/html'}],
#  'summary': '<p>Domain adaptation is essential to enable wide usage of deep learning based\n'
#             'networks trained using large labeled datasets. Adversarial learning based\n'
#             'techniques have shown their utility towards solving this problem using a\n'
#             'discriminator that ensures source and target distributions are close. However,\n'
#             'here we suggest that rather than using a point estimate, it would be useful if\n'
#             'a distribution based discriminator could be used to bridge this gap. This could\n'
#             'be achieved using multiple classifiers or using traditional ensemble methods.\n'
#             'In contrast, we suggest that a Monte Carlo dropout based ensemble discriminator\n'
#             'could suffice to obtain the distribution based discriminator. Specifically, we\n'
#             'propose a curriculum based dropout discriminator that gradually increases the\n'
#             'variance of the sample based distribution and the corresponding reverse\n'
#             'gradients are used to align the source and target feature representations. The\n'
#             'detailed results and thorough ablation analysis show that our model outperforms\n'
#             'state-of-the-art results.\n'
#             '</p>',
#  'summary_detail': {'base': 'http://export.arxiv.org/rss/cs.CV',
#                     'language': None,
#                     'type': 'text/html',
#                     'value': '<p>Domain adaptation is essential to enable wide usage of deep '
#                              'learning based\n'
#                              'networks trained using large labeled datasets. Adversarial learning '
#                              'based\n'
#                              'techniques have shown their utility towards solving this problem '
#                              'using a\n'
#                              'discriminator that ensures source and target distributions are '
#                              'close. However,\n'
#                              'here we suggest that rather than using a point estimate, it would be '
#                              'useful if\n'
#                              'a distribution based discriminator could be used to bridge this gap. '
#                              'This could\n'
#                              'be achieved using multiple classifiers or using traditional ensemble '
#                              'methods.\n'
#                              'In contrast, we suggest that a Monte Carlo dropout based ensemble '
#                              'discriminator\n'
#                              'could suffice to obtain the distribution based discriminator. '
#                              'Specifically, we\n'
#                              'propose a curriculum based dropout discriminator that gradually '
#                              'increases the\n'
#                              'variance of the sample based distribution and the corresponding '
#                              'reverse\n'
#                              'gradients are used to align the source and target feature '
#                              'representations. The\n'
#                              'detailed results and thorough ablation analysis show that our model '
#                              'outperforms\n'
#                              'state-of-the-art results.\n'
#                              '</p>'},
#  'title': 'Curriculum based Dropout Discriminator for Domain Adaptation. (arXiv:1907.10628v1 '
#           '[cs.LG])',
#  'title_detail': {'base': 'http://export.arxiv.org/rss/cs.CV',
#                   'language': None,
#                   'type': 'text/plain',
#                   'value': 'Curriculum based Dropout Discriminator for Domain Adaptation. '
#                            '(arXiv:1907.10628v1 [cs.LG])'}}

print(d['entries'][0]['link'])
# http://arxiv.org/abs/1907.10628

print(d['entries'][0]['title'])
# Curriculum based Dropout Discriminator for Domain Adaptation. (arXiv:1907.10628v1 [cs.LG])
