# Football_Teamクラス
class Football_Team :
    # 初期化メソッド
    def __init__(self, name, win, lose, draw) :
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw
    # 勝率を計算するメソッド
    def calc_win_rate(self) :
        rate = self.win / (self.win + self.lose)
        return rate
    # 結果を表示するメソッド
    def show_team_result(self) :
        msg = f'{self.name:<12s} {self.win:>3d} {self.lose:>3d} {self.draw:>3d} {self.calc_win_rate():.3f}'
        print(msg)
