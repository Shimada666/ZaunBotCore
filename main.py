import json
import random
import typing


class Corpus:
    weight: float
    generic: bool
    keywords: typing.List[str]
    content: str


class ZaunBot:
    def __init__(self):
        with open('data.json', 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            self.spec_keywords = set()
            self.base_keywords = data['baseKeywords']
            self.corpora = data['corpus']
            for corpus in self.corpora:
                self.spec_keywords |= set(corpus['keywords'])

    def list_generic_answer(self) -> typing.List[str]:
        """
        返回所有通用的骂人的话
        @return:
        """
        answers = list(map(lambda x: x['content'], filter(lambda x: x['generic'] is True, self.corpora)))
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

    def match_text(self, text: str):
        """
        输入骂人的话，匹配最佳回骂
        1. 包含具体关键词，优先返回具体回骂
        2. 包含基本关键词，返回通用回骂
        @param text:
        """
        # if self.words_in_text(self.base_keywords, text):

        return self.get_one_generic_answer()


if __name__ == '__main__':
    print(ZaunBot().corpora)
    print(ZaunBot().base_keywords)
    print(ZaunBot().spec_keywords)
    print(ZaunBot().list_generic_answer())
    print(ZaunBot().get_one_generic_answer())
