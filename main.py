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
            data = f.read()
            self.corpora = json.loads(data)

    def list_generic_answer(self) -> typing.List[str]:
        """
        返回所有通用的骂人的话
        @return:
        """
        answers = list(map(lambda x: x.content, self.corpora))
        return answers

    def get_one_generic_answer(self) -> str:
        """
        返回一句通用骂人话
        @return:
        """
        answers = self.list_generic_answer()
        return random.choice(answers)

    def match_text(self, text: str):
        """
        输入骂人的话，匹配最佳回骂
        @param text:
        """
        pass


if __name__ == '__main__':
    print(ZaunBot().corpora)
