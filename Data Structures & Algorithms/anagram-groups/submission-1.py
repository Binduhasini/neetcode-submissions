class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        st = []
        cnt=0
        for word in strs:
            st.append([''.join(sorted(word)),cnt])
            cnt+=1
        ans = []
        st.sort()
        i=0
        while(i<n):
            temp=[]
            temp.append(strs[st[i][1]])
            j=i+1
            while(j<n and st[j][0]==st[i][0]):
                temp.append(strs[st[j][1]])
                j+=1
            i=j
            ans.append(temp)
            
        # for i in range(0,n):
        #     if(vis[i]==0):
        #         temp = []
        #         temp.append(strs[i])
        #         vis[i]=1
        #         for j in range(i+1,n):
        #             if(st[i]==st[j]):
        #                 temp.append(strs[j])
        #                 vis[j]=1
        #         ans.append(temp)
    
        return ans
        