class Quiz:
    """Класс для квиз-викторины."""

    quizzes = []

    def __init__(
            self, question, answers,
            correct_answer, named_correct_answer, image_path=None):
        """Создание объекта викторины."""
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.named_correct_answer = named_correct_answer
        self.image_path = image_path
        Quiz.quizzes.append(self)

    def make_quiz(self):
        """Создание списка викторины."""
        for quizz in self:
            Quiz(*quizz)
        return Quiz.quizzes

    def find_index(self, question):
        """Определение индекса в списке."""
        for index in range(len(self)):
            if self[index].question == question:
                return index
