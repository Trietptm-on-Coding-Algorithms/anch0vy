import ann
import pprint
for x in range(10):
    l_nn = ann.make_nn(4,5,2)
    ann.cpu([1,0,1,0],l_nn)
    print '==========================='
