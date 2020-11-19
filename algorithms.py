import random


def random_numbers(eghamat_min, eghamat_max, vorod_min, vorod_max, khoroj_min, khoroj_max, otagh_min, otagh_max):
    eghamat_random = random.randint(eghamat_min, eghamat_max)
    vorod_random = random.randint(vorod_min, vorod_max)
    khoroj_random = random.randint(khoroj_min, khoroj_max)
    otagh_random = random.randint(otagh_min, otagh_max)
    return eghamat_random, vorod_random, khoroj_random, otagh_random
