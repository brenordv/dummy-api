# -*- coding: utf-8 -*-

from random import getrandbits
import hashlib


def get_sha256(seed=None):
    """
    Generates a sha256 string based on a provided seed.
    :param seed: seed used to generate the hash
    :return: string with the hash (hexdigest)
    """
    if seed is None:
        seed = getrandbits(128)

    if not isinstance(seed, str):
        seed = str(seed)

    hasher = hashlib.sha3_256()
    hasher.update(seed.encode())
    return hasher.hexdigest()
