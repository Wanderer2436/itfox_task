import core.models


def add_or_remove_like(news: core.models.News, user: core.models.Users):
    if not news.likes.contains(user):
        news.likes.add(user)
    else:
        news.likes.remove(user)