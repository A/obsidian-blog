from src.entities.matcher.match import Match


class AbstractMatcher:
    @classmethod
    def match(cls, content: str):
        raise NotImplementedError('Should have implemented this')
