#pip install requests

import requests

baseUrl= 'https://jsonplaceholder.typicode.com'
# # get all posts
# posts_response = requests.get(f'{baseUrl}/posts')
# posts = posts_response.json()
# print(posts)

# get one post
# post_response = requests.get(f'{baseUrl}/posts/1')
# post = post_response.json()
# print("\n one post only : \n",post)

post = {"userId": 1, "id": 2, "title": "some Title", "body": "some blog post body"}
response = requests.post(f'{baseUrl}/posts', data= post)
createdPost = response.json()
print("\nCreate a new post \n", createdPost)

uPost = {"userId": 1, "title": "new Title", "body": "some blog post body"}
response = requests.put(f'{baseUrl}/posts', data= uPost)
updatedPost = response.json()
print("\Update a old post \n", updatedPost)


