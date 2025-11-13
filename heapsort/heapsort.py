from typing_extensions import runtime
from manim import *

class Heapsort(Scene):
    def construct(self):
        #开场
        textInfo_1 = Text("堆排序",font_size=20)
        textInfo_2 = Text("戴上耳机，一起静心领悟",font_size=15,font="Trebuchet MS",slant=ITALIC).shift(DOWN*1.5)
        
        self.play(Write(textInfo_1),runtime = 2)
        self.wait(1)
        self.play(Write(textInfo_2),runtime = 2)
        self.wait(1)
        self.play(FadeOut(textInfo_1),FadeOut(textInfo_2),runtime=1)

        #动画一
        arrUnsorted = ["4","10","3","5","1"]
        arrSorted = ["1","3","4","5","10"]
        arrUnsorted_group = VGroup(*[Text(ele,font_size=20)for ele in arrUnsorted]).arrange(RIGHT,buff=0.2)
        self.play(Write(arrUnsorted_group),runtime=2)
        self.play(arrUnsorted_group.animate.shift(UP*0.5),runtime = 1)
        
        textInfo = Text("如何升序排序为",font_size=15).next_to(arrUnsorted_group,DOWN,buff=0.3)
        arrSorted_group = VGroup(*[Text(ele,font_size=20)for ele in arrSorted]).arrange(RIGHT,buff=0.2).next_to(textInfo,DOWN,buff=0.2)
        self.play(Write(textInfo),runtime = 1.5)
        self.play(FadeOut(arrUnsorted_group),runtime = 0.3)
        self.play(Write(arrSorted_group),runtime = 2)
        self.wait(2)
        self.play(FadeOut(arrSorted_group,textInfo),runtime = 0.3)
        self.play(Write(arrUnsorted_group),runtime = 1.5)
        self.play(arrUnsorted_group.animate.set_color(GREEN))
        self.wait(1)
        self.play(arrUnsorted_group[1].animate.set_color(RED))
        self.play(arrUnsorted_group[1].animate.shift(DOWN*0.5+RIGHT*1))
        self.play(arrUnsorted_group[1].animate.set_color(WHITE))
        
        self.play(arrUnsorted_group[3].animate.set_color(RED))
        self.play(arrUnsorted_group[3].animate.next_to(arrUnsorted_group[1],LEFT,buff=0.3))
        self.play(arrUnsorted_group[3].animate.set_color(WHITE))

        self.play(arrUnsorted_group[0].animate.set_color(RED))
        self.play(arrUnsorted_group[0].animate.next_to(arrUnsorted_group[3],LEFT,buff=0.3))
        self.play(arrUnsorted_group[0].animate.set_color(WHITE))

        self.play(arrUnsorted_group[2].animate.set_color(RED))
        self.play(arrUnsorted_group[2].animate.next_to(arrUnsorted_group[0],LEFT,buff=0.3))
        self.play(arrUnsorted_group[2].animate.set_color(WHITE))

        self.play(arrUnsorted_group[4].animate.set_color(RED))
        self.play(arrUnsorted_group[4].animate.next_to(arrUnsorted_group[2],LEFT,buff=0.3))
        self.play(arrUnsorted_group[4].animate.set_color(WHITE))
        self.wait(1)

        textMax = Text('每次选出未排序元素中的最大值',font_size=15,t2c={"最大值":RED}).shift(DOWN*0.5)
        self.play(Write(textMax),runtime = 6)
        self.wait(2)
        self.play(FadeOut(textMax),FadeOut(arrUnsorted_group),runtime=1)
        
        #动画二
        arrUnsorted_group.arrange(RIGHT, buff=0.2)
        self.play(Create(arrUnsorted_group),runtime=2)
        self.play(arrUnsorted_group.animate.shift(UP*0.5),runtime = 1)

        textArr = Text("数组",font_size=15).next_to(arrUnsorted_group,DOWN,buff=0.2)
        textBinTree = Text("看作一个完全二叉树",font_size=15).next_to(arrUnsorted_group,DOWN,buff=0.2)
        self.play(Write(textArr),runtime = 1.5)
        self.wait(1)
        self.play(FadeOut(textArr))

        self.play(Write(textBinTree),runtime = 1.5)
        self.wait(1.5)
        self.play(FadeOut(textBinTree))

        self.play(arrUnsorted_group.animate.shift(LEFT*3.5))

        #画二叉树
        textNum_4 = Text("4",font_size=20).shift(UP*1+RIGHT*2.5)
        textNum_10 = Text("10",font_size=20).shift(UP*0.3+RIGHT*1.85)
        textNum_3 = Text("3",font_size=20).next_to(textNum_10,RIGHT,buff=1.1)
        textNum_5 = Text("5",font_size=20).shift(DOWN*0.3+RIGHT*1.35)
        textNum_1 = Text("1",font_size=20).next_to(textNum_5,RIGHT,buff=1.1)
        
        line_4to10 = Line(start=textNum_4,end=textNum_10).set_length(0.45)
        line_4to3 = Line(start=textNum_4,end=textNum_3).set_length(0.45)
        line_10to5 = Line(start=textNum_10,end=textNum_5).set_length(0.45)
        line_10to1 = Line(start=textNum_10,end=textNum_1).set_length(0.45)

        self.play(Write(textNum_4))
        self.play(Write(textNum_10),Write(textNum_3))
        self.play(Create(line_4to10),Create(line_4to3))
        self.play(Write(textNum_5),Write(textNum_1))
        self.play(Create(line_10to5),Create(line_10to1))
        self.wait(2)

        #对应关系高亮显示
        arrArrownum = Arrow(
            start = ORIGIN,
            end = UP*0.5,
            buff = 0,
            max_tip_length_to_length_ratio=0.1,
            tip_length = 0.5
        ).next_to(arrUnsorted_group[1],DOWN,buff=0.1)
        textNumindex = Text("索引为i",font_size=15).next_to(arrArrownum,DOWN,buff=0.1)
        arrIndexgroup = VGroup(arrArrownum,textNumindex)
        textLeftChild = Text("左孩子索引=2*i+1",font_size=15,t2c={"左孩子":GREEN}).next_to(textNumindex,DOWN,buff=0.2)
        textRightChild = Text("右孩子索引=2*i+2",font_size=15,t2c={"右孩子":YELLOW}).next_to(textLeftChild,DOWN,buff=0.2)
        self.play(Create(arrIndexgroup),runtime = 2.5)
        self.play(textNum_10.animate.set_color(RED))
        self.play(Write(textLeftChild),Write(textRightChild))
        self.wait(1)
        self.play(textNum_5.animate.set_color(GREEN))
        self.play(textNum_1.animate.set_color(YELLOW))
        self.wait(2)
        self.clear()
        
        #动画三
        textHeapSpe = Text("堆是一种特殊的完全二叉树",font_size=20)
        self.play(Write(textHeapSpe),runtime = 1)
        self.wait(2)
        self.play(textHeapSpe.animate.shift(UP*3.5))
        lineMid = Line(start=UP,end=ORIGIN).set_length(5)
        textMaxHeap = Text("大顶堆",font_size=20).shift(UP*3+LEFT*3.5)
        textMaxHeapInfo = Text("每个节点的值不小于子节点的值",font_size=18,t2c={"不小于":RED}).next_to(textMaxHeap,DOWN,buff=0.3)
        textMinHeap = Text("小顶堆",font_size=20).shift(UP*3+RIGHT*3.5)
        textMinHeapInfo = Text("每个节点的值不大于子节点的值",font_size=18,t2c={"不大于":RED}).next_to(textMinHeap,DOWN,buff=0.3)
        self.play(Create(lineMid))
        self.play(Write(textMaxHeap),runtime = 1.5)
        self.play(Write(textMaxHeapInfo),runtime = 1.5)
        self.wait(1)

        #画大顶堆示例
        textMaxheapNum_10 = Text("10",font_size=15).next_to(textMaxHeapInfo,DOWN,buff=1.2)
        textMaxheapNum_9 = Text("9",font_size=15).next_to(textMaxheapNum_10,DOWN,buff=0.5).shift(LEFT*0.8)
        textMaxheapNum_8 = Text("8",font_size=15).next_to(textMaxheapNum_9,RIGHT,buff=1.55)
        textMaxheapNum_7 = Text("7",font_size=15).next_to(textMaxheapNum_9,DOWN,buff=0.5).shift(LEFT*0.8)
        textMaxheapNum_6 = Text("6",font_size=15).next_to(textMaxheapNum_7,RIGHT,buff=1.45)
        lineMaxheap10to9 = Line(start=textMaxheapNum_10,end=textMaxheapNum_9).set_length(0.6)
        lineMaxheap10to8 = Line(start=textMaxheapNum_10,end=textMaxheapNum_8).set_length(0.6)
        lineMaxheap9to7 = Line(start=textMaxheapNum_9,end=textMaxheapNum_7).set_length(0.6)
        lineMaxheap9to6 = Line(start=textMaxheapNum_9,end=textMaxheapNum_6).set_length(0.6)
        self.play(Write(textMaxheapNum_10))
        self.play(Write(textMaxheapNum_9),Write(textMaxheapNum_8))
        self.play(Create(lineMaxheap10to9),Create(lineMaxheap10to8))
        self.play(Write(textMaxheapNum_7),Write(textMaxheapNum_6))
        self.play(Create(lineMaxheap9to7),Create(lineMaxheap9to6))
        self.wait(1.5)

        #画小顶堆示例
        self.play(Write(textMinHeap),runtime = 1.5)
        self.play(Write(textMinHeapInfo),runtime = 1.5)
        self.wait(1)
        textMinheapNum_1 = Text("1",font_size=15).next_to(textMinHeapInfo,DOWN,buff=1.2)
        textMinheapNum_2 = Text("2",font_size=15).next_to(textMinheapNum_1,DOWN,buff=0.5).shift(LEFT*0.8)
        textMinheapNum_3 = Text("3",font_size=15).next_to(textMinheapNum_2,RIGHT,buff=1.55)
        textMinheapNum_4 = Text("4",font_size=15).next_to(textMinheapNum_2,DOWN,buff=0.5).shift(LEFT*0.8)
        textMinheapNum_5 = Text("5",font_size=15).next_to(textMinheapNum_4,RIGHT,buff=1.55)
        lineMinheap1to2 = Line(start=textMinheapNum_1,end=textMinheapNum_2).set_length(0.6)
        lineMinheap1to3 = Line(start=textMinheapNum_1,end=textMinheapNum_3).set_length(0.6)
        lineMinheap2to4 = Line(start=textMinheapNum_2,end=textMinheapNum_4).set_length(0.6)
        lineMinheap2to5 = Line(start=textMinheapNum_2,end=textMinheapNum_5).set_length(0.6)
        
        self.play(Write(textMinheapNum_1))
        self.play(Write(textMinheapNum_2),Write(textMinheapNum_3))
        self.play(Create(lineMinheap1to2),Create(lineMinheap1to3))
        self.play(Write(textMinheapNum_4),Write(textMinheapNum_5))
        self.play(Create(lineMinheap2to4),Create(lineMinheap2to5))
        self.wait(2)
        self.clear()
        # 动画四
        self.play(Write(textInfo_1),runtime = 2)
        self.wait(1)
        self.play(textInfo_1.animate.shift(UP*3.5))
        textArrsortBuild = Text("建堆",font_size=17).next_to(textInfo_1,DOWN,buff=2.3)
        textArrsortExchange = Text("交换",font_size=17).next_to(textArrsortBuild,DOWN,buff=0.3)
        self.play(Write(textArrsortBuild),runtime=1)
        self.play(Write(textArrsortExchange),runtime=1)
        self.wait(1)
        self.clear()
        textArrsortBuild.font_size = 20
        self.play(Write(textArrsortBuild),runtime=1)
        self.play(textArrsortBuild.animate.shift(UP*2+LEFT*5))
        heap_group = VGroup(
            textNum_4, textNum_10, textNum_3,
            textNum_5, textNum_1,
            line_4to10, line_4to3, line_10to5, line_10to1
        )
        heap_group.shift(UP*0.2+RIGHT*1.6)
        textInit = Text("初始二叉树结构",font_size=15).next_to(heap_group,UP,buff=0.35)
        textLast = Text("从最后一个非叶子")
        textBuildIntro = [
            "将未排序数组构建为大顶堆",
            "叶子节点天然为堆,不需要调整",
            "从最后一个非叶子节点开始建立"
            ]
        textBuildIntro_group = VGroup(*[Text(ele,font_size=15)
        for ele in textBuildIntro]).arrange(DOWN,buff=0.3).next_to(textArrsortBuild,DOWN,buff=0.2)
        arrUnsorted_group.shift(RIGHT*3)
        self.play(Write(textBuildIntro_group))
        self.wait(3)
        self.play(Write(arrUnsorted_group),runtime=2)
        lineInitUnsort = Line(start=arrUnsorted_group[0].get_center(),end=arrUnsorted_group[4].get_center()).next_to(arrUnsorted_group,DOWN,buff=0.1)
        textUnsort = Text("未排序部分",font_size=15).next_to(lineInitUnsort,DOWN,buff=0.1)
        self.play(Create(lineInitUnsort),Write(textUnsort))
        self.wait(1)
        self.play(Write(textInit))
        self.play(Write(heap_group))
        self.wait(1)
        self.play(FadeOut(textInit))
        self.play(arrUnsorted_group[1].animate.set_color(RED),textNum_10.animate.set_color(RED))
        self.play(arrUnsorted_group[3].animate.set_color(GREEN),arrUnsorted_group[4].animate.set_color(GREEN),textNum_5.animate.set_color(GREEN),textNum_1.animate.set_color(GREEN))
        self.wait(2)
        self.play(
            arrUnsorted_group[1].animate.set_color(WHITE),
            arrUnsorted_group[3].animate.set_color(WHITE),
            arrUnsorted_group[4].animate.set_color(WHITE),
            textNum_10.animate.set_color(WHITE),
            textNum_5.animate.set_color(WHITE),
            textNum_1.animate.set_color(WHITE)
        )

        self.play(
            arrUnsorted_group[0].animate.set_color(RED),
            arrUnsorted_group[1].animate.set_color(GREEN),
            arrUnsorted_group[2].animate.set_color(GREEN),
            textNum_4.animate.set_color(RED),
            textNum_10.animate.set_color(GREEN),
            textNum_3.animate.set_color(GREEN)
        )
        self.wait(2)
        
        self.play(
            arrUnsorted_group[0].animate.set_color(WHITE),
            arrUnsorted_group[1].animate.set_color(WHITE),
            arrUnsorted_group[2].animate.set_color(WHITE),
            textNum_4.animate.set_color(WHITE),
            textNum_10.animate.set_color(WHITE),
            textNum_3.animate.set_color(WHITE)
        )

        pos_4 = textNum_4.get_center()
        pos_10 = textNum_10.get_center()

        self.play(
            textNum_4.animate.move_to(pos_10),
            textNum_10.animate.move_to(pos_4),
            run_time=1.2
        )

        self.wait(2)
        self.clear()
        #动画五
        heapifycode = """void heapify(int arr[],int n,int i)
{

    int largest = i; 
    int left = 2*i+1; 
    int right = 2*i+2;
    
    if(left<n && arr[left]>arr[largest])
    {
        largest = left;
    }
    if(right<n && arr[right]>arr[largest])
    {
        largest = right;
    }
    if(largest != i)
    {
        swap(&arr[i],&arr[largest]); 
        heapify(arr,n,largest); 
    }
}"""
        heapify_code = Code(code_string=heapifycode,language="c",add_line_numbers=False,background_config={"fill_opacity": 0,"stroke_width": 0})
        textHeapifyCodeshow = Text("代码展示",font_size=20)
        self.play(Write(textHeapifyCodeshow),runtime=1)
        self.wait(1)
        self.play(FadeOut(textHeapifyCodeshow),runtime=0.5)
        self.play(Create(heapify_code))
        self.wait(3)
        self.clear()

        #动画六
        textExch = Text("交换",font_size=20)
        self.play(Write(textExch),runtime=1)
        self.play(textExch.animate.shift(UP*3))
        self.play(Write(arrUnsorted_group))
        self.play(Create(lineInitUnsort),Write(textUnsort))
        self.play(arrUnsorted_group[1].animate.set_color(RED))
        pos_fir = arrUnsorted_group[1].get_center()
        pos_sec = arrUnsorted_group[4].get_center()
        self.play(
            arrUnsorted_group[4].animate.move_to(pos_fir),
            arrUnsorted_group[1].animate.move_to(pos_sec+RIGHT*0.1),
            FadeOut(lineInitUnsort),
            FadeOut(textUnsort),
            FadeOut(textExch),
            run_time=1.2
        )
        self.wait(1)
        self.play(arrUnsorted_group[1].animate.set_color(WHITE))
        lineUnsortSec = Line(start=arrUnsorted_group[0].get_left(),end=arrUnsorted_group[3].get_right()).shift(DOWN*0.2)
        textUnsort.next_to(lineUnsortSec,DOWN,buff=0.1)
        self.play(Create(lineUnsortSec),Write(textUnsort))
        self.wait(1)

        arrowUp = Arrow(start=ORIGIN,
                    end=UP*0.5,
                    buff = 0,
                    max_tip_length_to_length_ratio=0.1,
                    tip_length = 0.3
                )
        arrowUp.next_to(textUnsort,DOWN,buff=0.1)
        textBuidAgain = Text("继续建堆",font_size=15).next_to(arrowUp,DOWN,buff=0.1)
        
        self.play(Create(arrowUp))
        self.play(Write(textBuidAgain))
        self.wait(1)
        self.play(FadeOut(arrowUp),FadeOut(textBuidAgain))
        self.play(arrUnsorted_group[3].animate.set_color(RED))
        self.play(FadeOut(lineUnsortSec),FadeOut(textUnsort))
        self.play(arrUnsorted_group[3].animate.set_color(WHITE))
        lineUnsortSec.put_start_and_end_on(arrUnsorted_group[0].get_left(),arrUnsorted_group[2].get_right()).shift(DOWN*0.2)
        textUnsort.next_to(lineUnsortSec,DOWN,buff=0.1)
        self.play(Create(lineUnsortSec),Write(textUnsort))
        self.play(arrUnsorted_group[0].animate.set_color(RED))

        pos_num4 = arrUnsorted_group[0].get_center()
        pos_num3 = arrUnsorted_group[2].get_center()
        self.play(
            arrUnsorted_group[2].animate.move_to(pos_num4),
            arrUnsorted_group[0].animate.move_to(pos_num3)
        )
        self.play(arrUnsorted_group[0].animate.set_color(WHITE))
        self.play(FadeOut(lineUnsortSec),FadeOut(textUnsort))
        lineUnsortSec.put_start_and_end_on(arrUnsorted_group[2].get_left(),arrUnsorted_group[4].get_right()).shift(DOWN*0.2)
        textUnsort.next_to(lineUnsortSec,DOWN,buff=0.1)
        self.play(Create(lineUnsortSec),Write(textUnsort))
        self.play(arrUnsorted_group[2].animate.set_color(RED))
        pos_num1 = arrUnsorted_group[4].get_center()
        self.play(
            arrUnsorted_group[2].animate.move_to(pos_num1),
            arrUnsorted_group[4].animate.move_to(pos_num4)
        )
        self.play(FadeOut(textUnsort),FadeOut(lineUnsortSec))
        self.play(arrUnsorted_group[2].animate.set_color(WHITE))
        
        textFinsh = Text("完成升序排序",font_size=15).next_to(arrUnsorted_group,DOWN,buff=0.2)
        self.play(Write(textFinsh))
        self.wait(1)
        self.clear()

        #展示交换代码
        ExchangeCode = """
        void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
        void heapSort(int arr[],int n)
{
    for(int i=n/2-1;i>=0;i--)
    {
        heapify(arr,n,i);
    }
    for(int i=n-1;i>0;i--)
    {
        swap(&arr[0],&arr[i]);
        heapify(arr,i,0); 
    }
}
        """
        exchangecode = Code(code_string=ExchangeCode,language="c",add_line_numbers=False,background_config={"fill_opacity": 0,"stroke_width": 0})
        self.play(Create(exchangecode))
        self.wait(3)
        self.play(FadeOut(exchangecode),runtime=1.5)
        #动画七
        textSummarylist = ["总的来说","建堆就是找出未排序元素中的最大或最小值","交换是建立排序的过程","堆排序就是建堆后进行交换的朴素思想"]
        textSummary = VGroup(*[Text(ele,font_size=20)for ele in textSummarylist])
        for i in range(len(textSummarylist)):
            self.play(Write(textSummary[i]),runtime=1)
            self.wait(1.5)
            self.play(FadeOut(textSummary[i]))
        # 结束
        textWasim = Text("Wasim",font_size=15,slant=ITALIC)
        self.play(Write(textWasim),runtime=2)
        self.wait(3)
        self.clear()