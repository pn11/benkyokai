'''1. LR で region を区切る
2. 区切った中で、(Rの数+1)/2+(Lの数)/2 が十分時間が経った偶数回後にRの上にいる数、
   (Rの数)/2+(Lの数+1)/2 がLの上にいる数。'''
import re

S = input()

LRpos = [s.start() for s in re.finditer('LR', S)]
LRpos.insert(0, -1)
LRpos.append(len(S))

final_state = [0]*len(S)

for i in range(len(LRpos)-1):
    part_str = S[LRpos[i]+1:LRpos[i+1]+1]
    RLpos = part_str.find('RL')
    num_R = RLpos+1
    num_L = len(part_str) - num_R

    final_state[LRpos[i]+RLpos+1] = (num_R+1)//2 + num_L//2
    final_state[LRpos[i]+RLpos+2] = (num_R)//2 + (num_L+1)//2

print(' '.join(str(i) for i in final_state))
