class Cyclemin:
    def bestmod(self, s, k):
        res = s
        s_l = list(s)
        for i in range(len(s_l)):
            s_l.append(s_l[0])
            s_l = s_l[1:]
            tmp = s_l[:]
            k1 = k
            for j in range(len(tmp)):
                if k1 == 0: break
                if tmp[j] == 'a': continue
                tmp[j] = 'a'
                k1 -= 1
            res = min(res, ''.join(tmp))
                      
        return ''.join(res)