### Posts 

Posts are just about content, so they are pretty streight forward markdown-files with the frontmatter blocks.

```yaml
---
title: Hello World
published: True
date: 2021-01-09
layout: main
---

# Hello World

[[WikiLink to a note]]
![[Image.png]]
```

All wikilinks in a post are inlined and all images are copied to `ASSETS_DEST_DIR` during the build. Inlining works like in obsidian by a glob `**/{post}.md` from the root of the vault. For images it's almost same, with only the difference they're requiring extension to be in the link.