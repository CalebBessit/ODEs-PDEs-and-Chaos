'''
Source code for Manim animation video explaining Lienard systems.

Author: Caleb Bessit
Date  : 04 September 2023
'''

from tkinter import LEFT
from manim import *
import numpy as np
import math

class LienardSystems(Scene):
    def construct(self):

        '''
        ************************************
                  DATA AND OBJECTS
        ************************************
        '''
        


        tex =[
                Tex(r"Li\'enard Systems", font_size=60),
                Tex(r'An intuitive explanation', font_size=25).shift(DOWN*0.5),
                Tex(r'Consider a system of the form', font_size=30).shift(3.5*UP),
                Tex(r' $\Ddot{x} + f(x) \Dot{x} + g(x) = 0$', font_size=35, color=BLUE).shift(2.75*UP),
                Tex(r'Assuming:', font_size=30),
                Tex(r'(1) $f(x) \text{ and } g(x)$ are continuously differentiable for all $x$;', font_size=30).shift(2*UP + 0.5*LEFT),
                Tex(r'(2) $g(-x)=-g(x)$ for all $x$ (i.e., $g(x)$ is an odd function);', font_size=30).shift(1.5*UP),
                Tex(r'(3) $g(x)>0$ for $x>0$;', font_size=30).shift(UP),
                Tex(r'(4) $f(-x)=f(x)$ for all $x$ (i.e., $f(x)$ is an even function);', font_size=30).shift(0.5*UP),
                Tex(r'(5) The odd function $F(x)= \int_{0}^x f(u)du$ has exactly one positive zero at $x=a$, is negative for $0<x<a$, is positive and non-decreasing for $x>a$, and $F(x) \longrightarrow \infty$ and $x \longrightarrow \infty$.', font_size=30).shift(0.5*DOWN),
                Tex(r'then the system has a unique, stable limit cycle surrounding the origin in the phase plane.', font_size=30, color=RED).shift(2*DOWN),
                Tex(r'Why do these assumptions make sense?', font_size=30, color=TEAL).shift(3.2*DOWN),
                Tex(r"Let's construct an $F(x)$ that satisfies this.", font_size=30, color=GOLD).shift(2*UP+0.5*RIGHT),
                Tex(r"For concreteness, let's take, say, $F(x)=x^3-x:$ ", font_size=30).to_edge(UP).shift(0.25*UP),
                Tex(r"Then $f(x) = F'(x) = 3x^2-1.$ ", font_size=30).to_edge(DOWN).shift(0.2*DOWN),
                Tex(r"What we'll do now is imagine the equation describing the motion of a particle on the line.", font_size=30).shift(2.5*UP),
                Tex(r' $\Ddot{x} + f(x) \Dot{x} + g(x) = 0$', font_size=35, color=BLUE),
                Tex(r'Now, if we ignore $g(x)$...', font_size=30).shift(UP),
                Tex(r"Let's consider the signs of $\Ddot{x}$ in these three regions while moving to the right:", font_size=30).to_edge(UP),
                Tex(r'This looks like...', font_size=30).shift(UP),
                Tex(r"But then could we not just end up staying here?", font_size=30).shift(UP),
                Tex(r'If we ignore $f(x)$...', font_size=30).shift(UP),
                Tex(r"For simplicity, let's take, say, $g(x)=x$.", font_size=30).shift(UP),
                Tex(r'Combining the effect of these two we get', font_size=30).shift(UP),
                Tex(r'Now imagine if we jump off the line...', font_size=30).shift(3*UP),
                Tex(r'...and into two-dimensional space', font_size=30).shift(DOWN),
                Tex(r'We get something like the Van der Pol Oscillator!', font_size=30, color=ORANGE).shift(UP),
                MathTex(
                    r"\text{(5) The odd function } F(x) = \int_{0}^x f(u) \, du \text{ has }",
                    r"{}\text{exactly one positive zero at } x = a,\\",
                    font_size=30
                ).to_edge(UP).shift(0.25*UP),
                MathTex(
                    r"{}\text{is negative for } 0 < x < a,",
                    r"{}\text{ is positive and non-decreasing for } x > a,",
                    r"{}\text{ and }",
                    r"F(x) \longrightarrow \infty \text{ as } x \longrightarrow \infty.",
                    font_size=30).to_edge(DOWN),
                Tex(r'$\Ddot{x}=-f(x) \dot{x}$', font_size=30, color=BLUE),
                Tex(r'with $f(x)=3x^2-1$', font_size=30, color=ORANGE).shift(0.5*DOWN),
                Tex(r"$\Ddot{x}= - (3x^2-1) \Dot{x}$", font_size=35, color=ORANGE).shift(2.5*UP),
                Tex(r"Let's see how this affects our particle on the line.", font_size=30).shift(3*UP),
                Tex(r'Similarly, when moving to the left...', font_size=30).shift(3*DOWN),
                Tex(r"But now there's a problem!", font_size=30).shift(3*UP),
                Tex(r"In this region for example, we're slowed down when moving to the right...", font_size=30).shift(2*UP),
                Tex(r"...but also slowed down when moving to the left.", font_size=30, color=RED_C).shift(2*DOWN),
                Tex(r"So can our particle even oscillate at all?", font_size=30, color=GOLD).shift(3*DOWN),
                Tex(r"Yes! This is due to the $g(x)$ we've been ignoring!", font_size=30, color=GREEN).shift(2.5*UP),
                Tex(r"Now, performing the same sign analysis on $\Ddot{x}$ as we did with $f(x)$...", font_size=30).shift(2.5*UP),
                Tex(r"$g(x)=x$", font_size=40, color=ORANGE).shift(3*UP),
                Tex(r"For our particle this means:", font_size=30).shift(2.5*UP),
                Tex(r"Finally, let's put everything together.",font_size=35),
                Tex(r"Thank you for watching!",font_size=40).shift(0.5*UP),
                Tex(r"made by Caleb Bessit",font_size=25, color=TEAL),
                ]
        
        rects = [
                    SurroundingRectangle(tex[9], buff = .1),
                    SurroundingRectangle(tex[27][1], buff = .1),
                    SurroundingRectangle(tex[28][0], buff = .1),
                    SurroundingRectangle(tex[28][1], buff = .1),
                    SurroundingRectangle(tex[28][3], buff = .1),
                ]   
        
        xmin, xmax, ymin, ymax, step = -7, 7, -5, 5, 0.4
        length = xmax-xmin
        unitShift = length/4.5
        extend     = 3
        axes = [
                    Axes(x_range=(-1, 5), 
                         y_range=(-5,5), 
                         y_axis_config={"tip_width":0.2, "tip_height":0.2, "length":1} ,#For initial frame
                         axis_config={'tip_shape': StealthTip}
                         ), 
                    
                    Axes(x_range=(-3,3), 
                         y_range=(-5,5),
                         axis_config={'tip_shape': StealthTip}
                        ),

                    NumberLine(x_range=(xmin, xmax),
                          include_tip=True,
                          numbers_with_elongated_ticks=[0],
                          label_direction=0.3*DR,
                          tip_shape= StealthTip
                          ),

                    NumberLine(x_range=(-1, xmax),
                          include_tip=True,
                          numbers_with_elongated_ticks=[0],
                          tip_shape= StealthTip
                          ),
                    NumberLine(x_range=(xmin, xmax),
                          include_tip=True,
                          numbers_with_elongated_ticks=[0],
                          label_direction=0.3*DR,
                          tip_shape= StealthTip
                          ),

                    NumberLine(x_range=(xmin, xmax),
                          include_tip=True,
                          numbers_with_elongated_ticks=[0],
                          tip_shape= StealthTip
                          ),

               ]
        
        m = np.sqrt(1/3)
        dots = [
                    Dot(point=LEFT, color=RED) ,                            #Initial point a
                    Dot(point=2*RIGHT, color=RED),                          #Point a on plot of F(x)
                    Dot(point=2*LEFT, color=RED),                           #Point -a
                    Dot(point=2*m*RIGHT, color=PURPLE),                     #Point b
                    Dot(point=2*m*LEFT, color=PURPLE),                      #Point -b           
                    Dot(UP, radius=0.15, color=RED).move_to(UP+7*LEFT, aligned_edge=LEFT),
                    DoubleArrow(tip_shape_end=ArrowCircleFilledTip, color=PURE_RED, buff=0.5).shift(5*LEFT+DOWN),
                    DoubleArrow(tip_shape_start=ArrowCircleFilledTip, color=PURE_GREEN, buff=0.5).shift(DOWN),
                    DoubleArrow(tip_shape_end=ArrowCircleFilledTip, color=PURE_RED, buff=0.5).shift(5*RIGHT+DOWN),
                    Dot(UP+3*LEFT, radius=0.15, color=RED),
                    Dot(UP+3*RIGHT, radius=0.15, color=RED),
                    Dot(UP, radius=0.15, color=RED).move_to(UP+7*RIGHT, aligned_edge=RIGHT),  #Bottom moving to right stuff
                    Dot(DOWN, radius=0.15, color=BLUE).move_to(DOWN+7*RIGHT, aligned_edge=RIGHT),
                    Dot(DOWN+3*RIGHT, radius=0.15, color=BLUE),
                    Dot(DOWN+3*LEFT, radius=0.15, color=BLUE),
                    Dot(DOWN, radius=0.15, color=BLUE).move_to(DOWN+7*LEFT, aligned_edge=LEFT),
                    Dot(UP+2.5*LEFT, radius=0.15, color=TEAL),
                    Dot(UP+2.5*RIGHT, radius=0.15, color=TEAL),
                    DoubleArrow(tip_shape_end=ArrowCircleFilledTip, color=PURE_RED, buff=0.5).shift(DOWN),
                    DoubleArrow(tip_shape_start=ArrowCircleFilledTip, color=PURE_RED, buff=0.5).shift(DOWN),
                    Dot(UP+2.5*LEFT, radius=0.15, color=TEAL),
                    DoubleArrow(tip_shape_start=ArrowCircleFilledTip, color=PINK, buff=0.5).shift(3.5*LEFT+ DOWN),
                    DoubleArrow(tip_shape_end=ArrowCircleFilledTip, color=PINK, buff=0.5).shift(3.5*RIGHT+DOWN),
                    Dot(UP+6*LEFT, radius=0.15, color=PURPLE),
                    Dot(UP, radius=0.15, color=PURPLE),
                    Dot(UP+6*RIGHT, radius=0.15, color=PURPLE),
                    Dot(UP, radius=0.15, color=PURPLE),
                    Dot(UP+6*LEFT, radius=0.15, color=PURPLE),
                    Dot(UP+6*LEFT, radius=0.15, color=TEAL),
                ]
        dLabels =[
                    Tex(r'$a$', font_size=30).next_to(dots[0], 0.1*DR),     #Initial a           
                    Tex(r'$a$', font_size=30).next_to(dots[1], 0.1*DR),     #Label for point a on plot of F(x)
                    Tex(r'$-a$', font_size=30).next_to(dots[2], 0.1*UL),    #Label for-a
                    Tex(r'$b$', font_size=30).next_to(dots[3], 0.1*UL),     #Label for b
                    Tex(r'$-b$', font_size=30).next_to(dots[4], 0.1*DL),     #Label for -b 
                    Tex(r'$\ddot{x}$', font_size=50, color= PURE_RED).next_to(dots[6], 0.1*DOWN),
                    Tex(r'$\ddot{x}$', font_size=50, color= PURE_GREEN).next_to(dots[7], 0.1*DOWN),
                    Tex(r'$\ddot{x}$', font_size=50, color= PURE_RED).next_to(dots[8], 0.1*DOWN),
                    Tex(r'$\ddot{x}$', font_size=50, color= PURE_RED).next_to(dots[18], 0.1*DOWN),
                    Tex(r'$\ddot{x}$', font_size=50, color= PINK).next_to(dots[21], 0.1*DOWN),
                    Tex(r'$\ddot{x}$', font_size=50, color= PINK).next_to(dots[22], 0.1*DOWN),
               ]
        
        funcs =[
                    lambda x:x*(x-1.5)*(x+1.5), #For idea of F(x)
                    lambda x: x*(x-1)*(x+1),    #For actual F(x)
                    lambda x:3*x**2-1   ,        #For f(x)
                    lambda pos: (pos[1])*RIGHT + (  mu*(math.pow(pos[0],2) -1 )*pos[1] -pos[0]  )*UP
               ]
        
        curves=[
                    axes[0].plot(funcs[0], x_range=(0,1.5,0.01),color=TEAL),  #Initial F(x)
                    axes[0].plot(funcs[0], x_range=(0,1.6,0.01),color=TEAL),  #F(x), with negative
                    axes[0].plot(funcs[0], x_range=(0,2.1,0.01),color=TEAL),  #F(x), exten
                    axes[1].plot(funcs[1], x_range=(-1.75,1.75,0.01), color= TEAL), #Actual F(X)
                    axes[1].plot(funcs[2], x_range=(-1.3,1.3,0.01), color= ORANGE)  #Actual f(x)
               ]
        
        cLabels =[
                    Tex(r'$F(x)=x^3-x$', font_size=30, color= TEAL).next_to(curves[3], 0.1*UP+0.15*RIGHT),
                    Tex(r'$f(x)=3x^2-1$', font_size=30, color= ORANGE).next_to(curves[4], 0.1*UP+0.1*LEFT)
               ]
        
        lines =[
                    DoubleArrow(start=1.5*UP+1.5*RIGHT, end=1.5*UP+5*RIGHT,buff=0,color=PURPLE,tip_shape_start=ArrowCircleFilledTip), #Right third
                    Line(start=1.5*UP+1.5*LEFT, end=1.5*UP+1.5*RIGHT,color=PURPLE),                                              #Middle third
                    DoubleArrow(start=1.5*UP+5*LEFT, end=1.5*UP+1.5*LEFT,buff=0,color=PURPLE,tip_shape_end=ArrowCircleFilledTip),  #Left third arrow
                    DashedLine(start=DOWN, end= UP),  #-b line separator
                    DashedLine(start=DOWN, end= UP),  #b line sep
                    DashedLine(start=DOWN, end= UP)
               ]
    
        lLabels=[
                    Tex(r"$-1/\sqrt{3}$", font_size=30).next_to(lines[2].get_right()+0.4*DOWN+LEFT), #-b label
                    Tex(r"$-1/\sqrt{3}$", font_size=30).next_to(lines[0].get_left()+0.4*DOWN+0.5*LEFT),      #b label
                    Tex(r"$x$").next_to(lines[0].get_right(), aligned_edge=LEFT)           #x-axis label
      
               ]
        
        tables=[
                    MathTable(
                        [[ 'x' ,  'f(x)', '\Dot{x}' , '\Ddot{x}'],
                        [ 'x>b' ,  '+ve','+ve', '-ve']],
                        include_outer_lines=True),
                    MathTable(
                        [[ 'x' ,  'f(x)', '\Dot{x}' , '\Ddot{x}'],
                        [ 'x>b' ,  '+ve','+ve', '-ve'],
                        [ '-b<x<b' ,  '-ve', '+ve', '+ve']],
                        include_outer_lines=True),
                    MathTable(
                        [[ 'x' ,  'f(x)', '\Dot{x}' , '\Ddot{x}'],
                        [ 'x>b' ,  '+ve','+ve', '-ve'],
                        [ '-b<x<b' ,  '-ve', '+ve', '+ve'],
                        [ 'x<-b' ,  '+ve', '+ve', '-ve']],
                        include_outer_lines=True),
                    MathTable(
                          [[ '\Ddot{x}' ,  '-ve', '+ve' , '-ve']],
                            include_outer_lines=True 
                        ),

                    MathTable(
                          [[ 'x' ,  '\Ddot{x}'],
                           [ 'x<0' ,  '+ve'],
                           [ 'x>0' ,  '-ve']
                           ],
                            include_outer_lines=True 
                        )
               ]
        
        groups=[
                    VGroup(tables[0]).scale(0.75).move_to(1.5*DOWN),
                    VGroup(tables[1]).scale(0.75).move_to(1.5*DOWN),
                    VGroup(tables[2]).scale(0.75).move_to(1.5*DOWN),
                    VGroup(tables[3]).scale(0.75).move_to(3*DOWN),
                    VGroup(lines[3]).scale(1.3).shift(3*LEFT),
                    VGroup(lines[4]).scale(1.3).shift(3*RIGHT),
                    VGroup(lines[5]).scale(1.15),
                    VGroup(tables[4]).scale(0.6).move_to(2.5*DOWN),
                    VGroup(dots[21], dLabels[9]),
                    VGroup(dots[22],dLabels[10])
               ]
        '''
            ************************************
                       ANIMATIONS
            ************************************
        '''
        '''
            Component configuration
        '''
        tex[4].next_to(tex[5], LEFT)
        rects[0].align_to(tex[5], LEFT)

        for i in range(6,10):
            tex[i].align_to(tex[5], LEFT)

        for t in range(0,3):
            tables[t].get_horizontal_lines()[0].set_color(RED)
            tables[t].get_horizontal_lines()[2].set_color(RED)
            tables[t].get_vertical_lines()[4].set_color(RED)
            tables[t].get_vertical_lines()[1].set_color(RED)

        axes[2].add_labels({-unitShift: Tex(r"$-b$"), 0: Tex(r"$0$"), unitShift: Tex(r"$b$")})
        axes[3].add_labels({0: Tex(r"$0$"), 3: Tex(r"$b$")})
        axes[4].add_labels({0: Tex(r"$0$")})
        axes[5].add_labels({0: Tex(r"$0$")})


        '''
            Animation implemenations
        '''

        #Frame 1
        self.play(FadeIn(tex[0]),run_time=2)
        self.play(FadeIn(tex[1]))
        self.wait(1.5)
        self.play(FadeOut(tex[1]),FadeOut(tex[0]))
        self.remove(tex[0], tex[1])

        #Frame 2
        self.play(FadeIn(tex[2]))
        self.wait(1.1)
        self.play(Write(tex[3]))
        self.wait(1.1)

        self.play(FadeIn(tex[4]))

        for i in range(5,10):
            self.play(Write(tex[i], run_time=2))
            self.wait(0.5)


        self.wait(1.2)
        self.play(Write(tex[10]))
        self.wait(2.1)
        self.play(FadeIn(tex[11]))
        self.wait(2)

        # #Frame 3
        self.play(Create(rects[0], run_time=1.5))
        

        group = VGroup()
        for i in range(2,9):
            group.add(tex[i])

        group.add(tex[10], tex[11])
        self.play(FadeOut(group))

        self.remove(group)

        self.play(FadeIn(tex[12]))
        self.wait(1.5)
        self.play(FadeOut(tex[12]))
        self.remove(tex[12])
        self.wait(1.5)
        self.play(ReplacementTransform(tex[9],tex[27]), FadeOut(rects[0]), Write(tex[28]))
        
        self.play(Create(axes[0], run_time=2.5, rate_func= lambda t:t))
        self.wait(1.3)
        self.play(ReplacementTransform(rects[0], rects[1]), FadeIn(dots[0]), FadeIn(dLabels[0]))
        self.wait(1.2)
        self.play(ReplacementTransform(rects[1], rects[2]), Create(curves[0]))
        self.wait(1.2)
        self.play(ReplacementTransform(rects[2], rects[3]), ReplacementTransform(curves[0], curves[1]))
        self.wait(1.2)
        self.play(ReplacementTransform(rects[3], rects[4]), ReplacementTransform(curves[1], curves[2]))

        #Frame 4
        self.play(FadeOut(tex[27]), FadeOut(tex[28]), FadeOut(rects[4]))
        self.remove(tex[27],tex[28], rects[4])

        self.play(Write(tex[13]), run_time=2)
        self.wait(1.5)
        self.play(ReplacementTransform(axes[0], axes[1]),ReplacementTransform(dots[0], dots[1]),ReplacementTransform(curves[2], curves[3]),ReplacementTransform(dLabels[0],dLabels[1]))
        self.play(FadeIn(dots[2]), FadeIn(dLabels[2]), FadeIn(cLabels[0]))
        self.wait(2)
        self.play(Write(tex[14]))
        self.wait(1.5)
        self.play(Create(curves[4]))
        self.play(Write(cLabels[1]))
        self.play(FadeIn(dots[3]),FadeIn(dots[4]),FadeIn(dLabels[3]),FadeIn(dLabels[4]))
        self.wait(3)

        
        group = VGroup()
        group.add(tex[13],axes[1],dots[1],curves[3],dLabels[1],dots[2],dLabels[2],cLabels[0],
                  tex[14],curves[4],cLabels[1],dots[3],dots[4],dLabels[3],dLabels[4])
        self.play(

                    FadeOut(group)

                 )
        self.remove(group)
        self.wait(1.2)

        #Frame 5
        for i in range(15,17):
            self.play(Write(tex[i]))

        self.play(FadeIn(tex[17], run_time=2))

        self.wait(1.2)
        self.play(ReplacementTransform(tex[16],tex[29], run_time=2))
        self.wait(0.5)
        self.play(Write(tex[30]))

        self.wait(1.5)

        #Frame 6
        group = VGroup()
        group.add(tex[15], tex[17])
        self.play(FadeOut(group))
        self.remove(group)

        self.wait(1.5)

        self.play(tex[29].animate.shift(2.5*UP))

        self.play(FadeOut(tex[30]), ReplacementTransform(tex[29], tex[31]))

        self.remove(tex[30])

        self.wait(1.5)
        group = VGroup()
        for i in range(3):
            group.add( lines[i], lLabels[i] )

        self.play(FadeIn(group))
        self.wait(2)
        self.play(Write(tex[18], run_time=2))

        self.wait(1.3)
        self.play(Indicate(lines[0], run_time=1.2))
        self.play(Create(groups[0], run_time=4))
        self.wait(1.5)

        for i in range(1,3):
            self.play(Indicate(lines[i], run_time=1.2))
            self.play(ReplacementTransform(groups[i-1],groups[i], run_time=4))
            self.wait(1.5)

        

        #Frame 7
        self.play(ReplacementTransform(tex[18],tex[32]))
        self.wait(1.2)
        self.play(FadeIn(axes[2]), ReplacementTransform(groups[2],groups[3]) ,FadeOut(group))
        self.remove(group)
        self.play(FadeIn(groups[4]), FadeIn(groups[5]), FadeIn(dots[5]))

        self.wait(1.5)
        self.play(ReplacementTransform(dots[5], dots[9],run_time=6, rate_func=lambda t:t), FadeIn(dots[6], dLabels[5]))
        self.play(ReplacementTransform(dots[9],dots[10], run_time=1, rate_func=lambda t:t), FadeIn(dots[7], dLabels[6]))
        self.play(ReplacementTransform(dots[10], dots[11], run_time=6, rate_func=lambda t:t), FadeIn(dots[8], dLabels[7]))

        self.wait(1.1)

        self.play(ReplacementTransform(groups[3],tex[33]))

        group= VGroup()
        for i in range(6,9):
            group.add(dots[i], dLabels[i-1])
        self.play(FadeOut(group))
        self.remove(group)

        self.wait(1.3)
        self.play(FadeIn(dots[12]))
        self.play(ReplacementTransform(dots[12], dots[13],run_time=6, rate_func=lambda t:t))
        self.play(ReplacementTransform(dots[13],dots[14], run_time=1, rate_func=lambda t:t))
        self.play(ReplacementTransform(dots[14], dots[15], run_time=6, rate_func=lambda t:t))

        self.wait(2)

        group = VGroup(tex[31], tex[32], tex[33],dots[11], dots[15], groups[4], groups[5])
        self.play(FadeOut(group))
        self.remove(group)

        #Frame 8
        
        self.play(Write(tex[34], run_time=2))


        self.play(  ReplacementTransform(axes[2], axes[3], run_time= 2)  )
        self.wait(1.1)
        self.play(FadeIn(dots[16]))
        self.wait(1.5)
        
        self.play(FadeIn(tex[35]), FadeIn(dots[18], dLabels[8]), )
        self.wait(1.1)
        self.play(ReplacementTransform(dots[16], dots[17], run_time=4, rate_func= lambda t: t**0.5))

        self.wait(1.1)
        self.play(FadeIn(tex[36])) 
        self.wait(1.1)
        self.play(ReplacementTransform(dots[18],dots[19]), ReplacementTransform(dots[17], dots[20], run_time=4, rate_func= lambda t: t**0.5))

        self.wait(2)
        self.play(Write(tex[37]))
        self.wait(2)

        group = VGroup(tex[34], tex[35], tex[36], dots[19], dLabels[8],dots[20], axes[3] )
        self.play(FadeOut(group))
        self.remove(group)

        #Frame 9
        self.wait(1.1)
        self.play(tex[37].animate.move_to(3*UP))
        self.wait(1.2)
        self.play(Write(tex[38]))
        self.wait(1.2)
        self.play(Write(tex[22]))

        self.wait(1.2)
        group= VGroup(tex[37], tex[38], tex[22])
        self.play(ReplacementTransform(group, tex[40]))
        self.wait(2)
        self.play(Write(tex[39], run_time=3))

        self.wait(1.2)
        self.play(Create(groups[7], run_time=5))
        self.wait(1.2)
        self.play(Create(axes[4], run_time=3), Create( groups[6]),  FadeIn(dots[23]))

        self.wait(2)
        self.play(ReplacementTransform(tex[39], tex[41], run_time=2))
        self.wait(1.5)
        self.play(FadeIn(groups[8]),ReplacementTransform(dots[23], dots[24], run_time= 3, rate_func= lambda t: t**5))
        self.play(FadeIn(groups[9]), ReplacementTransform(dots[24], dots[25], run_time= 3,rate_func= lambda t: t**0.5))
        self.play(ReplacementTransform(dots[25], dots[26],run_time= 3,rate_func= lambda t: t**5  ))
        self.play(ReplacementTransform(dots[26], dots[27], run_time=3, rate_func= lambda t: t**0.5))
        

        group = VGroup()
        group.add(tex[40], tex[41], groups[8], groups[9], groups[6], axes[4], groups[7], dots[27] )
        
        self.play(FadeOut(group))
        self.remove(group)

        #Frame 10
        self.wait(2)
        self.play(FadeIn(tex[42], run_time=3))
        self.wait(2)
        self.play(FadeOut(tex[42]))
        self.remove(tex[42])

        #Frame 11
        self.wait(2)
        self.play(FadeIn(axes[5], run_time=2))
        dot = dots[28]

        self.play(FadeIn(dot))
        self.wait(2)

        p = 10

        for i in range(1):
            self.play(dot.animate(run_time=4, rate_func=lambda t: t**p).move_to(UP))
            self.play(dot.animate(run_time=4, rate_func=lambda t: 1/( (1-(1/p)) + 1/((t+0.0000000000001)*p) )  ).move_to(UP+6*RIGHT))  
            self.play(dot.animate(run_time=4, rate_func=lambda t: t**p).move_to(UP))
            self.play(dot.animate(run_time=4, rate_func=lambda t: 1/( (1-(1/p)) + 1/((t+0.0000000000001)*p) )).move_to(UP+6*LEFT))
         

        self.play(FadeOut(axes[5] ),dot.animate(run_time=4, rate_func=lambda t: t**p).move_to(UP))
        self.play(FadeIn(tex[24],run_time=2.3),dot.animate(run_time=4, rate_func=lambda t: 1/( (1-(1/p)) + 1/((t+0.0000000000001)*p) )  ).move_to(UP+6*RIGHT))
        self.play(dot.animate(run_time=4, rate_func=lambda t: t**p).move_to(UP))
        self.play(FadeIn(tex[25], run_time=2.3),dot.animate(run_time=4, rate_func=lambda t: 1/( (1-(1/p)) + 1/((t+0.0000000000001)*p) )).move_to(UP+6*LEFT))
        self.wait(2)
        group = VGroup()

        group.add(tex[25], dot)

        mu = 1
        
        vdp = StreamLines(funcs[3],
                        x_range=[xmin, xmax, step],
                        y_range=[ymin, ymax, step],
                        colors = [RED, ORANGE, YELLOW, GREEN, TEAL, PURPLE],
                        stroke_width = 3,
                        padding = 1
                        )
        
        self.play(FadeOut(group, run_time=1), ReplacementTransform(tex[24], tex[26]), )
        self.wait(1.2)
        self.play(FadeOut(tex[26]))
        self.remove(group, tex[26])

        self.add(vdp)
        vdp.start_animation(warm_up=True, flow_speed=1.5, time_width=0.75)
        self.wait(9)
        self.play(vdp.end_animation())
        
        self.wait(2)
        self.play(FadeIn(tex[43], run_time=1.8))
        self.wait(1.2)
        self.play(FadeIn(tex[44], run_time=1.8))
        self.wait(2)
        
        