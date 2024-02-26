from Alignment_algorithms.Sequence_alignment.weighted_gap_global_align import WeightedGapAlign

MATCH = 1
MISSMATCH = -1
s = input()
t = input()
gap_open, gap_cont = map(int, input().split())
# algo = NeedlemanWunschAlgorithm(matrix=blossum_matrix, gap_score=GAP_SCORE)
algo = WeightedGapAlign(match_score=MATCH, missmatch_score=MISSMATCH, gap_open=gap_open, gap_cont=gap_cont)
A, B = algo.align(s, t)
# print(algo.get_max_weight())
print(A)
print(B)
