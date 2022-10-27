import pandas as pd


class BuildFeatures:
    def __init__(self):
        # Data relating to the portuguese class grades
        self.por_df = pd.read_csv('../../data/raw/student/student-por.csv', delimiter=';')
        # Data relating to the math class grades
        self.math_df = pd.read_csv('../../data/raw/student/student-mat.csv', delimiter=';')

    def plot_dfs(self):
        pass

    def examine_dfs(self):
        # Analyze the labels we have
        por_isnull = set(self.por_df.isnull().all())
        por_isnan = set(self.por_df.isna().all())
        if len(por_isnull) >= 2 or por_isnull == {True}:
            print('The portuguese data set contains null values, strongly consider examining the extent of this.')
        if len(por_isnan) >= 2 or por_isnan == {True}:
            print('The portuguese data set contains nan values, strongly consider examining the extent of this.')

        math_isnull = set(self.math_df.isnull().all())
        math_isnan = set(self.math_df.isna().all())
        if len(math_isnull) >= 2 or math_isnull == {True}:
            print('The math data set contains null values, strongly consider examining the extent of this.')
        if len(math_isnan) >= 2 or math_isnan == {True}:
            print('The math data set contains nan values, strongly consider examining the extent of this.')

        # Visualize data sets
        self.plot_dfs()

    def run(self):
        self.examine_dfs()


if __name__ == '__main__':
    bf_obj_one = BuildFeatures()
    bf_obj_one.run()
