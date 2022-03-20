from click import style
from manim import *
from colour import Color
import os
import sys
sys.path.append('../')

import Objects.helpers as helpers
from Configs import *

path_to_SVG = os.path.join(helpers.root(), 'Objects', 'SVG_files')
path_to_Objects = os.path.join(helpers.root(), 'Objects')





class ChessFigures(VMobject):
    def __init__(self):
        VMobject.__init__(self)


        self.white_pawn = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'pawn.svg'))
        self.white_pawn.scale(chess_figures_scale_factor)
        self.white_pawn.set_fill(white_chess_figures_fill_color)
        self.white_pawn.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_pawn = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'pawn.svg'))
        self.black_pawn.scale(chess_figures_scale_factor)
        self.black_pawn.set_fill(black_chess_figures_fill_color)
        self.black_pawn.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)


        self.white_knight = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'knight.svg'))
        self.white_knight.scale(chess_figures_scale_factor)
        self.white_knight.set_fill(white_chess_figures_fill_color)
        self.white_knight.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_knight = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'knight.svg'))
        self.black_knight.scale(chess_figures_scale_factor)
        self.black_knight.set_fill(black_chess_figures_fill_color)
        self.black_knight.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)


        self.white_bishop = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'bishop.svg'))
        self.white_bishop.scale(chess_figures_scale_factor)
        self.white_bishop.set_fill(white_chess_figures_fill_color)
        self.white_bishop.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_bishop = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'bishop.svg'))
        self.black_bishop.scale(chess_figures_scale_factor)
        self.black_bishop.set_fill(black_chess_figures_fill_color)
        self.black_bishop.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)


        self.white_rook = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'rook.svg'))
        self.white_rook.scale(chess_figures_scale_factor)
        self.white_rook.set_fill(white_chess_figures_fill_color)
        self.white_rook.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_rook = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'rook.svg'))
        self.black_rook.scale(chess_figures_scale_factor)
        self.black_rook.set_fill(black_chess_figures_fill_color)
        self.black_rook.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)


        self.white_queen = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'queen.svg'))
        self.white_queen.scale(chess_figures_scale_factor)
        self.white_queen.set_fill(white_chess_figures_fill_color)
        self.white_queen.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_queen = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'queen.svg'))
        self.black_queen.scale(chess_figures_scale_factor)
        self.black_queen.set_fill(black_chess_figures_fill_color)
        self.black_queen.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)


        self.white_king = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'king.svg'))
        self.white_king.scale(chess_figures_scale_factor)
        self.white_king.set_fill(white_chess_figures_fill_color)
        self.white_king.set_stroke(white_chess_figures_stroke_color, chess_figures_stroke_width)

        self.black_king = SVGMobject(os.path.join(path_to_SVG, 'chess_figures', 'king.svg'))
        self.black_king.scale(chess_figures_scale_factor)
        self.black_king.set_fill(black_chess_figures_fill_color)
        self.black_king.set_stroke(black_chess_figures_stroke_color, chess_figures_stroke_width)




class Man(VMobject):
    def __init__(self, svg_index=1):
        VMobject.__init__(self)

        man = SVGMobject(os.path.join(path_to_SVG, 'people', 'men', f'man_{svg_index}'))
        man.set_color(WHITE)

        self.add(man)



class Boy(VMobject):
    def __init__(self, svg_index=1):
        VMobject.__init__(self)

        boy = SVGMobject(os.path.join(path_to_SVG, 'people', 'children', f'boy_{svg_index}'))
        boy.set_color(WHITE)

        self.add(boy)



class Girl(VMobject):
    def __init__(self, svg_index=1):
        VMobject.__init__(self)

        girl = SVGMobject(os.path.join(path_to_SVG, 'people', 'children', f'girl_{svg_index}'))
        girl.set_color(WHITE)

        self.add(girl)



