# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import gc
import json
from scipy.stats import f_oneway

class NodeLogcalls:
    ''' 参数为节点logcalls路径 '''
    def __init__(self, path):
        with open(path, "r") as f:
            self._datas = f.read()
        self._datas = self._datas.split('\n')
        self._datas = self._datas[:-1] # 最后一行为空白，去掉

        # 函数调用信息（self._data为全部的原始数据信息）
        self.calls = list()

        # logcall的元素为 (函数调用时间, 函数名)
        self.logcalls = list()

        # called_func 的元素为所有被调用的函数名，没有重复
        self.called_func = list()

        # 时间窗口集合
        self.timewinds_logcalls = list()
        self.timewindows_func_count = list()

        '''
        pure_calls从logcalls中提取所有被调用的函数,
        不包含函数调用时间，
        用来根据函数名计算函数调用次数
        '''
        self.pure_calls = list()

        self._exec_trim()
        self.called_func = self._calc_calledfunc(self.logcalls)


    ''' 整理原始数据, 获得函数调用信息 '''
    def _exec_trim(self):
        # i, totals = 0, len(self._datas)
        self.calls = self._datas[:]

        for k in self.calls:
            line = k.split(' ')
            self.logcalls.append((line[0],line[-1]))

        for k, v in self.logcalls:
            self.pure_calls.append(v)



    ''' 计算被调用的函数 '''
    def _calc_calledfunc(self, logcalls = None):
        # called_func 的元素为所有被调用的函数名，没有重复
        tmp = list()
        for e in logcalls:
            if e[1] not in tmp:
                tmp.append(e[1])

        return tmp


    ''' 获得被调用的函数 '''
    def get_calledfunc(self):
        # called_func 的元素为所有被调用的函数名，没有重复
        return self.called_func


    ''' 获得所有被调用函数以及被调用次数 '''
    def get_all_calledfunc_count(self, called_func, pure_calls):
        dict_f = {}
        for f in called_func:
            dict_f[f] = pure_calls.count(f)
        return dict_f


    ''' 获得指定的函数被调用次数, 返回次数 '''
    def get_func_count(self, func_name):
        return self.pure_calls.count(func_name)


    ''' 获得指定函数被调用次数, 返回函数名与次数 '''
    def get_funcs_count(self, *args):
        foo = dict()
        for e in args:
            foo[e] = self.get_func_count(e)


    """ 帮助GC释放无用的内存, 否则数据太大就会崩掉的 """
    def help_gc(self):
        self._datas = None
        self.calls = None
        gc.collect()


    """ 根据指定logcalls返回所有函数名 """
    def get_pure_func(self, logcalls):
        tmp = list()
        for k, v in self.logcalls:
            tmp.append(v)
        return tmp


    """ 按时间窗分割数据 """
    def split_timewindow(self, time_gap):
        self.timewinds_logcalls = list()
        start_time = int(self.logcalls[1][0])
        gap_start = start_time

        cnt_start = 0
        cnt = 0
        for e in self.logcalls:
            cnt += 1
            if int(e[0]) >  gap_start + time_gap:
                cnt = cnt-1 if cnt > 0 else cnt    # 回退一个位置的数据为时间窗口区间最后一个数据
                self.timewinds_logcalls.append(self.logcalls[cnt_start: cnt])
                cnt_start = cnt
                gap_start += time_gap

        log_and_pure_calls = list()

        for e in self.timewinds_logcalls:
            log_and_pure_calls.append((self._calc_calledfunc(e), self.get_pure_func(e)))

        timewindows_func_count = list()
        for e in log_and_pure_calls:
            timewindows_func_count.append(self.get_all_calledfunc_count(e[0], e[1]))
        self.timewindows_func_count = timewindows_func_count

        return timewindows_func_count



    def get_statistic_timewind(self, func_name, time_gap):
        ''' param: func_name 函数/任务名
            param: time_gap  时间窗口大小
            返回指定函数依据时间窗口获得的统计量
            ex: a1 = [12, 14, 16]
                a2 = [13, 10, 20] 这种形式
        '''
        a = list()
        for e in self.split_timewindow(time_gap):
            if func_name in e:
                a.append(e[func_name])
            else:
                a.append(0)
        return a



    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.get_all_calledfunc_count(self.called_func, self.pure_calls)))


