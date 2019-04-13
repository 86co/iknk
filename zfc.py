sys.setrecursionlimit(65536)    #再起深度の上限

ext     = lambda a, b: True if all([i in b for i in a]) and all([i in a for i in b]) else False
pair    = lambda a, b: [a] if ext(a, b) else [a, b]
union   = lambda a: [i for j in a for i in j]

suc     = lambda a: union(pair(a,pair(a,a)))

pred_re = lambda a, b: b if ext(suc(b), a) else pred_re(a, suc(b))
pred    = lambda a: [] if ext(a, []) else pred_re(a, [])

add     = lambda a, b: a if ext(b, []) else add(suc(a), pred(b))
multi   = lambda a, b: [] if ext(b, []) else add(multi(a, pred(b)), a)