class Pigeon(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        pigeon = SVGMobject(os.path.join(path_to_SVG, 'animals', 'pigeon'))
        pigeon.set_color(WHITE).scale(0.5)

        self.add(pigeon)


class Rabbit(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        rabbit = SVGMobject(os.path.join(path_to_SVG, 'animals', 'rabbit'))
        rabbit.set_color(WHITE).scale(0.55)

        self.add(rabbit)




class Cage(VMobject):
    def __init__(self, style='square'):
        VMobject.__init__(self)

        if style == 'square':
            cage = SVGMobject(os.path.join(path_to_SVG, 'cage_square'))
            cage.set_color(GOLD).scale(1.5)

        if style == 'bird':
            cage = SVGMobject(os.path.join(path_to_SVG, 'cage_bird'))
            cage.set_color(GOLD).scale(2)

        self.add(cage)



class OpenScissors(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        open_scissors = SVGMobject(os.path.join(path_to_SVG, 'scissors', 'open_scissors'))
        open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)

        self.add(open_scissors)


class ClosedScissors(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        closed_scissors = SVGMobject(os.path.join(path_to_SVG, 'scissors', 'closed_scissors'))
        closed_scissors.set_color(WHITE).scale(0.4).rotate(PI/5)

        self.add(closed_scissors)


class ThinkingBubble(VMobject):
    def __init__(self, smooth=True, from_left_to_right=True, style=1):
        VMobject.__init__(self)

        if smooth:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'smooth_thinking_bubble_left_1')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'smooth_thinking_bubble_left_2')
                        )
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'smooth_thinking_bubble_right_1')
                        )
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'smooth_thinking_bubble_right_2')
                        )
        else:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'thinking_bubble_left_1')
                        )
                    thinking_bubble = VGroup(thinking_bubble[1], thinking_bubble[2], thinking_bubble[0])
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'thinking_bubble_left_2')
                        )
                    thinking_bubble = VGroup(thinking_bubble[1], thinking_bubble[2], thinking_bubble[3], thinking_bubble[0])
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'thinking_bubble_right_1')
                        )
                    thinking_bubble = VGroup(thinking_bubble[1], thinking_bubble[2], thinking_bubble[0])
                else:
                    thinking_bubble = SVGMobject(
                            os.path.join(path_to_SVG, 'thinking_bubbles', 'thinking_bubble_right_2')
                        )
                    thinking_bubble = VGroup(thinking_bubble[1], thinking_bubble[2], thinking_bubble[3], thinking_bubble[0])
        
        thinking_bubble.set_color(WHITE)

        self.add(thinking_bubble)




class Pen(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        pen = SVGMobject(os.path.join(path_to_SVG, 'pen')).set_color(WHITE).scale(0.5).rotate(PI/7)

        self.add(pen)



class Pencil(VMobject):
    def __init__(self, svg_index=1):
        VMobject.__init__(self)

        pencil = SVGMobject(os.path.join(path_to_SVG, 'pencils', f'pencil_{svg_index}'))
        pencil.scale(0.6).rotate(PI / 12)
        pencil.set_color(WHITE)

        self.add(pencil)



class Scales(VMobject):
    def __init__(self, svg_index=1):
        VMobject.__init__(self)

        scales = SVGMobject(os.path.join(path_to_SVG, 'scales', f'scale_{svg_index}')).scale(1.2)
        

        if svg_index == 1:
            self.body = VGroup(scales[0], scales[1], scales[3], scales[2])
            self.left_plate = scales[4]
            self.right_plate = scales[5]
        
        else:
            scales.set_color(WHITE)
            self.body = scales[0]
            self.left_plate = scales[2]
            self.right_plate = scales[1]

        self.add(self.body, self.left_plate, self.right_plate)



class Weight(VGroup):
    def __init__(self, kg=1, unit_kg=1):
        VGroup.__init__(self)

        self.weight_value = kg

        self.weight = VGroup(
            SVGMobject(os.path.join(path_to_SVG, 'weight')).set_color(WHITE).scale(0.5),
            MathTex(f"{kg}", color=BLACK, font_size=35).shift(0.1 * DOWN)
        ).scale(((kg/(2*unit_kg)) ** (1./3.)) * 0.75)

        self.kettlebell = self.weight[0]
        self.weight_text = self.weight[1]

        self.add(self.kettlebell, self.weight_text)



class  Apple(VMobject):
    def __init__(self, color=GREEN,):
        VMobject.__init__(self)

        if color == GREEN:
            apple = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'green_apple'))
        
        elif color == RED:
            apple = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'red_apple'))
        
        apple.scale(0.25)

        self.add(apple)




class Mushroom(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        mushroom = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'mushroom'))
        mushroom.scale(0.25)

        self.add(mushroom)


class Tomato(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        tomato = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'tomato'))
        tomato.scale(0.25)

        self.add(tomato)


class Carrot(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        carrot = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'carrot'))
        carrot.scale(0.25)

        self.add(carrot)



class Banana(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        banana = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'banana'))
        banana.scale(0.25)

        self.add(banana)


