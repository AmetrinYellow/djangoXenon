import random
from string import ascii_letters, digits
import transliterate


def create_short(title="", cnt=10):
    short = "-".join(transliterate.slugify(title, "ru")[:50].split("-")[:-1]) + "-"
    return short + "".join([random.choice(ascii_letters+digits) for _ in range(cnt)])
