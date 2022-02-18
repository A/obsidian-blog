# from src.entities.matcher.match import EntitiesMatcher, Target


# def test_entities_matcher():
#     content = """
# ![Image Alt](https://example.com/inline_image)
# """
# 
#     """
# ![Image No Link Alt]()
# ![Image Local Alt](./local_image.png)
# ![Image Ref Alt][ref_id]
# ![Image Ref Local Alt][ref_local_id]
# 
# [ref_id]: https:example.com/ref_image
# [ref_local_id]: ./local_image_png
# 
# [[Obsidian Link]]
# [[Link with Spec Characters,._-]]
# [[Link with Title | Placeholder Title]]
# 
# ![[Obsidian Embed]]
# ![[Obsidian Embed with Spec Characters,._-]]
# ![[Obsidian Embed JPG.png]]
# ![[Obsidian Embed PNG.png]]
# ![[Obsidian Embed PDF.pdf]]
# ![[Obsidian Embed with Alt | Placeholder Title]]
# """
# 
#     res = EntitiesMatcher().get_matches(content)
# 
#     assert res == [
#         {
#             'matcher_id': 
#             'placeholder': 'Image Alt',
#             'url': 'https://example.com/inline_image',
#         },
#         # {'placeholder': 'Image No Link Alt', 'url': None},
#         # {'placeholder': 'Image Local Alt', 'url': './local_image.png'},
#         # {'placeholder': 'Image Ref Alt', 'url': 'https:example.com/ref_image'},
#         # {'placeholder': 'Image Ref Local Alt', 'url': './local_image_png'},
#         # {'placeholder': 'Obsidian Link'},
#         # {'placeholder': 'Link with Spec Characters,._-'},
#         # {
#         #     'placeholder': 'Link with Title',
#         #     'placeholder_title': 'Placeholder Title',
#         # },
#         # {'placeholder': 'Obsidian Embed'},
#         # {'placeholder': 'Obsidian Embed with Spec Characters,._-'},
#         # {'placeholder': 'Obsidian Embed JPG', 'ext': 'png'},
#         # {'placeholder': 'Obsidian Embed PNG', 'ext': 'png'},
#         # {'placeholder': 'Obsidian Embed PDF', 'ext': 'pdf'},
#         # {
#         #     'placeholder': 'Obsidian Embed with Alt',
#         #     'placeholder_title': 'Placeholder Title',
#         # },
#     ]
