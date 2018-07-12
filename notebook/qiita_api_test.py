import requests
import pprint

with open('data/temp/qiita_access_token.txt') as f:
    qiita_access_token = f.read().strip()

headers = {'Authorization': 'Bearer {}'.format(qiita_access_token)}

url_items = 'https://qiita.com/api/v2/items'

item_data = {
    'title': 'テスト記事',
    'body': 'テスト',
    'private': True,
    'tags': [{'name': 'test'}],
    'coediting': False,
    'gist': False,
    'tweet': False
}

r_post = requests.post(url_items, headers=headers, json=item_data)

print(r_post.status_code)
# 201

pprint.pprint(r_post.json())
# {'body': 'テスト\n',
#  'coediting': False,
#  'comments_count': 0,
#  'created_at': '2018-07-12T22:05:19+09:00',
#  'group': None,
#  'id': '93ead2568150009de5f1',
#  'likes_count': 0,
#  'page_views_count': None,
#  'private': True,
#  'reactions_count': 0,
#  'rendered_body': '<p>テスト</p>\n',
#  'tags': [{'name': 'test', 'versions': []}],
#  'title': 'テスト記事',
#  'updated_at': '2018-07-12T22:05:19+09:00',
#  'url': 'https://qiita.com/nkmk/private/93ead2568150009de5f1',
#  'user': {'description': '',
#           'facebook_id': '',
#           'followees_count': 0,
#           'followers_count': 0,
#           'github_login_name': None,
#           'id': 'nkmk',
#           'items_count': 0,
#           'linkedin_id': '',
#           'location': '',
#           'name': '',
#           'organization': '',
#           'permanent_id': 53096,
#           'profile_image_url': 'https://qiita-image-store.s3.amazonaws.com/0/53096/profile-images/1473692950',
#           'twitter_screen_name': None,
#           'website_url': ''}}

item_id = r_post.json()['id']
print(item_id)
# 93ead2568150009de5f1

r_get = requests.get(url_items + '/' + item_id, headers=headers)

print(r_get.status_code)
# 200

pprint.pprint(r_get.json())
# {'body': 'テスト\n',
#  'coediting': False,
#  'comments_count': 0,
#  'created_at': '2018-07-12T22:05:19+09:00',
#  'group': None,
#  'id': '93ead2568150009de5f1',
#  'likes_count': 0,
#  'page_views_count': 0,
#  'private': True,
#  'reactions_count': 0,
#  'rendered_body': '<p>テスト</p>\n',
#  'tags': [{'name': 'test', 'versions': []}],
#  'title': 'テスト記事',
#  'updated_at': '2018-07-12T22:05:19+09:00',
#  'url': 'https://qiita.com/nkmk/private/93ead2568150009de5f1',
#  'user': {'description': '',
#           'facebook_id': '',
#           'followees_count': 0,
#           'followers_count': 0,
#           'github_login_name': None,
#           'id': 'nkmk',
#           'items_count': 0,
#           'linkedin_id': '',
#           'location': '',
#           'name': '',
#           'organization': '',
#           'permanent_id': 53096,
#           'profile_image_url': 'https://qiita-image-store.s3.amazonaws.com/0/53096/profile-images/1473692950',
#           'twitter_screen_name': None,
#           'website_url': ''}}

item_data_updated = item_data.copy()
item_data_updated['title'] = 'テスト記事更新'
print(item_data_updated)
# {'title': 'テスト記事更新', 'body': 'テスト', 'private': True, 'tags': [{'name': 'test'}], 'coediting': False, 'gist': False, 'tweet': False}

r_patch = requests.patch(url_items + '/' + item_id, headers=headers, json=item_data_updated)

print(r_patch.status_code)
# 200

pprint.pprint(r_patch.json())
# {'body': 'テスト\n',
#  'coediting': False,
#  'comments_count': 0,
#  'created_at': '2018-07-12T22:05:19+09:00',
#  'group': None,
#  'id': '93ead2568150009de5f1',
#  'likes_count': 0,
#  'page_views_count': None,
#  'private': True,
#  'reactions_count': 0,
#  'rendered_body': '<p>テスト</p>\n',
#  'tags': [{'name': 'test', 'versions': []}],
#  'title': 'テスト記事更新',
#  'updated_at': '2018-07-12T22:05:19+09:00',
#  'url': 'https://qiita.com/nkmk/private/93ead2568150009de5f1',
#  'user': {'description': '',
#           'facebook_id': '',
#           'followees_count': 0,
#           'followers_count': 0,
#           'github_login_name': None,
#           'id': 'nkmk',
#           'items_count': 0,
#           'linkedin_id': '',
#           'location': '',
#           'name': '',
#           'organization': '',
#           'permanent_id': 53096,
#           'profile_image_url': 'https://qiita-image-store.s3.amazonaws.com/0/53096/profile-images/1473692950',
#           'twitter_screen_name': None,
#           'website_url': ''}}

r_delete = requests.delete(url_items + '/' + item_id, headers=headers)

print(r_delete.status_code)
# 204

url_tag = 'https://qiita.com/api/v2/tags/{}/following'

tag = 'python'

r_put = requests.put(url_tag.format(tag), headers=headers)

print(r_put.status_code)
# 204

r_delete_tag = requests.delete(url_tag.format(tag), headers=headers)

print(r_delete_tag.status_code)
# 204