def get_route_related_fun(nodes, func_name, time_gap, alpha = 0.05):
    ''' param: nodes     所有节点数据
        param: func_name 要判断的函数/任务名
        param: time_gap  统计的时间窗口大小(ms), 该参数决定样本容量
        param: alpha     显著水平

        return: True     经过方差分析, 多组数据之间的差异具有统计学意义,
                         即该函数的调用次数与组间因素(不同路由)的影响有关
                False    反之

        根据指定alpha返回某函数是否路由相关
        该函数基于方差分析, 且没有进行方差齐检验
    '''
    all_statistic = list()
    for e in nodes.values():
        all_statistic.append(e.get_statistic_timewind(func_name, 1500))
    f, p = f_oneway(*all_statistic)
    print f, p
    return True if p < alpha else False



''' 获得指定数量的子图, 子图数量总是4的倍数 31857'''
def get_axs(num = 140):
    axs = list()
    for i in range(1, num/4+1):
        plt.figure(i)
        for i in range(1, 5):
            axs.append(plt.subplot(24*10 + i))

    if num % 4 != 0:
        plt.figure(num/4+1)
        for i in range(1, 5):
            axs.append(plt.subplot(24*10 + i))
    return axs




if __name__ == '__main__':
    path = "/media/tete/F/TinyOS/wsnA/logcalls-logs/"  # 数据路径
    result_path = "C:/Users/Administrator/Desktop/tools/cooja/TaskCalls/result/5-result/" # 结果路径
    node_amount = 2             #节点数量
    nodes = dict()              # 存储所有节点的NodeLogcalls实例
    for i in range(1, node_amount+1):
        print str(i) + ' node has been created.'
        nodes['node_'+str(i)] = NodeLogcalls(path + str(i) + '.txt')
        #nodes['node_'+str(i)].help_gc()
        #nodes['node_'+str(i)].save_to_file(result_path+'node_'+str(i)+'.txt')




    """ 找出调用函数最多的节点, 以及调用函数的数量这样可
    以在统计中覆盖到所有的函数，并且构造合适数量的子图
    """
    most_func_node = {'node_1': 0}
    most_func_node['node_1'] = len(nodes['node_1'].get_calledfunc())
    for e in nodes:
        foo = nodes[e].get_calledfunc()
        if len(foo) > most_func_node[most_func_node.keys()[0]]:
            most_func_node = {e: len(foo)}

    print 'the number of total functions = ', most_func_node[most_func_node.keys()[0]]



    """ 获取调用函数最多节点的中被调用的所有函数 """
    allfunc = list()
    allfunc = nodes[most_func_node.keys()[0]].get_calledfunc()



    """  x坐标为节点编号, 本例为(1 - 40)"""
    x_nodes = [i for i in range(1, node_amount+1)]
    y_logcalls = list()

    ''' work prefect '''
    for e in nodes['node_1'].called_func:
        print get_route_related_fun(nodes, e, 500)

    """ 获取一定数量的子图， 每个子图用来描述一个函数，
    子图是由一个大图分成四个小图得来的，因此子图数量总是
    4的倍数， 例如获取10个子图， 则该函数返回12个子图
    """
    '''
    axs = get_axs(most_func_node[most_func_node.keys()[0]])
    select_ax = 0   # 选择的子图位置
    for e in allfunc:
        """ 画图
        画图有些耗时间，耐心等待。
        """
        y_logcalls = list()
        for i in x_nodes:
            y_logcalls.append(nodes['node_'+str(i)].get_func_count(e))
        plt.sca(axs[select_ax])#交替让axs成为当前Axes对象
        plt.plot(x_nodes, y_logcalls)
        select_ax += 1
        print str(e), select_ax, ' is over.\n\n'
        '''
