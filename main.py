import json
import random
import typing


class Corpus:
    weight: float
    generic: bool
    keywords: typing.List[str]
    content: str

    def __init__(self, weight, generic, keywords, content):
        self.weight = weight
        self.generic = generic
        self.keywords = keywords
        self.content = content

    def __repr__(self):
        return f'(weight={self.weight},generic={self.generic},keywords={self.keywords},content={self.content})'


class ZaunBot:
    def __init__(self):
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            self.spec_keywords = set()
            self.base_keywords = set(data['baseKeywords'])
            self.corpora: typing.List[Corpus] = []
            for corpus in data['corpus']:
                self.corpora.append(Corpus(**corpus))
            for corpus in self.corpora:
                self.spec_keywords |= set(corpus.keywords)
            self.keywords = self.base_keywords | self.spec_keywords

    def list_generic_answer(self) -> typing.List[str]:
        """
        返回所有通用的骂人的话
        @return:
        """
        answers = list(map(lambda x: x.content, filter(lambda x: x.generic is True, self.corpora)))
        return answers

    def get_one_generic_answer(self) -> str:
        """
        返回一句通用骂人话
        @return:
        """
        answers = self.list_generic_answer()
        return random.choice(answers)

    def words_in_text(self, words: typing.Iterable[str], text: str) -> bool:
        """
        关键词是否包含在语句里
        :param words:
        :param text:
        :return:
        """
        for word in words:
            if word in text:
                return True
        return False

    def list_corpus_from_word(self, word: str) -> typing.List[Corpus]:
        res = []
        for corpus in self.corpora:
            if word in corpus.keywords:
                res.append(corpus)
        return res

    def list_corpus_from_words(self, words: typing.Iterable[str]) -> typing.List[Corpus]:
        res = set()
        for word in words:
            corpus_list = self.list_corpus_from_word(word)
            for corpus in corpus_list:
                res.add(corpus)
        return list(res)

    def get_matched_spec_words(self, text: str) -> typing.List[str]:
        res = []
        for word in self.spec_keywords:
            if word in text:
                res.append(word)
        return res

    def match_text(self, text: str):
        """
        输入骂人的话，匹配最佳回骂
        1. 包含具体关键词，优先返回具体回骂
        2. 包含基本关键词，返回通用回骂
        @param text:
        """
        matched_spec_words = self.get_matched_spec_words(text)
        if matched_spec_words:
            corpora = self.list_corpus_from_words(matched_spec_words)
            return random.choice(corpora).content
        return self.get_one_generic_answer()


if __name__ == '__main__':
    print(ZaunBot().match_text('我操你妈的狗东西'))
