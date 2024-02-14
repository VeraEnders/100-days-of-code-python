# # We've got some buggy code, try running the code.

# facebook_posts = [
#   {"Likes": 21, "Comments": 2},
#   {"Likes": 13, "Comments": 2, "Shares": 1},
#   {"Likes": 33, "Comments": 8, "Shares": 3},
#   {"Comments": 4, "Shares": 2},
#   {"Comments": 1, "Shares": 1},
#   {"Likes": 19, "Comments": 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#   total_likes = total_likes + post["Likes"]

# # The code will crash and give you an KeyError.
# # Prevent the program from crashing: catch the KeyError exception. 
# # Posts without any likes can be counted as 0 likes.

facebook_posts = [
  {"Likes": 21, "Comments": 2},
  {"Likes": 13, "Comments": 2, "Shares": 1},
  {"Likes": 33, "Comments": 8, "Shares": 3},
  {"Comments": 4, "Shares": 2},
  {"Comments": 1, "Shares": 1},
  {"Likes": 19, "Comments": 3}
]
total_likes = 0

for post in facebook_posts:
  try:
    likes = post["Likes"]
  except KeyError:
    likes = 0
  finally:
    total_likes += likes
print(total_likes)

# for post in facebook_posts:
#   try:
#     total_likes = total_likes + post["Likes"]
#   except KeyError:
#     pass
# print(total_likes)