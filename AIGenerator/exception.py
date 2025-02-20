
class QuestionParsingError(Exception):
    """ 当解析问题数据失败时，抛出此异常 """
    def __init__(self, message="Failed to parse the question data", details=None):
        super().__init__(message)
        self.details = details