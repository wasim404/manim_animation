from manim import *
from typing_extensions import runtime

class BinarySearch(Scene):
    def construct(self):
        # 播放动画一：视频开场
        self.animation_start()

        # 播放动画二：二分搜索引入
        self.binary_search_info()

        # 播放动画三：二分搜索时间复杂度计算
        self.binary_search_time_complexity()

        # 播放动画四：二分搜索找精确值
        self.binary_search_exact_value()

        # 播放动画五：upper_bound演示
        self.show_upper_bound()

        # 播放动画六：右边界演示
        self.show_right_bound()

        # 播放动画七：力扣34题解析
        self.show_leetcode_34()

    def animation_start(self):
        # 对象定义
        textInfo_1 = Text("二分搜索",font_size=20)
        headphone = SVGMobject(
            "binary_search/assets/headphone.svg"
        ).scale(0.1).next_to(textInfo_1, DOWN,buff=1.8)
        
        # 对象播放
        self.play(Write(textInfo_1),runtime = 2)
        self.wait(1)
        self.play(Write(headphone),runtime=2)
        self.wait(1)
        self.play(FadeOut(textInfo_1),FadeOut(headphone),runtime=1)

    def binary_search_info(self):
        # 对象定义

        # 用于演示二分搜索的有序数组,并转换为manim对象
        arr = [1,3,5,9,13,15]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5)

        # 播放升序数组
        self.play(Write(arr_text))
        self.wait(1)
        self.play(arr_text.animate.shift(UP*1.5))

        # 动画二的文字对象
        AnimationSecondInfo = [
            "有序数组中，如何高效查找目标元素？",
            "顺序遍历",
            "二分查找"
        ]

        AnimationSecondInfoText = VGroup(
            Text(AnimationSecondInfo[0], font_size=15, font="Hei", t2c={"查找": RED}),
            *[Text(ele, font_size=15, font="Hei") for ele in AnimationSecondInfo[1:]]
        )

        # 本代码所有箭头的模版
        ArrowTemplate = Arrow(
            start=ORIGIN,
            end=UP,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )

        # 左指针组对象，用于展示数组左边界
        ArrowLeft = ArrowTemplate.copy().next_to(arr_text[0],DOWN,buff=0.1)
        LeftTextInfo = Text("Left",font_size=15,font='Avenir').next_to(ArrowLeft,DOWN,buff=0.1)
        ArrowLeftGroup = VGroup(ArrowLeft,LeftTextInfo)

        # 右指针组对象，用于展示数组右边界
        ArrowRight = ArrowTemplate.copy().next_to(arr_text[5],DOWN,buff=0.1)
        RightTextInfo = Text("Right",font_size=15,font='Avenir').next_to(ArrowRight,DOWN,buff=0.1)
        ArrowRightGroup = VGroup(ArrowRight,RightTextInfo)

        # 中间指针组对象，用于展示数组中间位置
        ArrowMid = ArrowTemplate.copy().next_to(arr_text[2],DOWN,buff=0.1)
        MidTextInfo = Text("Mid",font_size=15,font='Avenir').next_to(ArrowMid,DOWN,buff=0.1)
        ArrowMidGroup = VGroup(ArrowMid,MidTextInfo)

        # 对象播放

        # AnimationSecondInfo[0]播放处理
        self.play(Write(AnimationSecondInfoText[0]),runtime=2)
        self.wait(1)
        self.play(FadeOut(AnimationSecondInfoText[0]))

        # AnimationSecondInfo[1]播放处理
        self.play(Write(AnimationSecondInfoText[1]),runtime=2)
        self.wait(1)

        # 顺序找播放
        self.play(arr_text[2].animate.set_color(GREEN))
        self.wait(1)
        for i in range(3):
            self.play(arr_text[i].animate.set_color(ORANGE))
            self.wait(1)
            self.play(arr_text[i].animate.set_color(WHITE))
        self.play(FadeOut(AnimationSecondInfoText[1]),runtime=1)
        self.wait(1)

        # 二分查找播放
        self.play(Write(AnimationSecondInfoText[2]),runtime=1)
        self.play(arr_text[2].animate.set_color(GREEN))
        self.play(Write(ArrowLeftGroup),runtime=1)
        self.play(Write(ArrowRightGroup),runtime=1)
        self.play(Write(ArrowMidGroup),runtime=1)
        self.wait(1)
        self.play(arr_text[2].animate.set_color(ORANGE))
        self.wait(1)
        self.clear()

    def binary_search_time_complexity(self):
        # 定义
        arr = [1,3,5,9,13,15]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5)
        self.play(Write(arr_text))
        self.play(arr_text.animate.shift(UP*2.3))
        LengthInfo = Text("长度",font_size=15).next_to(arr_text,RIGHT,buff=1.85).shift(UP*0.6)
        ArrLength = Text(str(len(arr)),font_size=15).next_to(arr_text,RIGHT,buff=2)

        ArrowTemplate = Arrow(
            start=ORIGIN,
            end=UP,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )

        # 左指针组对象，用于展示数组左边界
        ArrowLeft = ArrowTemplate.copy().next_to(arr_text[0],DOWN,buff=0.1)
        LeftTextInfo = Text("Left",font_size=15,font='Avenir').next_to(ArrowLeft,DOWN,buff=0.1)
        ArrowLeftGroup = VGroup(ArrowLeft,LeftTextInfo)

        # 右指针组对象，用于展示数组右边界
        ArrowRight = ArrowTemplate.copy().next_to(arr_text[5],DOWN,buff=0.1)
        RightTextInfo = Text("Right",font_size=15,font='Avenir').next_to(ArrowRight,DOWN,buff=0.1)
        ArrowRightGroup = VGroup(ArrowRight,RightTextInfo)

        # 中间指针组对象，用于展示数组中间位置
        ArrowMid = ArrowTemplate.copy().next_to(arr_text[3],DOWN,buff=0.1)
        MidTextInfo = Text("Mid",font_size=15,font='Avenir').next_to(ArrowMid,DOWN,buff=0.1)
        ArrowMidGroup = VGroup(ArrowMid,MidTextInfo)

        newarr = [1,3,5,9]
        newarr_text = VGroup(*[Text(str(ele),font_size=15)for ele in newarr]).arrange(RIGHT,buff=0.5).next_to(arr_text,DOWN,buff=1.35)
        newarr_length = Text(str(len(newarr)),font_size=15).next_to(newarr_text,RIGHT,buff=2).next_to(ArrLength,DOWN,buff=1.3)

        newarr_v2 = [1,3]
        newarr_v2_text = VGroup(*[Text(str(ele),font_size=15)for ele in newarr_v2]).arrange(RIGHT,buff=0.5).next_to(newarr_text,DOWN,buff=1.35)
        newarr_v2_length = Text(str(len(newarr_v2)),font_size=15).next_to(newarr_v2_text,RIGHT,buff=2).next_to(newarr_length,DOWN,buff=1.35)
        
        newarr_v3 = [3]
        newarr_v3_text = VGroup(*[Text(str(ele),font_size=15)for ele in newarr_v3]).arrange(RIGHT,buff=0.5).next_to(newarr_v2_text,DOWN,buff=1.35)
        newarr_v3_length = Text(str(len(newarr_v3)),font_size=15).next_to(newarr_v3_text,RIGHT,buff=2).next_to(newarr_v2_length,DOWN,buff=1.35)
        
        length_info = Text("含有n个元素的数组每次排除一半",font_size=15).next_to(newarr_text,LEFT,buff=1.5)
        eq1 = MathTex("\\frac{n}{2^k} = 1",font_size = 30).next_to(length_info,DOWN,buff=0.5)
        eq2 = MathTex("2^k = n",font_size = 30).next_to(length_info,DOWN,buff=0.5)
        eq3 = MathTex("k = \\log_2 n",font_size = 30).next_to(length_info,DOWN,buff=0.5)
        time_info = Text("二分搜索平均时间复杂度：O(logn)",font_size=15,t2c={"O(logn)":GREEN}).next_to(eq3,DOWN,buff=0.5)

        # 播放
        self.wait(1)
        self.play(Write(LengthInfo))
        self.play(Write(ArrLength),runtime=1)
        self.wait(1)

        self.play(Write(ArrowLeftGroup))
        self.play(Write(ArrowRightGroup))
        self.play(Write(ArrowMidGroup))
        self.wait(1)
        self.play(FadeOut(ArrowLeftGroup,ArrowRightGroup,ArrowMidGroup))
        self.play(TransformFromCopy(arr_text,newarr_text),runtime=2)
        self.play(Write(newarr_length),runtime=1)

        self.play(TransformFromCopy(newarr_text,newarr_v2_text),runtime=2)
        self.play(Write(newarr_v2_length),runtime=1)

        self.play(TransformFromCopy(newarr_v2_text,newarr_v3_text),runtime=2)
        self.play(Write(newarr_v3_length),runtime=1)

        self.play(Write(length_info),runtime=1)
        self.wait(1)
        self.play(Write(eq1),runtime=1)
        self.wait(2)
        self.play(Transform(eq1,eq2),runtime=2)
        self.wait(1)
        self.play(Transform(eq1,eq3),runtime=2)
        self.wait(2)

        self.play(Write(time_info),runtime=1)
        self.wait(2)
        self.clear()

    def binary_search_exact_value(self):
        # 定义
        AnimationForthInfo = [
            "二分搜索运用关键：有序数组（整体/局部）",
            "通过调整left和right，不断缩小结果区间"
        ]
        AnimationForthInfoText = VGroup(*[Text(ele,font_size=15)for ele in AnimationForthInfo]).arrange(DOWN,buff=0.5)

        standard_binary_search_code = Code(
            "binary_search/snippets/binsearch.py",
            language="python",
            tab_width=4,
            add_line_numbers=False,
            background_config={
                "buff": 0.5,
                "fill_color": "#00000000",   # 背景颜色（VSCode风格）
                "stroke_color": BLACK
            },
            paragraph_config={
                "font_size": 20,
                "line_spacing": 0.8,
            }
        ).shift(LEFT*2.9)

        ExactValueInfo = Text("二分查找精确值",font_size=20)
        arr = [1,3,5,9,13,15]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5).next_to(standard_binary_search_code.code_lines[1],RIGHT,buff=1.8)
        ArrowTemplate = Arrow(
            start=ORIGIN,
            end=UP,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )

        # 左指针组对象，用于展示数组左边界
        ArrowLeft = ArrowTemplate.copy().next_to(arr_text[0],DOWN,buff=0.1)
        LeftTextInfo = Text("Left",font_size=15,font='Avenir').next_to(ArrowLeft,DOWN,buff=0.1)
        ArrowLeftGroup = VGroup(ArrowLeft,LeftTextInfo)

        # 右指针组对象，用于展示数组右边界
        ArrowRight = ArrowTemplate.copy().next_to(arr_text[5],DOWN,buff=0.1)
        RightTextInfo = Text("Right",font_size=15,font='Avenir').next_to(ArrowRight,DOWN,buff=0.1)
        ArrowRightGroup = VGroup(ArrowRight,RightTextInfo)

        # 中间指针组对象，用于展示数组中间位置
        ArrowMid = ArrowTemplate.copy().next_to(arr_text[2],DOWN,buff=0.1)
        MidTextInfo = Text("Mid",font_size=15,font='Avenir').next_to(ArrowMid,DOWN,buff=0.1)
        ArrowMidGroup = VGroup(ArrowMid,MidTextInfo)
        
        # 目标指针组对象
        ArrowTarget = ArrowTemplate.copy().next_to(arr_text[1],DOWN,buff=0.1)
        TargetTextInfo = Text("Target",font_size=15,font='Avenir').next_to(ArrowTarget,DOWN,buff=0.1)
        ArrowTargetGroup = VGroup(ArrowTarget,TargetTextInfo)
        mid_code = Code(
            code_file="binary_search/snippets/mid_code.py",
            language="python",
            tab_width=4,
            add_line_numbers=False,
            background_config={
                "buff": 0.5,
                "fill_color": "#00000000",   # 背景颜色（VSCode风格）
                "stroke_color": BLACK
            },
            paragraph_config={
                "font_size": 20,
                "line_spacing": 0.8,
            }
        )
        mid_code.code_lines[0].move_to(standard_binary_search_code.code_lines[3])
        mid_code.code_lines[0].align_to(standard_binary_search_code.code_lines[3],LEFT)
        
        # 代码演示中的文字注释
        LoopInfo = Text("建立循环",font_size=15).next_to(standard_binary_search_code.code_lines[2],RIGHT,buff=1)
        # 播放

        # 文字内容播放，作为引入
        for i in range(0,2):
            self.play(Write(AnimationForthInfoText[i]),runtime=1)
            self.wait(1)
        self.play(FadeOut(AnimationForthInfoText[0],AnimationForthInfoText[1]),runtime=2)
        self.play(Write(ExactValueInfo))
        self.wait(1)
        self.play(ExactValueInfo.animate.shift(UP*2.9))
        # 播放代码演示
        self.play(Write(standard_binary_search_code.code_lines[0]))
        self.wait(1)
        self.play(Write(standard_binary_search_code.code_lines[1]))
        self.wait(1)

        self.play(Write(arr_text),runtime=1)
        self.play(Write(ArrowLeftGroup))
        self.play(Write(ArrowRightGroup))

        self.play(Write(standard_binary_search_code.code_lines[2]),runtime=1)
        self.play(Write(LoopInfo),runtime=1)
        self.wait(1)
        self.play(FadeOut(LoopInfo))

        self.play(Write(standard_binary_search_code.code_lines[3]),runtime=1)
        self.wait(1)
        self.play(Transform(standard_binary_search_code.code_lines[3],mid_code.code_lines[0]),runtime=1)
        self.wait(1)

        self.play(Write(ArrowMidGroup))
        self.play(Write(ArrowTargetGroup))
        self.wait(1)
        self.play(arr_text[2].animate.set_color(ORANGE))
        self.play(arr_text[1].animate.set_color(GREEN))

        self.play(Write(standard_binary_search_code.code_lines[4]),
                  Write(standard_binary_search_code.code_lines[5]),
                  Write(standard_binary_search_code.code_lines[6]),
                  Write(standard_binary_search_code.code_lines[7]),
                  Write(standard_binary_search_code.code_lines[8]),
                  Write(standard_binary_search_code.code_lines[9])
                ) 
        self.wait(2)

        # 展示右指针组对象移动，体现当mid大于target时候
        self.play(ArrowRightGroup.animate.next_to(ArrowTargetGroup,DOWN,buff=0.1))
        
        self.play(FadeOut(ArrowMidGroup))
        self.play(arr_text[2].animate.set_color(WHITE))
        self.play(arr_text[1].animate.set_color(WHITE))
        self.wait(2)

        # 第二轮循环
        self.play(Write(standard_binary_search_code.code_lines[2]),runtime=1)
        self.play(Write(standard_binary_search_code.code_lines[3]),runtime=1)
        ArrowMidGroup.next_to(ArrowLeftGroup,DOWN,buff=0.1)
        self.play(Write(ArrowMidGroup))
        self.wait(1)
        self.play(Write(standard_binary_search_code.code_lines[6]),runtime=1)
        self.play(FadeOut(ArrowLeftGroup))
        self.play(ArrowMidGroup.animate.next_to(arr_text[0],DOWN,buff=0.1))
        ArrowLeftGroup.next_to(ArrowRightGroup,DOWN,buff=0.1)
        self.play(Write(ArrowLeftGroup))
        self.wait(2)

        # 第三轮循环
        self.play(Write(standard_binary_search_code.code_lines[2]),runtime=1)
        self.play(Write(standard_binary_search_code.code_lines[3]),runtime=1)
        self.play(FadeOut(ArrowMidGroup))
        ArrowMidGroup.next_to(ArrowLeftGroup,DOWN,buff=0.1)
        self.play(Write(ArrowMidGroup))
        self.play(Write(standard_binary_search_code.code_lines[4]),runtime=1)
        self.play(arr_text[1].animate.set_color(GREEN))
        self.wait(2)
        self.clear()

    def show_upper_bound(self):
        # 定义
        AnimationFifthInfo = [
            "二分搜索不仅能查找精确值",
            "也能快速定位边界",
            "考虑一下这个问题",
            "如何快速查找第一个严格大于target的元素",
            "upper_bound返回了第一个严格大于target的元素的下标",
            "lower_bound返回了第一个大于等于target元素的下标"
        ]
        AnimationFifthInfoText = VGroup(*[Text(ele,font_size=20)for ele in AnimationFifthInfo])

        upper_bound_code = Code(
            code_file='binary_search/snippets/upper_bound.py',
            language="python",
            tab_width=4,
            add_line_numbers=False,
            background_config={
                "buff": 0.5,
                "fill_color": "#00000000",   # 背景颜色（VSCode风格）
                "stroke_color": BLACK
            },
            paragraph_config={
                "font_size": 20,
                "line_spacing": 0.8,
            }
            ).shift(LEFT*2.9)
        
        arr = [1,3,5,9,13,15]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5).next_to(upper_bound_code.code_lines[1],RIGHT,buff=1.8)
        ArrowTemplate = Arrow(
            start=ORIGIN,
            end=UP,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )

        # 左指针组对象，用于展示数组左边界
        ArrowLeft = ArrowTemplate.copy().next_to(arr_text[0],DOWN,buff=0.1)
        LeftTextInfo = Text("Left",font_size=15,font='Avenir').next_to(ArrowLeft,DOWN,buff=0.1)
        ArrowLeftGroup = VGroup(ArrowLeft,LeftTextInfo)

        # 右指针组对象，用于展示数组右边界
        ArrowRight = ArrowTemplate.copy().next_to(arr_text[5],DOWN,buff=0.1)
        RightTextInfo = Text("Right",font_size=15,font='Avenir').next_to(ArrowRight,DOWN,buff=0.1)
        ArrowRightGroup = VGroup(ArrowRight,RightTextInfo)

        # 中间指针组对象，用于展示数组中间位置
        ArrowMid = ArrowTemplate.copy().next_to(arr_text[2],DOWN,buff=0.1)
        MidTextInfo = Text("Mid",font_size=15,font='Avenir').next_to(ArrowMid,DOWN,buff=0.1)
        ArrowMidGroup = VGroup(ArrowMid,MidTextInfo)
        
        # 目标指针组对象
        ArrowTarget = ArrowTemplate.copy().next_to(arr_text[3],DOWN,buff=0.1)
        TargetTextInfo = Text("Target",font_size=15,font='Avenir').next_to(ArrowTarget,DOWN,buff=0.1)
        ArrowTargetGroup = VGroup(ArrowTarget,TargetTextInfo)

        upper_bound_title = Text("upper_bound",font_size=20)
        rect = SurroundingRectangle(upper_bound_code.code_lines[8],buff=0.1,color=WHITE)
        lower_bound_title = Text("lower_bound",font_size=20).shift(UP*2.9)
        lower_bound_code = Code(
            code_file="binary_search/snippets/lower_bound_code.py",
            language="python",
            tab_width=4,
            add_line_numbers=False,
            background_config={
                "buff": 0.5,
                "fill_color": "#00000000",   # 背景颜色（VSCode风格）
                "stroke_color": BLACK
            },
            paragraph_config={
                "font_size": 20,
                "line_spacing": 0.8,
            }
        )
        lower_bound_code.code_lines[0].move_to(upper_bound_code.code_lines[4])
        lower_bound_code.code_lines[0].align_to(upper_bound_code.code_lines[4],LEFT)
        AnimationFifthInfoText[4].next_to(upper_bound_code.code_lines[8],RIGHT,buff=2)
        AnimationFifthInfoText[5].next_to(upper_bound_code.code_lines[8],RIGHT,buff=2)
        # 播放
        for i in range(0,3):
            self.play(Write(AnimationFifthInfoText[i]))
            self.wait(1)
            self.play(FadeOut(AnimationFifthInfoText[i]))
        self.play(Write(AnimationFifthInfoText[3]))
        self.wait(2)
        self.play(FadeOut(AnimationFifthInfoText[3]))
        # upper_bound
        self.play(Write(upper_bound_title))
        self.wait(1)
        self.play(upper_bound_title.animate.shift(UP*2.9))
        self.play(Write(upper_bound_code.code_lines[0]))
        self.play(Write(upper_bound_code.code_lines[1]))
        self.play(Write(arr_text))
        self.play(Write(ArrowLeftGroup),Write(ArrowRightGroup))
        for i in range(2,9):
            self.play(Write(upper_bound_code.code_lines[i]))
        self.wait(1)
        self.play(Write(ArrowMidGroup))
        self.play(Write(ArrowTargetGroup))
        self.play(ArrowLeftGroup.animate.next_to(ArrowTargetGroup,DOWN,buff=0.1))
        self.wait(2)

        self.play(FadeOut(ArrowMidGroup))
        self.wait(1)
        self.play(Write(upper_bound_code.code_lines[2]))
        ArrowMidGroup.next_to(arr_text[4],DOWN,buff=0.1)
        self.play(Write(ArrowMidGroup))
        self.wait(1)
        self.play(ArrowRightGroup.animate.next_to(ArrowLeftGroup,DOWN,buff=0.1))
        self.wait(2)

        self.play(FadeOut(ArrowMidGroup))
        self.play(Write(upper_bound_code.code_lines[2]))
        ArrowMidGroup.next_to(ArrowRightGroup,DOWN,buff=0.1)
        self.play(Write(ArrowMidGroup))
        self.play(ArrowLeftGroup.animate.next_to(arr_text[4],DOWN,buff=0.1))

        self.play(Write(rect))
        self.play(arr_text[4].animate.set_color(GREEN))
        self.wait(2)
        self.play(FadeOut(ArrowTargetGroup,ArrowLeftGroup,ArrowRightGroup,ArrowMidGroup,rect))
        self.play(Write(AnimationFifthInfoText[4]))
        self.wait(1)
        self.play(FadeOut(AnimationFifthInfoText[4]))
        self.play(arr_text[4].animate.set_color(WHITE))
        self.play(Transform(upper_bound_title,lower_bound_title))
        self.wait(1)
        self.play(Transform(upper_bound_code.code_lines[4],lower_bound_code.code_lines[0]))
        self.wait(1)
        self.play(Write(AnimationFifthInfoText[5]))
        self.wait(1)
        self.play(FadeOut(AnimationFifthInfoText[5]))
        self.clear()

    def show_right_bound(self):
        # 定义
        AnimationSixthInfo = [
            "考虑这个问题",
            "如何快速找到数组中最后一个严格小于target的元素",
            "upper_bound",
            "lower_bound",
            "lower_bound返回值就是第一个大于等于target元素的下标",
            "那么前一位元素必然就是严格小于target的元素",
            "不要忘了，二分运用的前提是数组有序排列！" ,
            "同理，upper_bound返回值的前一个元素就是第一个小于等于target的元素"
        ]

        AnimationSixthInfoText = VGroup(*[Text(ele,font_size=20)for ele in AnimationSixthInfo])
        AnimationSixthInfoText[3].shift(LEFT*3).shift(UP*2)
        
        arr = [1,3,5,9,13,15]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5).next_to(AnimationSixthInfoText[3],RIGHT,buff=2)

        ArrowTemplate = Arrow(
            start=ORIGIN,
            end=UP,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )
        # 目标指针组对象
        ArrowTarget = ArrowTemplate.copy().next_to(arr_text[3],DOWN,buff=0.1)
        TargetTextInfo = Text("Target",font_size=15,font='Avenir').next_to(ArrowTarget,DOWN,buff=0.1)
        ArrowTargetGroup = VGroup(ArrowTarget,TargetTextInfo)

        ReturnTextInfo = Text("return",font_size=15,font='Avenir').move_to(TargetTextInfo)
        # 播放
        for i in range(0,2):
            self.play(Write(AnimationSixthInfoText[i]))
            self.wait(2)
            if i==0:
                self.play(FadeOut(AnimationSixthInfoText[i]))
        self.play(AnimationSixthInfoText[1].animate.shift(UP*2.9))
        self.play(Write(AnimationSixthInfoText[3]))
        self.play(Write(arr_text))
        self.play(Write(ArrowTargetGroup))
        self.wait(1)
        self.play(Transform(TargetTextInfo,ReturnTextInfo))
        self.wait(1)
        for i in range(4,8):
            self.play(Write(AnimationSixthInfoText[i]))
            self.wait(2)
            self.play(FadeOut(AnimationSixthInfoText[i]))
        self.clear()

    def show_leetcode_34(self):
        # 定义

        LeetCode34Img = ImageMobject("binary_search/assets/leetcode_34.png").scale(0.7)
        AnimationSeventhInfo = [
            "解决一下力扣编号34题",
            "Target=8",
            "先找到第一个大于等于target的元素",
            "再找到最后一个小于等于target的元素",
            "lower_bound(target)",
            "lower_bound(target+1)-1",
            "当所有元素均小于target时，返回下标表示插入位置（越界），要单独判断"
        ]
        AnimationSeventhInfoText = VGroup(*[Text(ele,font_size=20)for ele in AnimationSeventhInfo])
        
        arr = [5,7,7,8,8,10]
        arr_text = VGroup(*[Text(str(ele),font_size=15) for ele in arr]).arrange(RIGHT,buff=0.5)
        AnimationSeventhInfoText[1].next_to(arr_text,RIGHT,buff=1)
        AnimationSeventhInfoText[2].next_to(arr_text,DOWN,buff=0.7)
        AnimationSeventhInfoText[3].next_to(AnimationSeventhInfoText[2],DOWN,buff=0.7)
        AnimationSeventhInfoText[4].move_to(AnimationSeventhInfoText[2])
        AnimationSeventhInfoText[5].move_to(AnimationSeventhInfoText[3])
        Leetcode34Code = Code(
            code_file="binary_search/snippets/leetcode34.py",
            language="python",
            tab_width=4,
            add_line_numbers=False,
            background_config={
                "buff": 0.5,
                "fill_color": "#00000000",   # 背景颜色（VSCode风格）
                "stroke_color": BLACK
            },
            paragraph_config={
                "font_size": 20,
                "line_spacing": 0.8,
            }
        ).scale(0.85).shift(LEFT*2)
        AnimationSeventhInfoText[6].next_to(Leetcode34Code.code_lines[14],RIGHT,buff=0.8)
        # 播放
        self.play(Write(AnimationSeventhInfoText[0]))
        self.wait(1)
        self.play(FadeOut(AnimationSeventhInfoText[0]))
        self.play(FadeIn(LeetCode34Img))
        self.wait(3)
        self.play(FadeOut(LeetCode34Img))
        self.play(Write(arr_text))
        self.play(Write(AnimationSeventhInfoText[1]))
        for i in range(2,4):
            self.play(Write(AnimationSeventhInfoText[i]))
            self.wait(2)
        self.play(Transform(AnimationSeventhInfoText[2],AnimationSeventhInfoText[4]))
        self.wait(1)
        self.play(Transform(AnimationSeventhInfoText[3],AnimationSeventhInfoText[5]))
        self.wait(1)
        self.clear()
        self.play(Write(Leetcode34Code))
        self.wait(1)
        self.play(Write(AnimationSeventhInfoText[6]))
        self.wait(2)
        self.play(FadeOut(Leetcode34Code,AnimationSeventhInfoText[6]))

        textWasim = Text("Wasim",font_size=15,slant=ITALIC,font='Didot')
        self.play(Write(textWasim),runtime=2)
        self.wait(2)
        self.clear() 