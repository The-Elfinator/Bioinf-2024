from Alignment_algorithms.Sequence_alignment.alignment_with_mem_opt import OptimizedAlignment
from Alignment_algorithms.Sequence_alignment.Needleman_Wunsch_algorithm import NeedlemanWunschAlgorithm

MATCH = 2
MISSMATCH = -1
GAP = -2
s = "AGTACGCA"
t = "TATGC"
algo = NeedlemanWunschAlgorithm(match_score=MATCH, missmatch_score=MISSMATCH, gap_score=GAP)
# algo = WeightedGapAlign(match_score=MATCH, missmatch_score=MISSMATCH, gap_open=gap_open, gap_cont=gap_cont)
# algo = OptimizedAlignment(match_score=MATCH, missmatch_score=MISSMATCH, gap_score=GAP)
A, B = algo.align(s, t)
dp = algo.get_dp()
for line in dp:
    for x in line:
        print(x, end='\t')
    print()
# print(algo.get_max_weight())
print(A)
print(B)
mem_algo = OptimizedAlignment(match_score=MATCH, missmatch_score=MISSMATCH, gap_score=GAP)
mem_A, mem_B = mem_algo.align(s, t)
print(mem_A)
print(mem_B)
