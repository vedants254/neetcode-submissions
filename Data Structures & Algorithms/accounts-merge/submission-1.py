class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n =len(accounts)
        emailsId={}
        emails=[]
        emailtoacc={}

        m=0
        for accid,a in enumerate(accounts):
            for i in range(1,len(a)):
                email=a[i]
                if email in emailsId:
                    continue
                emails.append(email)
                emailsId[email]=m
                emailtoacc[m]=accid
                m+=1
        adj=[[] for i in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                id1=emailsId[a[i]]
                id2=emailsId[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        emailgrp=defaultdict(list)
        visited=[False]*m
        def dfs(node,accid):
            visited[node]=True
            emailgrp[accid].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,accid)
        for i in range(m):
            if not visited[i]:
                dfs(i,emailtoacc[i])

        res=[]
        for accid in emailgrp:
            name=accounts[accid][0]
            res.append([name]+sorted(emailgrp[accid]))
        return res 