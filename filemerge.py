import glob #查找文件系统中指定模式的路径
MyDiction={} #单词合并时每个单词的开头一般大写从而有利于识别
def Readfile(File): #这个函数面向的对象是File
    file_obj=open(File)
    try:
        while True:
            line=file_obj.readline().strip("\n") #返回一个str，（）默认一次只读一行
            if not line:
                break
	    array=line.split("\t") #返回一个两变量的list
	    if array[0] in MyDiction:
		MyDiction[array[0]].append(array[1])#append()默认加在后面
	    else:
	        MyDiction[array[0]]=[array[1]]#如果没有，第一次录入键和值，值为list
    finally:
	file_obj.close()
    return MyDiction
def main():
    list_dirs=glob.glob(r"F:\biodata\GSE48213_RAW") #glob包里的glob函数，引入当前目录下的.txt结尾的文件
    for i in list_dirs:
	Readfile(i)
    for gene_name in MyDiction:
        print ("%s\t%s"%(gene_name,"\t".join(MyDiction[gene_name])))
if __name__=='__main__': #文件运行的入口，从主函数开始
    main()
