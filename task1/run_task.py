from task1.Alignment_algorithms.Sequence_alignment.Needleman_Wunsch_algorithm import NeedlemanWunschAlgorithm
from blossum_matrix import matrix as blossum_matrix

GAP_SCORE = -5
s = input()
t = input()
algo = NeedlemanWunschAlgorithm(matrix=blossum_matrix, gap_score=GAP_SCORE)
A, B = algo.align(s, t)
print(A)
print(B)
