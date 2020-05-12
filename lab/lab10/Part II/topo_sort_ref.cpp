bool Graph::topological_sort()
{
	for(int i=0; i<V; ++i)
		if(indegree[i] == 0)
			q.push(i);         // 将所有入度为0的顶点入队

	int count = 0;             // 计数，记录当前已经输出的顶点数 
	while(!q.empty())
	{
		int v = q.front();      // 从队列中取出一个顶点
		q.pop();

		cout << v << " ";      // 输出该顶点
		++count;
		// 将所有v指向的顶点的入度减1，并将入度减为0的顶点入栈
		list<int>::iterator beg = adj[v].begin();
		for( ; beg!=adj[v].end(); ++beg)
			if(!(--indegree[*beg]))
				q.push(*beg);   // 若入度为0，则入栈
	}

	if(count < V)
		return false;           // 没有输出全部顶点，有向图中有回路
	else
		return true;            // 拓扑排序成功
}