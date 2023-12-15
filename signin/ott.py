import random
from datetime import datetime
from django.utils.text import slugify


def ott_gen_func():
    time_seed = int(str(slugify(datetime.now())).replace("-", ""))
    rand_seed = random.seed(time_seed)
    rand_num = random.random()
    result = str(rand_num)[2:14:2]
    return result


if __name__ == "__main__":
    var = ott_gen_func()
    print(var)
