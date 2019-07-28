import arxiv
import time

l = arxiv.query(query='au:"Grisha Perelman"')

arxiv.download(l[0], 'data/temp/')
# 'data/temp/0211159v1.The_entropy_formula_for_the_Ricci_flow_and_its_geometric_applications.pdf'

arxiv.download(l[0], 'data/temp/', lambda x: x.get('id').split('/')[-1])
# 'data/temp/0211159v1.pdf'

for a in l:
    arxiv.download(a, 'data/temp/')
    time.sleep(10)
