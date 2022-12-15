from resh import p, pri


def chek(a):
    global meme
    def inc(a):
      return  all([a[i]<a[i+1] for i in range(len(a)-1)])
    meme ={}

    def fw(a):
        key = tuple(a)
        if key in meme:

            return meme[key]
        
        

        if inc(a):
            meme[key] = "hh"
            return True

        for inde in range(len(a)):
            print(f'ind:{inde}')
            print(f"len:{len(a)}")
            print(f"front:{a[:inde]}")
            print(f'tail:{a[inde+1:]}\n')
            if fw(a[:inde]+a[inde+1:]):
                
                meme[key] = "op"
                return False

            
        meme[key]="hm"
        return True

    if fw(a):
        return "bob"
    else: 
        return "alice"
    
p =[5, 3, 2, 1, 4]
def pri(k):
    for i in k:
        print(f"{i}:{k[i]}")
