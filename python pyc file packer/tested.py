def ent():
  import sys
  import math 
  s='wow'
  counts=[0]*256
  entropy=0
  fr=s
  for xx in fr:
    counts[ord(xx)]+=1
  for count in counts:
    if count==0:
      continue
    p=1.0*count/len(fr)
    entropy -=p * math.log(p, 256)
  print '[*]%s : %f'%(s,entropy)