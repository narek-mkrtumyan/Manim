import sys

sys.path.append('../../../')
sys.path.append('../../')
sys.path.append('../')
from Functions.QarakusiFunctions import *


class Problem10323(Scene):
    def construct(self):
        self.add(bounds)

    # INITS
        numbers_font_size = 50
        labels_font_size = 50

        children_segment = Segment([-2.5, 2.5, 0], [-1, 2.5, 0])
        children_label = MathTex(r'\textrm{Ե.}', tex_template=armenian_tex_template, font_size=labels_font_size)
        children_label.next_to(children_segment, LEFT)
        
        men_segment_1 = children_segment.copy().shift(1.5*DOWN)
        men_label = MathTex(r'\textrm{Տ.}', tex_template=armenian_tex_template, font_size=labels_font_size)
        men_label.next_to(men_segment_1, LEFT)

    # Animations block
        self.play(Create(children_segment))
        self.wait(0.25)
        self.play(Write(children_label))
        self.wait(0.5)

        self.play(ReplacementTransform(children_segment.copy(), men_segment_1))
        self.wait(0.5)
        men_segments = MultiplySegmentRotating(self, men_segment_1, merge_segments=False, run_time=1.5)
        self.wait(0.25)
        self.play(Write(men_label))
        self.wait(0.5)

    # INITS
        women_segments = men_segments.copy().shift(1.5*DOWN)
        women_segments_extention = Segment(
            women_segments[-1][0][0].get_start_and_end()[0], 
            women_segments[-1][0][0].get_start_and_end()[0] + np.array([0.7, 0, 0]),
            color=ORANGE, mathtex=MathTex(r'10', font_size=numbers_font_size)
        )
        women_label = MathTex(r'\textrm{Կ.}', tex_template=armenian_tex_template, font_size=labels_font_size)
        women_label.next_to(women_segments, LEFT)

        brace = BraceBetweenPoints(
            women_segments_extention[0][0].get_start_and_end()[1] + np.array([0.5, -0.25, 0]),
            women_segments_extention[0][0].get_start_and_end()[1] + np.array([0.5, 3.25, 0]),
            )
        
        together_525 = MathTex(r'525', font_size=numbers_font_size).next_to(brace, RIGHT)

        together_minus_extra = MathTex(r'525', r'-', r'10', r'=', r'515', font_size=numbers_font_size)
        together_minus_extra.move_to(women_segments[1], DOWN).shift(1*DOWN)

        numbers = VGroup(*[MathTex(rf'{i}', color=GREEN, font_size=numbers_font_size) for i in range(1, 6)])
        numbers.move_to([0, 2.5, 0]).set_opacity(0).shift(0.5*UP)
        numbers[0].shift(0.5*DOWN)
        mas = MathTex(r'\textrm{մաս}', tex_template=armenian_tex_template).next_to(numbers[0], RIGHT)

        segments = VGroup(children_segment, *men_segments, *women_segments)

        dividing_by_5 = MathTex(r'515', r':', r'5', r'=', r'103', font_size=numbers_font_size)
        dividing_by_5.next_to(together_minus_extra, DOWN).shift(0.5*DOWN)
        dividing_by_5[2].set_color(GREEN)

        answer = MathTex(r'103', font_size=numbers_font_size).next_to(children_segment, UP*0.5).shift(0.25*DOWN)
        answer_rect = SurroundingRectangle(answer, color=GREEN)

        open_scissors = SVGMobject('../../../Functions/SVG_PNG_files/open_scissors.svg')
        open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)

        closed_scissors = ImageMobject('../../../Functions/SVG_PNG_files/closed_scissors.png')
        closed_scissors.set_color(WHITE).scale(0.13).shift(0.1*DOWN).rotate(PI/5)



    # ANIMATIONS

        self.play(ReplacementTransform(men_segments.copy(), women_segments))
        self.wait(0.5)
        self.play(Create(women_segments_extention))
        self.wait(0.5)
        self.play(Write(women_label))
        self.wait(0.5)

        self.play(Create(brace))
        self.wait(0.5)
        self.play(Write(together_525))
        self.wait(0.5)

        cut_with_scissors(self, open_scissors, closed_scissors, women_segments_extention[0][0].get_start_and_end()[0])

        self.play(women_segments_extention.animate().shift(0.25*RIGHT))
        self.wait(0.5)

        self.play(ReplacementTransform(together_525.copy(), together_minus_extra[0]))
        self.play(Write(together_minus_extra[1]))
        self.play(ReplacementTransform(women_segments_extention[1].copy(), together_minus_extra[2]))
        self.play(Write(together_minus_extra[3:]))
        self.wait(0.5)
        

        for i in range(5):
            segments[i].set_color(GREEN)
            self.play(segments[i].animate(rate_func=there_and_back, run_time=0.5).scale(1.2))
            segments[i].set_color(WHITE)

            if i == 0:
                self.play(numbers[i].animate().set_opacity(1), run_time=0.5)
                self.play(Write(mas), run_time=0.5)
            else:
                self.play(
                    numbers[i-1].animate().shift(0.5*DOWN).set_opacity(0),
                    numbers[i].animate().shift(0.5*DOWN).set_opacity(1),
                    run_time=0.5
                )
        self.wait(0.5)
        
        self.play(ReplacementTransform(together_minus_extra[-1].copy(), dividing_by_5[0]))
        self.play(Write(dividing_by_5[1]))
        self.play(
            ReplacementTransform(numbers[-1], dividing_by_5[2]),
            FadeOut(mas)
        )
        self.play(Write(dividing_by_5[3:]))
        self.wait(0.5)

        self.play(ReplacementTransform(dividing_by_5[-1].copy(), answer))
        self.wait(0.5)
        self.play(Create(answer_rect))
        self.wait(0.5)





class test(Scene):
    def construct(self):
        
        self.wait()

