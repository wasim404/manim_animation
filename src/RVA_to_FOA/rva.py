from manim import *
from typing_extensions import runtime
class Rva(Scene):
    def construct(self):
        textInfo_1 = Text("RVA和FOA的转换",font_size=20)
        textInfo_2 = Text("戴上耳机，一起静心领悟",font_size=15,slant=ITALIC).shift(DOWN*2)
        self.play(Write(textInfo_1),runtime=1.5)
        self.play(Write(textInfo_2),runtime=1.5)
        self.wait(1)
        self.play(FadeOut(textInfo_1),FadeOut(textInfo_2),runtime=0.5)
        
        # 动画一
        textDif = Text("同一个程序，在磁盘和内存中，是以两种完全不同的方式存在的",font_size=20)
        LineMid = Line(start=UP*3,end=DOWN*3)
        textSsd = Text("磁盘(未运行)",font_size=15).next_to(LineMid,LEFT,buff=3).shift(UP*2.3)
        LineSsdBase = Line(start=LEFT,end=ORIGIN).set_length(3).next_to(textSsd,DOWN,buff=0.3)
        textFilehead = Text("文件头",font_size=15).next_to(LineSsdBase,RIGHT,buff=0.3)
        textFileheadAddress = Text("0x00000000",font_size=15).next_to(LineSsdBase,LEFT,buff=0.3)
        arrowoffset = Arrow(
            start=UP*3,
            end=ORIGIN,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        ).next_to(LineSsdBase,DOWN,buff=0.3)
        textOffset = Text("FOA(例如32个字节)",font_size=15).next_to(arrowoffset,RIGHT,buff=0.3)
        lineSsdexe = Line(start=LEFT,end=ORIGIN).set_length(3).next_to(arrowoffset,DOWN,buff=0.3)
        textExe = Text("某段数据",font_size=15).next_to(lineSsdexe,RIGHT,buff=0.3)
        textExeAddress = Text("0x00000020",font_size=15).next_to(lineSsdexe,LEFT,buff=0.3)
        textFOA = Text("FOA:文件偏移地址",font_size=15).next_to(lineSsdexe,DOWN,buff=0.3)
        
        textRam = Text("内存(运行时)",font_size=15).next_to(textSsd,RIGHT,buff=6)
        LineImageBase = Line(start=LEFT,end=ORIGIN).set_length(3).next_to(textRam,DOWN,buff=0.3)
        textImage = Text("ImageBase",font_size=15).next_to(LineImageBase,RIGHT,buff=0.3)
        textImageAddress = Text("0x00400000",font_size=15).next_to(LineImageBase,LEFT,buff=0.3)
        arrowRvaOffset = Arrow(
            start=UP*3,
            end=ORIGIN,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        ).next_to(LineImageBase,DOWN,buff=0.3)
        textRvaOffset = Text("RVA(例如32个字节)",font_size=15).next_to(arrowRvaOffset,RIGHT,buff=0.3)
        lineRvaexe = Line(start=LEFT,end=ORIGIN).set_length(3).next_to(arrowRvaOffset,DOWN,buff=0.3)
        textRvaExe = Text("某段数据",font_size=15).next_to(lineRvaexe,RIGHT,buff=0.3)
        textRvaExeAddress = Text("0x00400020",font_size=15).next_to(lineRvaexe,LEFT,buff=0.3)
        textRva = Text("RVA:相对虚拟地址",font_size=15).next_to(lineRvaexe,DOWN,buff=0.3)
        self.play(Write(textDif),runtime=3)
        self.wait(1)
        self.play(textDif.animate.shift(UP*3.3))
        self.play(Create(LineMid),runtime=1)
        self.play(Write(textSsd),runtime=1)
        self.play(Create(LineSsdBase),runtime=1)
        self.play(Write(textFilehead),Write(textFileheadAddress),runtime=1)
        self.wait(1)
        self.play(Create(arrowoffset),runtime=1)
        self.play(Write(textOffset),runtime=1)
        self.play(Create(lineSsdexe),runtime=1)
        self.play(Write(textExe),Write(textExeAddress),runtime=1)
        self.play(Write(textFOA))
        self.wait(1)

        self.play(Write(textRam),runtime=1)
        self.play(Create(LineImageBase),runtime=1)
        self.play(Write(textImage),runtime=1)
        self.play(Write(textImageAddress),runtime=1)
        self.wait(1)
        self.play(Create(arrowRvaOffset),runtime=1)
        self.play(Write(textRvaOffset),runtime=1)
        self.play(Create(lineRvaexe),runtime=1)
        self.play(Write(textRvaExeAddress),Write(textRvaExe),runtime=1)
        self.wait(1)
        self.play(Write(textRva),runtime=1)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # 动画二
        textChange = Text("RVA和FOA相互转换的方法",font_size=15)
        textOffsetSame = Text("偏移量相同",font_size=15).shift(DOWN*2.5)
        textAdd = Text("程序按节区存储",font_size=15)
        textChangeFun = Text("FOA=(RVA-该段数据所在节区虚拟地址)+节区在文件中偏移量",font_size=15)

        self.play(Write(textChange))
        self.wait(1)
        self.play(textChange.animate.shift(UP * 3))
        self.play(
            Write(textSsd),
            Create(LineSsdBase),
            Write(textFilehead),
            Write(textFileheadAddress),
            Create(arrowoffset),
            Write(textOffset),
            Create(lineSsdexe),
            Write(textExe),
            Write(textExeAddress),
            run_time=5
        )

        self.play(
            Write(textRam),
            Create(LineImageBase),
            Write(textImage),
            Write(textImageAddress),
            Create(arrowRvaOffset),
            Write(textRvaOffset),
            Create(lineRvaexe),
            Write(textRvaExeAddress),
            Write(textRvaExe),
            runtime=5
        )
        self.wait(1)
        self.play(textOffset.animate.set_color(RED))
        self.play(textRvaOffset.animate.set_color(RED))
        self.play(Write(textOffsetSame),runtime=1)
        self.wait(1)
        ssd_group = Group(
    textSsd, LineSsdBase,
    textFilehead, textFileheadAddress,
    arrowoffset, textOffset,
    lineSsdexe, textExe, textExeAddress
)

        ram_group = Group(
    textRam, LineImageBase,
    textImage, textImageAddress,
    arrowRvaOffset, textRvaOffset,
    lineRvaexe, textRvaExeAddress, textRvaExe
)

        self.wait(1)

        self.play(
    FadeOut(ssd_group),
    FadeOut(ram_group),
    run_time=2
)
        self.play(textOffsetSame.animate.shift(UP*4.5))
        self.play(Write(textAdd),runtime=1)
        self.wait(1)
        self.play(FadeOut(textAdd))
        self.play(Write(textChangeFun),runtime=1)
        self.wait(1)
        self.play(FadeOut(textChangeFun,textOffsetSame,textChange))


        # 动画三
        LineNewImageBase = Line(start=LEFT*2,end=RIGHT*2).shift(UP*2)
        textNewImageBase = Text("ImageBase",font_size=15).next_to(LineNewImageBase,RIGHT,buff=0.3)
        textImageAddress.next_to(LineNewImageBase,LEFT,buff=0.3)
        LineSomeAdd = Line(start=LEFT*2,end=RIGHT*2).next_to(LineNewImageBase,DOWN,buff=1.3)
        textSomeAdd = Text("某节区",font_size=15).next_to(LineSomeAdd,RIGHT,buff=0.3)
        textSomeAddress = Text("0x0044F000",font_size=15).next_to(LineSomeAdd,LEFT,buff=0.3)
        arrowNewOffset = Arrow(
            start=UP*3,
            end=ORIGIN,
            stroke_width=3,
            tip_length = 0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        ).next_to(LineNewImageBase,DOWN,buff=0.2)
        LineNewExe = Line(start=LEFT*2,end=RIGHT*2).next_to(arrowNewOffset,DOWN,buff=0.1)
        textNewExe = Text("某段数据",font_size=15).next_to(LineNewExe,RIGHT,buff=0.3)
        textRvaTest = Text("RVA=0x00546578",font_size=15).next_to(LineNewExe,UP,buff=0.7).shift(RIGHT*1)
        textSub = Text("-",font_size=15).next_to(textRvaTest,RIGHT,buff=0.1)
        textSomeAddress_copy = textSomeAddress.copy()
        # 短箭头：从某节区(LineSomeAdd)到某段数据(LineNewExe)
        arrow_sec_to_data = Arrow(
            start=UP*0.9,
            end=DOWN*1,
            stroke_width=3,
            tip_length=0.1,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.1
        )
        textSubAddress = Text("0x000F7578",font_size=15).next_to(arrow_sec_to_data,RIGHT,buff=0.3)
        textFilehead.next_to(LineNewImageBase,RIGHT,buff=0.3)
        textFileheadAddress.next_to(LineNewImageBase,LEFT,buff=0.3)
        textDisPos = Text("节区在磁盘中起始地址",font_size=15).next_to(LineSomeAdd,RIGHT,buff=0.3)
        textDisPosAdd = Text("0x0044DE00",font_size=15).next_to(LineSomeAdd,LEFT,buff=0.3)
        textPlus = Text("+",font_size=15).next_to(textSubAddress,RIGHT,buff=0.1)
        textDisPosAdd_copy = textDisPosAdd.copy()
        textResAddress = Text("0x00545378",font_size=15).next_to(LineNewExe,LEFT,buff=0.3)
        
        self.play(Create(LineNewImageBase),Write(textNewImageBase),Write(textImageAddress))
        self.play(Create(LineSomeAdd),Write(textSomeAdd),Write(textSomeAddress))
        self.wait(1)
        self.play(Create(LineNewExe),Write(textNewExe))
        self.play(Create(arrowNewOffset))
        self.play(arrowNewOffset.animate.set_color(RED))
        self.play(Write(textRvaTest))
        self.wait(1)
        self.play(arrowNewOffset.animate.set_color(WHITE))
        self.play(Write(textSub),textSomeAddress_copy.animate.next_to(textSub))
        self.play(FadeOut(textRvaTest,textSub,textSomeAddress_copy))
        self.play(ReplacementTransform(arrowNewOffset, arrow_sec_to_data))
        self.play(Write(textSubAddress),arrow_sec_to_data.animate.set_color(RED))
        self.play(FadeOut(textNewImageBase,textSomeAddress,textSomeAddress,textSomeAdd,textImageAddress))
        self.play(Write(textFilehead),Write(textFileheadAddress))
        self.play(Write(textDisPos),Write(textDisPosAdd),runtime=1)
        self.play(Write(textPlus),textDisPosAdd_copy.animate.next_to(textPlus,RIGHT,buff=0.1),runtime=1)
        self.play(FadeOut(textSubAddress,textPlus,textDisPosAdd_copy))
        self.play(Write(textResAddress))
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # 动画四
        textFunction = Text("FOA = (RVA - Section[i].VirtualAddress) + Section[i].PointerToRawData",font_size=15)
        self.play(Write(textFunction),runtime=1)
        self.wait(1)
        self.play(*[FadeOut(m) for m in self.mobjects])
        textWasim = Text("Wasim",font_size=15,slant=ITALIC)
        self.play(Write(textWasim),runtime=2)
        self.wait(3)
        self.clear()