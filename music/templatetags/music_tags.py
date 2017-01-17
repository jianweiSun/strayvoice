from django import template

register = template.Library()


@register.inclusion_tag('music/manage/album_bar.html')
def show_albums_bar(all_albums, album=None):
    return {'all_albums': all_albums,
            'album': album}


@register.simple_tag
def get_genre_name(genre_code):
    if genre_code == 'all':
        return '全部類型'
    else:
        GENRE_CHOICES = [(0, '未分類曲風'),
                         (1, 'Hip hop/ Rap'),
                         (2, 'Rock'),
                         (3, 'R&B/ Soul'),
                         (4, 'Singer/ Songwriter')]
        genre_dict = dict(GENRE_CHOICES)
        return genre_dict[int(genre_code)]
