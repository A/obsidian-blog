### Images

Images are processed in 2 steps:

1. **Parsing step**.
	- Parser inlines all wikilinks into the post
	- Parser collects all images used in the post
	- Parser updates image links in the post markdown according to the `ASSETS_DEST_DIR`
2. **Build step** where builder just takes `imgs` from the post and copies it to the `ASSETS_DEST_DIR`