class Pear(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        pear = SVGMobject(os.path.join(path_to_SVG, 'fruits', 'pear'))
        pear.scale(0.25)

        self.add(pear)



class ScaleStar(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        star = SVGMobject(os.path.join(path_to_SVG, 'star')).set_stroke(width=0)
        star.scale(0.25)

        self.add(star)









class Scissors():
    def __init__(self, cut_coordinate=ORIGIN, style=1):
        self.style = style

        if style == 1:
            self.open_scissors = OpenScissors()
            self.closed_scissors = ClosedScissors()
            self.cut_coordinate = np.array(cut_coordinate) - np.array([0.2, 0.4, 0])
            self.closed_scissors.move_to(self.cut_coordinate)
            self.open_scissors.move_to(self.cut_coordinate - np.array([0, 0.5, 0]))

        if style == 2:
            self.cut_coordinate = cut_coordinate
            scissor_1 = SVGMobject(os.path.join(path_to_SVG, 'scissors', 'scissors_1')).set_color(WHITE)
            scissor_2 = SVGMobject(os.path.join(path_to_SVG, 'scissors', 'scissors_2')).set_color(WHITE)
            dot = Dot().scale(0.2)
            self.__p_end = [a + b for a, b in zip([0, -0.35, 0], cut_coordinate)]
            VGroup(scissor_1, scissor_2).arrange(RIGHT, buff=0.1)
            scissor_1.shift(0.08 * DOWN + 0.6 * RIGHT)
            scissor_2.shift(0.08 * DOWN - 0.6 * RIGHT)
            scissors_with_dot = VGroup(scissor_1, scissor_2, dot).scale(0.5)
            point = scissors_with_dot[2].get_center()
            scissors_with_dot[0].rotate(angle=-0.02, about_point=point)
            scissors_with_dot[1].rotate(angle=0.02, about_point=point)
            scissors_with_dot.move_to(self.__p_end)
            scissors_with_dot.shift(DOWN)
            self.siz = scissors_with_dot



    def cut(self, scene : Scene, run_time=3):
        if self.style == 1:
            scene.play(FadeIn(self.open_scissors), run_time=run_time/3)
            scene.wait(run_time/9)
            scene.play(self.open_scissors.animate().move_to(self.cut_coordinate), run_time=run_time/3)
            scene.wait(run_time/9)
            scene.remove(self.open_scissors)
            scene.add(self.closed_scissors)
            scene.add_sound(os.path.join(path_to_Objects, 'sounds', 'scissors_sound'))
            scene.wait(0.25)
            scene.remove(self.closed_scissors)
            scene.add(self.open_scissors)
            scene.wait(run_time/9)

        if self.style == 2:
            run_time = 1
            def function_from_time(mobject, t):
                frame_rate = scene.camera.frame_rate
                dt = run_time/frame_rate
                dl = [0, run_time/frame_rate, 0]
                if t < run_time/2:
                    angle = PI / 8 * dt
                else:
                    angle = -PI / 8 * dt
                #p_end = [a+b for a, b in zip([0, -0.25, 0], mobject[3].get_center())]
                mobject.shift(dl)
                point = mobject[2].get_center()
                mobject[0].rotate(angle=angle, about_point=point)
                mobject[1].rotate(angle=-angle, about_point=point)
            scene.play(UpdateFromAlphaFunc(self.siz, function_from_time, run_time=run_time, rate_func=linear))
            scene.add_sound(os.path.join(path_to_Objects, 'sounds', 'scissors_sound'))
            scene.wait(0.2)
            self.siz.move_to(self.__p_end)

    def fade_out(self, scene : Scene, run_time=1):
        if self.style == 1:
            scene.play(
                self.open_scissors.animate().move_to(self.cut_coordinate - np.array([0, 0.5, 0])).set_opacity(0),
                run_time=run_time
            )
            scene.remove(self.open_scissors)
        
        if self.style == 2:
            def function_from_time(mobject, t):
                frame_rate = scene.camera.frame_rate
                dt = run_time/frame_rate
                dl = [0, -run_time/frame_rate, 0]
                angle = PI / 10 * dt
                mobject.shift(dl)
                point = mobject[2].get_center()
                color = Color(hue=1, saturation=t/3, luminance=1-t)
                mobject.set_color(color)
                mobject[0].rotate(angle=angle, about_point=point)
                mobject[1].rotate(angle=-angle, about_point=point)
            scene.play(UpdateFromAlphaFunc(self.siz, function_from_time, run_time=run_time, rate_func=linear))
            scene.remove(self.siz)
        

class Paper(VMobject):
    def __init__(self):
        VMobject.__init__(self)

        self.paper_1 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_1')).set_color(WHITE)
        self.paper_2 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_2')).set_color(WHITE).scale(0.87)
        self.paper_3 = SVGMobject(os.path.join(path_to_SVG, 'papers', 'paper_3')).set_color(WHITE).scale(0.77)
