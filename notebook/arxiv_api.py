import pprint

import arxiv
import pandas as pd

l = arxiv.query(query='au:"Grisha Perelman"')

print(type(l))
# <class 'list'>

print(len(l))
# 3

print(type(l[0]))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(l[0], width=200)
# {'affiliation': 'None',
#  'arxiv_comment': '39 pages',
#  'arxiv_primary_category': {'scheme': 'http://arxiv.org/schemas/atom', 'term': 'math.DG'},
#  'arxiv_url': 'http://arxiv.org/abs/math/0211159v1',
#  'author': 'Grisha Perelman',
#  'author_detail': {'name': 'Grisha Perelman'},
#  'authors': ['Grisha Perelman'],
#  'doi': None,
#  'guidislink': True,
#  'id': 'http://arxiv.org/abs/math/0211159v1',
#  'journal_reference': None,
#  'links': [{'href': 'http://arxiv.org/abs/math/0211159v1', 'rel': 'alternate', 'type': 'text/html'},
#            {'href': 'http://arxiv.org/pdf/math/0211159v1', 'rel': 'related', 'title': 'pdf', 'type': 'application/pdf'}],
#  'pdf_url': 'http://arxiv.org/pdf/math/0211159v1',
#  'published': '2002-11-11T16:11:49Z',
#  'published_parsed': time.struct_time(tm_year=2002, tm_mon=11, tm_mday=11, tm_hour=16, tm_min=11, tm_sec=49, tm_wday=0, tm_yday=315, tm_isdst=0),
#  'summary': 'We present a monotonic expression for the Ricci flow, valid in all dimensions\n'
#             'and without curvature assumptions. It is interpreted as an entropy for a\n'
#             'certain canonical ensemble. Several geometric applications are given. In\n'
#             'particular, (1) Ricci flow, considered on the space of riemannian metrics\n'
#             'modulo diffeomorphism and scaling, has no nontrivial periodic orbits (that is,\n'
#             'other than fixed points); (2) In a region, where singularity is forming in\n'
#             'finite time, the injectivity radius is controlled by the curvature; (3) Ricci\n'
#             'flow can not quickly turn an almost euclidean region into a very curved one, no\n'
#             'matter what happens far away. We also verify several assertions related to\n'
#             "Richard Hamilton's program for the proof of Thurston geometrization conjecture\n"
#             'for closed three-manifolds, and give a sketch of an eclectic proof of this\n'
#             'conjecture, making use of earlier results on collapsing with local lower\n'
#             'curvature bound.',
#  'summary_detail': {'base': 'http://export.arxiv.org/api/query?search_query=au%3A%22Grisha+Perelman%22&id_list=&start=0&max_results=1000&sortBy=relevance&sortOrder=descending',
#                     'language': None,
#                     'type': 'text/plain',
#                     'value': 'We present a monotonic expression for the Ricci flow, valid in all dimensions\n'
#                              'and without curvature assumptions. It is interpreted as an entropy for a\n'
#                              'certain canonical ensemble. Several geometric applications are given. In\n'
#                              'particular, (1) Ricci flow, considered on the space of riemannian metrics\n'
#                              'modulo diffeomorphism and scaling, has no nontrivial periodic orbits (that is,\n'
#                              'other than fixed points); (2) In a region, where singularity is forming in\n'
#                              'finite time, the injectivity radius is controlled by the curvature; (3) Ricci\n'
#                              'flow can not quickly turn an almost euclidean region into a very curved one, no\n'
#                              'matter what happens far away. We also verify several assertions related to\n'
#                              "Richard Hamilton's program for the proof of Thurston geometrization conjecture\n"
#                              'for closed three-manifolds, and give a sketch of an eclectic proof of this\n'
#                              'conjecture, making use of earlier results on collapsing with local lower\n'
#                              'curvature bound.'},
#  'tags': [{'label': None, 'scheme': 'http://arxiv.org/schemas/atom', 'term': 'math.DG'}, {'label': None, 'scheme': 'http://arxiv.org/schemas/atom', 'term': '53C'}],
#  'title': 'The entropy formula for the Ricci flow and its geometric applications',
#  'title_detail': {'base': 'http://export.arxiv.org/api/query?search_query=au%3A%22Grisha+Perelman%22&id_list=&start=0&max_results=1000&sortBy=relevance&sortOrder=descending',
#                   'language': None,
#                   'type': 'text/plain',
#                   'value': 'The entropy formula for the Ricci flow and its geometric applications'},
#  'updated': '2002-11-11T16:11:49Z',
#  'updated_parsed': time.struct_time(tm_year=2002, tm_mon=11, tm_mday=11, tm_hour=16, tm_min=11, tm_sec=49, tm_wday=0, tm_yday=315, tm_isdst=0)}

