import tkinter as tk
from tkinter import ttk

def create_table():
    # 创建主窗口
    root = tk.Tk()
    root.title("LR(0) 分析")
    root.iconbitmap('misc/favicon.ico')
    
    # 创建标题标签
    title_label = tk.Label(root, text="对输入串 bccd# 的 LR(0) 分析过程", font=("Arial", 10))
    title_label.pack(pady=8)
    
    # 创建表格
    table = ttk.Treeview(root, height=20)
    table["columns"] = ("Steps", "StatusStack", "SignStack","String","ACTION","GOTO")
    
    # 设置列宽
    table.column("#0", width=0, stretch=tk.NO)
    table.column("Steps", width=100)
    table.column("StatusStack", width=100)
    table.column("SignStack", width=100)
    table.column("String", width=150)
    table.column("ACTION", width=100)
    table.column("GOTO", width=100)
    
    # 设置列标题
    table.heading("#0", text="", anchor=tk.W)
    table.heading("Steps", text="步骤")
    table.heading("StatusStack", text="状态栈")
    table.heading("SignStack", text="符号栈")
    table.heading("String", text="输入串")
    table.heading("ACTION", text="ACTION")
    table.heading("GOTO", text="GOTO")
    
    # 添加数据
    table.insert("", tk.END, text="1", values=("1", '#S', "i+i*i#",'S -> TE'))
    table.insert("", tk.END, text="2", values=("2", '#ET', "i+i*i#",'T -> FU'))
    table.insert("", tk.END, text="3", values=("3", '#ETF', "i+i*i#",'F -> i'))
    
    # 显示表格
    table.pack()
    
    # 创建新的弹窗
    new_window = tk.Toplevel(root)
    new_window.title("LR(0) 分析表")
    new_window.iconbitmap('misc/favicon.ico')

   # 创建标题标签
    title_label = tk.Label(new_window, text="LR(0) 分析表", font=("Arial", 10))
    title_label.pack(pady=8)

    # 创建表格
    table2 = ttk.Treeview(new_window, height=20)
    # 这里 non 的填充个数视状态个数决定
    table2["columns"] = ("Status", "ACTION", "non1","GOTO","non-1")
    
    # 设置列宽
    table2.column("#0", width=0, stretch=tk.NO)
    for column in ("Status", "ACTION", "GOTO", "non1", "non-1"):
        table2.column(column, width=100)
    
    # 设置列标题
    table2.heading("#0", text="", anchor=tk.W)
    table2.heading("Status", text=" ")
    table2.heading("ACTION", text="ACTION")
    table2.heading("GOTO", text="GOTO")
    table2.heading("non1", text=" ")
    table2.heading("non-1", text=" ")
    
    # 添加数据
    table2.insert("", tk.END, text="1", values=("状态", 'a', "#",'E','A'))
    # ↑ 添加第二行的状态集
    table2.insert("", tk.END, text="2", values=("0", 'S1', 'S2','1','2'))
    
    # 显示表格
    table2.pack()

    # 运行主循环
    root.mainloop()

# 调用函数创建表格
create_table()