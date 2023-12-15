from django.utils.text import slugify
# from wite.posts.per2eng import per_2_eng
from .per2eng import per_2_eng


def custagslug(tag_name):
    slug_tag = slugify(per_2_eng(tag_name))
    return slug_tag