print(l[0]['author'])
# Grisha Perelman

print(l[0]['title'])
# The entropy formula for the Ricci flow and its geometric applications

print(l[0]['arxiv_url'])
# http://arxiv.org/abs/math/0211159v1

print(l[0]['pdf_url'])
# http://arxiv.org/pdf/math/0211159v1

print(l[0]['summary'])
# We present a monotonic expression for the Ricci flow, valid in all dimensions
# and without curvature assumptions. It is interpreted as an entropy for a
# certain canonical ensemble. Several geometric applications are given. In
# particular, (1) Ricci flow, considered on the space of riemannian metrics
# modulo diffeomorphism and scaling, has no nontrivial periodic orbits (that is,
# other than fixed points); (2) In a region, where singularity is forming in
# finite time, the injectivity radius is controlled by the curvature; (3) Ricci
# flow can not quickly turn an almost euclidean region into a very curved one, no
# matter what happens far away. We also verify several assertions related to
# Richard Hamilton's program for the proof of Thurston geometrization conjecture
# for closed three-manifolds, and give a sketch of an eclectic proof of this
# conjecture, making use of earlier results on collapsing with local lower
# curvature bound.

pprint.pprint([a['id'] for a in l])
# ['http://arxiv.org/abs/math/0211159v1',
#  'http://arxiv.org/abs/math/0303109v1',
#  'http://arxiv.org/abs/math/0307245v1']

pprint.pprint([[a['id'], a['published']] for a in l])
# [['http://arxiv.org/abs/math/0211159v1', '2002-11-11T16:11:49Z'],
#  ['http://arxiv.org/abs/math/0303109v1', '2003-03-10T16:44:35Z'],
#  ['http://arxiv.org/abs/math/0307245v1', '2003-07-17T15:26:38Z']]

df = pd.io.json.json_normalize(l)
print(df.shape)
# (3, 29)

print(df[['title', 'published']])
#                                                title             published
# 0  The entropy formula for the Ricci flow and its...  2002-11-11T16:11:49Z
# 1         Ricci flow with surgery on three-manifolds  2003-03-10T16:44:35Z
# 2  Finite extinction time for the solutions to th...  2003-07-17T15:26:38Z

l = arxiv.query(query='cat:cs.AI', max_results=10, sort_by='submittedDate')

pprint.pprint([[a['id'], a['published']] for a in l])
# [['http://arxiv.org/abs/1907.11184v1', '2019-07-25T16:45:06Z'],
#  ['http://arxiv.org/abs/1907.11112v1', '2019-07-25T14:45:04Z'],
#  ['http://arxiv.org/abs/1907.11021v1', '2019-07-25T13:15:12Z'],
#  ['http://arxiv.org/abs/1907.11007v1', '2019-07-25T12:30:08Z'],
#  ['http://arxiv.org/abs/1907.10953v1', '2019-07-25T10:36:01Z'],
#  ['http://arxiv.org/abs/1907.10952v1', '2019-07-25T10:31:34Z'],
#  ['http://arxiv.org/abs/1907.10925v1', '2019-07-25T09:34:13Z'],
#  ['http://arxiv.org/abs/1907.10914v1', '2019-07-25T09:19:30Z'],
#  ['http://arxiv.org/abs/1907.10772v1', '2019-07-24T23:28:37Z'],
#  ['http://arxiv.org/abs/1907.10761v1', '2019-07-24T22:30:04Z']]

