from typing_extensions import runtime
from manim import*

class Stack(Scene):
    def construct(self):
        #开场
        textInfo_1 = Text("进程运行中栈的工作机制",font_size=20)
        textInfo_2 = Text("戴上耳机，一起静心领悟",font_size=15,font="Trebuchet MS",slant=ITALIC).shift(DOWN*2)
        
        self.play(Write(textInfo_1))
        self.wait(1.5)
        self.play(Write(textInfo_2))
        self.wait(2)
        self.clear()

        textSimulation = Text("我们来模拟一个简单的栈结构",font="Gill Sans",font_size=15)
        
        self.play(Write(textSimulation))
        self.wait(2)
        self.clear()

        #栈动画一
        lineRight = Line(start = UP*4,end = DOWN*4).shift(RIGHT*3)
        lineLeft = lineRight.copy().shift(LEFT*6)
        textHighAd = Text("高地址,假设是0x65432100",color=RED,font_size=20).shift(LEFT*5+DOWN*3)
        textLowAd = Text("低地址,假设是0x00123456",color=GREEN,font_size=20).shift(LEFT*5+UP*3)
        textPush = Text("push(入栈)",color=RED,font="Gill Sans",font_size=15).shift(LEFT*5.7)
        textPop = Text("pop(出栈)",color=GREEN,font="Gill Sans",font_size=15).shift(RIGHT*5.7)
        textHighAdCopy = textHighAd.copy().shift(RIGHT*10)
        textLowAdCopy = textLowAd.copy().shift(RIGHT*10)
        textStack = Text("栈空间",font_size=20).shift(UP*3.7)
        textStackHead = Text("栈顶",font_size=15,color=GREEN).shift(LEFT*2.5+UP*3)
        textStackBottom = Text("栈底",font_size=15,color=RED).shift(RIGHT*2.5+DOWN*3)
        textStackHeadCopy = textStackHead.copy().shift(RIGHT*5)
        textStackBottomCopy = textStackBottom.copy().shift(LEFT*5)
        arrowLeft = Arrow(start=DOWN*3,end=UP*3,stroke_width=3,tip_length = 0.1,tip_shape=StealthTip,max_tip_length_to_length_ratio=0.1).shift(LEFT*5) #push箭头
        arrowRight = Arrow(start=UP*3,end=DOWN*3,stroke_width=3,tip_length = 0.1,tip_shape=StealthTip,max_tip_length_to_length_ratio=0.1).shift(RIGHT*5) #pop箭头
        
        self.play(Create(lineLeft),Create(lineRight))
        self.play(Write(textStack))
        self.play(Write(textHighAd),Write(textLowAd),Write(textHighAdCopy),Write(textLowAdCopy))
        self.play(Write(textStackHead),Write(textStackBottom),Write(textStackHeadCopy),Write(textStackBottomCopy))
        self.play(Create(arrowLeft),Create(arrowRight))
        self.play(Write(textPush),Write(textPop))
        self.wait(3)
        self.clear()

        #动画二
        textConstruct = Text("栈顶和栈底是两个特殊的位置",font_size=15)
        textCpu = Text("rsp和rbp这两个寄存器负责进行操作",font_size=15)
        self.play(Write(textConstruct))
        self.wait(1)
        self.play(FadeOut(textConstruct))
        self.play(Write(textCpu))
        self.wait(1)
        self.play(FadeOut(textCpu))
        self.clear()
        

        #动画三
        textRegister = Text("rsp寄存器不断变化",font_size=15)
        lineMid = Line(start=UP*3.3,end=DOWN*3.3)
        arrowRsp = Arrow(
            start=RIGHT,
            end=ORIGIN,
            buff = 0,
            max_tip_length_to_length_ratio=0.1,
            tip_length = 0.3,
            color=RED
        ).shift(RIGHT*0.25)
        textRsp = Text("rsp",font_size=15).next_to(arrowRsp,RIGHT,0.2)
        rsp_group = VGroup(arrowRsp, textRsp)
        addresses = [
            "0x00000001",
            "0x0000FFFF",
            "0x000A62B7",
            "0x006A0D3F",
            "0x0F3A27D8",
            "0x0FF1B86D"
        ]
        address_texts = VGroup(
            *[Text(addr,font_size=15)for addr in addresses
        ])
        address_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.9) 
        address_texts.next_to(lineMid, LEFT, buff=0.2)
        move_list = [4,0,2]
        self.play(Write(textRegister))
        self.wait(1)
        self.play(textRegister.animate.shift(UP*3.6))
        self.play(Create(lineMid))
        self.play(Write(address_texts))
        self.play(Create(rsp_group)) 
        for i in move_list:
            self.play(
                rsp_group.
                animate.
                move_to([1,address_texts[i].get_y(),0])
                ,runtime=1.5
            )
            self.play(
                address_texts[i].animate.set_color(RED)
            )
        self.wait(2)
        self.play(*[addr.animate.set_color(WHITE) for i, addr in enumerate(address_texts) if i in move_list], run_time=0.4)
        self.clear()
        
        #动画四
        textRegister_rbp = Text("rbp寄存器保持不变",font_size=15)
        arrowRbp = Arrow(
            start=RIGHT,
            end=ORIGIN,
            buff = 0,
            max_tip_length_to_length_ratio=0.1,
            tip_length = 0.3,
            color = GREEN
        ).move_to([0.75,address_texts[5].get_y(),0])
        textRbp = Text("rbp",font_size=15).next_to(arrowRbp,RIGHT,0.2)
        rbp_group = VGroup(arrowRbp, textRbp)
        self.play(Write(textRegister_rbp))
        self.wait(1)
        self.play(textRegister_rbp.animate.shift(UP*3.6))
        self.play(Create(lineMid)) 
        self.play(Write(address_texts))
        self.play(Create(rsp_group),Create(rbp_group))
        self.play(address_texts[5].animate.set_color(GREEN))
        for i in move_list:
            self.play(
                rsp_group.
                animate.
                move_to([1,address_texts[i].get_y(),0])
                ,runtime=1.5
            )
            self.play(
                address_texts[i].animate.set_color(RED)
            )
        self.wait(2)
        self.clear()
        
        #动画五
        textStackFrame = ["每调用一个函数","就会在栈空间上开辟一个新的栈帧","我会展示一段C代码","就是我博客里面的那个例子","你可以暂停复习一下"]
        StackFrame_group = VGroup(*[Text(element,font_size=20)for element in textStackFrame])
        for i, t in enumerate(StackFrame_group):
            self.play(Write(t))         
            self.wait()
            self.play(FadeOut(StackFrame_group[i]))                            

        #动画六
        code = Code(code_string="""#include <stdio.h>
            int function_3(int a,int b)
            {
                return a+b;
            }
            int function_2(int a,int b)
            {
                return function_3(a,b);
            }
            int function_1(int a,int b)
            {
                return function_2(a,b);
            }

            int main()
            {
                int x = function_1(2,3);
                printf("%d\\n",x);
                return 0;
            }""",
            tab_width=4,                 
            language="C",
            background="window"                        
        )

        self.play(Write(code))
        self.wait(3)
        self.clear()

        #动画七
        textFunction = ["不难发现","function_1调用了function_2","function_2调用了function_3","function_3完成加法逻辑","而返回时就要依次返回","完成以上过程就要依赖"]
        Function_group = VGroup(*[Text(element,font_size=20)for element in textFunction])
        textFrame = Text("栈帧",font_size=30)
        for i, t in enumerate(Function_group):
            self.play(Write(t))         
            self.wait(1)
            self.play(FadeOut(Function_group[i])) 
        self.play(Write(textFrame))
        self.wait(1)
        self.play(textFrame.animate.shift(UP*3.3+LEFT*5.5))
        self.wait(0.5)

        # 展示汇编语句（栈帧建立过程）
        asm_lines = [
            "push rbp",
            "mov rbp, rsp",
            "...",
            "mov rsp,rbp",
            "pop rbp",
            "ret"
        ]

        asm_group = VGroup(*[
            Text(line,font_size=26)
            for line in asm_lines
        ]).arrange(DOWN, aligned_edge=LEFT).move_to(ORIGIN)

        # 每一行依次出现，带轻微时间间隔
        for line in asm_group:
            self.play(Write(line), run_time=0.7)
            self.wait(0.3)

        rectUp = Rectangle(
            width=3, 
            height=1,         
            stroke_width=3,    
            fill_opacity=0      
        ).shift(UP*0.95)
        arrowFrameUp = Arrow(
            start=LEFT,
            end=LEFT*2.5,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        ).next_to(rectUp,LEFT,buff=0)
        textFrameUp = Text("栈帧结构建立",font_size=18).next_to(arrowFrameUp,LEFT,buff=0.1)
        
        rectDown = Rectangle(
            width=3, 
            height=1.5,         
            stroke_width=3,    
            fill_opacity=0      
        ).shift(DOWN*0.75)
        arrowFrameDown = Arrow(
            start=LEFT,
            end=LEFT*2.5,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        ).next_to(rectDown,LEFT,buff=0)
        textFrameDown = Text("函数返回",font_size=18).next_to(arrowFrameDown,LEFT,buff=0.1)
        self.play(Create(rectUp))
        self.play(Create(arrowFrameUp))
        self.play(Write(textFrameUp))
        self.play(Create(rectDown))
        self.play(Create(arrowFrameDown))
        self.play(Write(textFrameDown))
        self.wait(2)
        self.clear()

        #动画八
        textMess = ["可以这么类比","调用函数就像是在钓鱼","rsp寄存器就像鱼钩，不断变化","rbp寄存器就像鱼竿，保持不变","带着这个想法去理解"]
        textMess_group = VGroup(*[Text(element,font_size=20)for element in textMess])
        for i, t in enumerate(textMess_group):
            self.play(Write(t))         
            self.wait(1.5)
            self.play(FadeOut(textMess_group[i]))
        self.wait(2) 
        
        #动画九
        textFunStart = Text("栈帧结构建立",font_size=20)
        frameStart = [
            "push rbp",
            "mov rbp,rsp"
        ]
        frameStart_group = VGroup(*[Text(ele,font_size=30)for ele in frameStart]).arrange(DOWN,buff=0.2)
        self.play(Write(textFunStart))
        self.wait(1)
        self.play(textFunStart.animate.shift(UP*3.3+LEFT*5.5))
        self.play(Write(frameStart_group))
        self.play(frameStart_group.animate.shift(UP*0.5+LEFT*5))

        lineFrameLeft = Line(start=UP*4,end=DOWN*4).shift(LEFT*2.5)
        lineFrameRight = lineFrameLeft.copy().shift(RIGHT*5)
        textHigherAdd = Text("栈底方向",font_size=15,color=GREEN).shift(UP*3+LEFT*3.5)
        textLowerAdd = Text("栈顶方向",font_size=15,color=RED).shift(DOWN*3+LEFT*3.5)
        self.play(Create(lineFrameLeft),Create(lineFrameRight))
        self.play(Write(textStack))
        self.play(Write(textHigherAdd),Write(textLowerAdd))
        self.wait(1)

        addRess = [
            "0x000000F0",
            "0x000000E8",
            "0x000000E0",
            "0x000000D8"
        ]
        addRess_group = VGroup(*[Text(ele,font_size=15)for ele in addRess]).arrange(DOWN,buff=1.8).next_to(lineFrameRight,RIGHT,buff=0.2)
        self.play(Create(addRess_group))

        rbp_arrow = Arrow(
            start=LEFT,
            end=LEFT*2.5,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip,
            color=GREEN
        ).next_to(addRess_group[0], RIGHT, buff=0.2)  
        text_rbp = Text("rbp", font_size=15).next_to(rbp_arrow, RIGHT, buff=0.1)
        rbp_group = VGroup(rbp_arrow,text_rbp)
        textRbpRight = Text("上一个函数栈帧基址",font_size=15).next_to(text_rbp,LEFT,buff=2.8)
        self.play(Create(rbp_arrow), Write(text_rbp))
        self.play(Write(textRbpRight))
        self.wait(1)
        self.play(FadeOut(textRbpRight),runtime=0.5)

        rsp_arrow = Arrow(
            start=LEFT,
            end=LEFT*2.5,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip,
            color=RED
        ).next_to(addRess_group[1], RIGHT, buff=0.2)
        text_rsp = Text("rsp", font_size=15).next_to(rsp_arrow, RIGHT, buff=0.1)
        textRspRight = Text("当前栈空间栈顶",font_size=15).next_to(text_rsp,LEFT,buff=2.8)
        self.play(Create(rsp_arrow), Write(text_rsp))
        self.play(Write(textRspRight))
        self.wait(1)
        self.play(FadeOut(textRspRight),runtime=0.5)

        dashLineBottom = DashedLine(
            start = lineFrameLeft.get_center(),
            end = lineFrameRight.get_center(),
            dash_length=0.12
        ).shift(UP*0.45)
        dashLineUp = dashLineBottom.copy().shift(UP*0.9)
        self.play(Create(dashLineBottom),Create(dashLineUp))
        dashLine_group = VGroup(dashLineBottom,dashLineUp)
        textRet = Text("function_1返回地址",font_size=15).next_to(dashLineUp,DOWN,buff=0.35)
        self.play(Write(textRet))
        self.wait(1)

        arrowRet = Arrow(
            start = UP*1,
            end = ORIGIN,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip
        ).next_to(dashLineUp,UP,buff=0.1)
        textCall = Text("返回地址是call指令自动压入\n               与栈帧无关",font_size=15).next_to(arrowRet,UP,buff=0.1)
        self.play(Create(arrowRet))
        self.play(Write(textCall))
        self.wait(2)
        rsp_text_group = VGroup(rsp_arrow,text_rsp)
        rsp_text_group_copy = rsp_text_group.copy().next_to(addRess_group[2],RIGHT,buff=0.1)
        dashLine_group_UP = dashLine_group.copy().shift(UP*2)
        textRbpRight.next_to(textRet,UP,buff=1.8)
        self.play(FadeOut(textCall,arrowRet))
        self.play(Create(dashLine_group_UP))
        self.play(Write(textRbpRight))
        self.wait(1.5)
        self.play(Transform(rsp_text_group,rsp_text_group_copy))
        self.wait(2)

        # 开始建立栈帧逻辑
        arrowPush = Arrow(
            start = UP*1,
            end = ORIGIN,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip
        ).next_to(frameStart_group[0],UP,buff=0.1)
        textPush = Text("开始建立栈帧",font_size=15).next_to(arrowPush,UP,buff=0.1)
        self.play(Create(arrowPush))
        self.play(Write(textPush))
        self.play(frameStart_group[0].animate.set_color(RED))
        self.wait(1.5)
        self.play(FadeOut(arrowPush,textPush))

        new_rsp_group = rsp_text_group.copy().next_to(addRess_group[3],RIGHT,buff=0.1)
        textRspDec = Text("rsp值先减少8个字节（64位环境）",font_size=15).shift(DOWN*1.5)
        new_dashLine_group = dashLine_group.copy().shift(DOWN*3.85)
        textRbpInput = Text("写入rbp的数据",font_size=15).shift(DOWN*1.5)
        textRbpAdd = Text("0x000000F0",font_size=15).next_to(textRet,DOWN,buff=3.8)
        arrowMov = Arrow(
            start = ORIGIN,
            end = UP*1,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip
        ).next_to(frameStart_group[1],DOWN,buff=0.1)
        textMov = Text("rbp指向新的栈帧基址",font_size=15).next_to(arrowMov,DOWN,buff=0.1)
        new_rbp_group = rbp_group.copy().next_to(addRess_group[3],RIGHT,buff=1.5)
        self.play(Write(textRspDec))
        self.wait(1)
        self.play(FadeOut(textRspDec))
        self.play(Transform(rsp_text_group,new_rsp_group))
        self.wait(1)
        self.play(Write(textRbpInput))
        self.wait(1)
        self.play(FadeOut(textRbpInput))
        self.play(Create(new_dashLine_group))
        self.play(Write(textRbpAdd))
        self.wait(1)
        self.play(frameStart_group[0].animate.set_color(WHITE))
        self.play(frameStart_group[1].animate.set_color(RED))
        self.play(Create(arrowMov),Write(textMov))
        self.wait(1)
        self.play(FadeOut(arrowMov,textMov))
        self.play(Transform(rbp_group,new_rbp_group))
        self.wait(2)
        
        #动画十
        textFunMov = Text("执行函数体时\nrsp寄存器值不断变化\nrbp寄存器的值保持不变",font_size=17).shift(DOWN*1.3)
        self.play(Write(textFunMov))
        self.wait(3)
        self.play(FadeOut(rsp_text_group,textFunMov))
        self.play(FadeOut(textFunStart,frameStart_group))

        textFrameOut = Text("函数返回",font_size=20).shift(UP*3.3+LEFT*5.5)
        frameOut = [
            "mov rsp,rbp",
            "pop rbp",
            "ret"
        ]
        frameOut_group = VGroup(*[Text(ele,font_size=30)for ele in frameOut]).arrange(DOWN,buff=0.2).shift(UP*0.5+LEFT*5)
        textReloc = Text("恢复栈顶到当前栈帧基址",font_size=15).shift(DOWN*1.3)
        textReFrame = Text("还原旧的栈帧",font_size=15).shift(DOWN*1.3)
        self.play(Write(textFrameOut))
        self.play(Create(frameOut_group))
        self.play(frameOut_group[0].animate.set_color(RED))
        self.play(Write(textReloc))
        self.wait(1)
        self.play(FadeOut(textReloc))
        self.play(Create(new_rsp_group))
        self.wait(1)
        self.play(frameOut_group[0].animate.set_color(WHITE))
        self.play(frameOut_group[1].animate.set_color(RED))
        self.wait(1)
        self.play(Write(textReFrame))
        self.wait(1)
        self.play(FadeOut(textReFrame))
        self.play(rbp_group.animate.next_to(addRess_group[0],RIGHT,buff=0.1))
        self.play(FadeOut(new_rsp_group))
        self.play(rsp_text_group.animate.next_to(addRess_group[2],RIGHT,buff=0.1))
        self.wait(1)

        self.play(frameOut_group[1].animate.set_color(WHITE))
        self.play(frameOut_group[2].animate.set_color(RED))
        textRetCall = Text("返回上一层",font_size=15).shift(DOWN*1.3)
        self.play(Write(textRetCall))
        self.wait(1)
        self.play(FadeOut(textRetCall))
        self.play(rsp_text_group.animate.next_to(addRess_group[1],RIGHT,buff=0.1))
        self.wait(1)

        textReFun = Text("栈帧完全恢复",font_size=15).shift(DOWN*1.3)
        self.play(Write(textReFun))
        self.wait(1)
        self.play(FadeOut(textReFun))
        self.play(frameOut_group[2].animate.set_color(WHITE))
        self.wait(3)
        self.clear()

        #动画十一
        textEnd = [
            "以上就是栈帧的工作原理",
            "每一层函数都是这样",
            "但在现代编译器中",
            "优化性能选项,会弱化栈帧结构",
            "比如说函数功能过于简单就不会生成独立的栈帧",
            "希望你能喜欢，下期视频再见👋"
        ]
        textEnd_group = VGroup(*[Text(ele,font_size=20)for ele in textEnd])
        for i,t in enumerate(textEnd_group):
            self.play(Write(t))         
            self.wait(1.5)
            self.play(FadeOut(textEnd_group[i]))

        textWasim = Text("Wasim",font_size=15,slant=ITALIC)
        self.play(Write(textWasim),runtime=2)
        self.wait(3)
        self.clear() 