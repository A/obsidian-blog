### Image Context

Images are part of a `post_context` and may be accessible in templates from `post.imgs` list.

```
{
  "file": str,
  "slug": str, # generated from the sluggified filename
  "name": str, # generated from the filename
  "placeholder": str, # mediawiki image placeholder like ![[Image.png]]
}
```