l = arxiv.query(query='cat:cs.AI', max_results=10,
                sort_by='submittedDate', sort_order='ascending')

pprint.pprint([[a['id'], a['published']] for a in l])
# [['http://arxiv.org/abs/cs/9308101v1', '1993-08-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9308102v1', '1993-08-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9309101v1', '1993-09-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9311101v1', '1993-11-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9311102v1', '1993-11-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9312101v1', '1993-12-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9401101v1', '1994-01-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9402101v1', '1994-02-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9402102v1', '1994-02-01T00:00:00Z'],
#  ['http://arxiv.org/abs/cs/9402103v1', '1994-02-01T00:00:00Z']]

l = arxiv.query(query='cat:cs.AI AND submittedDate:[20190101 TO 20190131235959]',
                sort_by='submittedDate', sort_order='ascending')

df = pd.io.json.json_normalize(l)
print(df.shape)
# (298, 29)

print(df.head()[['id', 'published']])
#                                   id             published
# 0  http://arxiv.org/abs/1901.00073v1  2019-01-01T01:22:19Z
# 1  http://arxiv.org/abs/1901.00117v1  2019-01-01T08:50:47Z
# 2  http://arxiv.org/abs/1901.00158v2  2019-01-01T14:41:17Z
# 3  http://arxiv.org/abs/1901.01851v1  2019-01-01T18:05:43Z
# 4  http://arxiv.org/abs/1901.00204v1  2019-01-01T20:02:38Z

print(df.tail()[['id', 'published']])
#                                     id             published
# 293  http://arxiv.org/abs/1902.00045v1  2019-01-31T19:33:13Z
# 294  http://arxiv.org/abs/1902.00098v1  2019-01-31T22:14:34Z
# 295  http://arxiv.org/abs/1902.03092v1  2019-01-31T22:26:56Z
# 296  http://arxiv.org/abs/1902.00120v1  2019-01-31T23:10:31Z
# 297  http://arxiv.org/abs/1902.00137v2  2019-01-31T23:59:34Z

l = arxiv.query(query='cat:cs.AI AND ti:"deep learning" AND submittedDate:[20190101 TO 20190131235959]',
                sort_by='submittedDate', sort_order='ascending')

df = pd.io.json.json_normalize(l)
print(df[['title', 'published']])
#                                                title             published
# 0  Augmentation Scheme for Dealing with Imbalance...  2019-01-01T20:02:38Z
# 1  Geometrization of deep networks for the interp...  2019-01-06T14:32:45Z
# 2  Deep Learning for Human Affect Recognition: In...  2019-01-09T23:33:47Z
# 3  Automatic Surface Area and Volume Prediction o...  2019-01-15T17:26:43Z
# 4  Fast Deep Learning for Automatic Modulation Cl...  2019-01-16T01:15:50Z
# 5  DLocRL: A Deep Learning Pipeline for Fine-Grai...  2019-01-21T17:36:19Z
# 6  DF-SLAM: A Deep-Learning Enhanced Visual SLAM ...  2019-01-22T09:25:08Z
# 7            Deep learning Inversion of Seismic Data  2019-01-23T05:51:05Z
# 8  Proceedings of AAAI 2019 Workshop on Network I...  2019-01-25T10:12:23Z

l = arxiv.query(id_list=['1902.00358v2', '1902.00358', 'math/0211159v1'])

for a in l:
    print(a['arxiv_url'])
# http://arxiv.org/abs/1902.00358v2
# http://arxiv.org/abs/1902.00358v2
# http://arxiv.org/abs/math/0211159v1
