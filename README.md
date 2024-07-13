# isolation-forest-weighted-


Based on the implementation of rrcf done by [mgckind](https://github.com/mgckind/iso_forest.git), 
I only changed some part of the def make_tree(self,X,e,l) as follows:
(This is very simple but powerful)

    def make_tree(self,X,e,l):
        self.e = e
        if e >= l or len(X) <= 1:
            left = None
            right = None
            self.exnodes += 1
            return Node(X, self.q, self.p, e, left, right, node_type = 'exNode' )
        else:
            self.q = rn.choice(self.Q)
            mini = X[:,self.q].min()
            maxi = X[:,self.q].max()
            if mini==maxi:
                left = None
                right = None
                self.exnodes += 1
                return Node(X, self.q, self.p, e, left, right, node_type = 'exNode' )
            epsilon = (maxi-mini)/(2*(len(X[:,self.q]) -1) )
            
            num_nd = 1
            self.p = rn.uniform(mini,maxi)
            while num_nd != 0 :
                self.p = rn.uniform(mini, maxi)
                num_nd = sum((self.p-epsilon <= X[:,self.q]) &  (X[:,self.q] < self.p+epsilon))
                if num_nd < 2:
                    break;
            w = np.where(X[:,self.q] < self.p,True,False)
            return Node(X, self.q, self.p, e,\
            left=self.make_tree(X[w],e+1,l),\
            right=self.make_tree(X[~w],e+1,l),\
            node_type = 'inNode' )
 


Details are [Here](https://arxiv.org/abs/2202.01891)


