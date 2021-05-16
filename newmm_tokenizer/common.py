from .corpus import get_corpus

_THAI_WORDS_FILENAME = "words_th.txt"
_THAI_WORDS = None


def thai_words() -> frozenset:
    """
    Return a frozenset of Thai words such as "กติกา", "กดดัน", "พิษ",
    and "พิษภัย". \n(See: `dev/pythainlp/corpus/words_th.txt\
    <https://github.com/PyThaiNLP/pythainlp/blob/dev/pythainlp/corpus/words_th.txt>`_)
    :return: :class:`frozenset` containing words in Thai language.
    :rtype: :class:`frozenset`
    """
    global _THAI_WORDS
    if not _THAI_WORDS:
        _THAI_WORDS = get_corpus(_THAI_WORDS_FILENAME)
    return _THAI_WORDS
