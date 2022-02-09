class students:
    def __init__(self):
        name = 'student'
        age = 'student'
        class_ = 'student'

    def av_score(self, score1, score2, score3):
        score_sum = score1 + score2 + score3
        average_score = score_sum / 3
        print(average_score)


Jimmy = students()

Jimmy.av_score(10, 20, 20)


