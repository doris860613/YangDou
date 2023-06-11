"""
File: my_drawing.py
Name: Doris
\

----------------------
Title: WHERE's WALLY? (Kindergarten Level)

創作理念：趕快加入「威力超猛軍團」，你就是最厲害的威力小偵探！不怕找不到，只怕你不找！
        疫情大解封，終於可以出國玩啦！愛亂跑的威力當然不放過這次機會，於是威力踏上環遊世界的旅程
        跑到冰島玩耍，結果．．．．．阿阿阿阿阿阿阿！！！！威力居然不小心被可愛的雪人族包圍啦！！！！
        身為威力小偵探的你是否能不被可愛的雪人們影響，並成功將威力從雪人們中救出呢？
        難度指數★☆☆☆☆
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: WHERE's WALLY? (Kindergarten Level)

    創作理念：趕快加入「威力超猛軍團」，你就是最厲害的威力小偵探！不怕找不到，只怕你不找！
            疫情大解封，終於可以出國玩啦！愛亂跑的威力當然不放過這次機會，於是威力踏上環遊世界的旅程
            跑到冰島玩耍，結果．．．．．阿阿阿阿阿阿阿！！！！威力居然不小心被可愛的雪人族包圍啦！！！！
            身為威力小偵探的你是否能不被可愛的雪人們影響，並成功將威力從雪人們中救出呢？
            難度指數★☆☆☆☆
    """
    window = GWindow(width=500, height=500, title='WHERE\'s WALLY? (Kindergarten Level)')

    # snowman1-snowman60
    y1 = 2
    y2 = 12
    y3 = 12
    y4 = 6
    y5 = 12
    y6 = 27
    y7 = 16
    y8 = 16
    y9 = 20
    y10 = 20
    y11 = 18
    y12 = 23
    y13 = 22
    y14 = 30
    y15 = 23
    y16 = 30
    y17 = 23
    y18 = 30
    y19 = 36
    y20 = 42
    for i in range(6):
        x1 = 30
        x2 = 22
        x3 = 30
        x4 = 30
        x5 = 18
        x6 = 14
        x7 = 22
        x8 = 27
        x9 = 16
        x10 = 26
        x11 = 26
        x12 = 23
        x13 = 28
        x14 = 16
        x15 = 10
        x16 = 34
        x17 = 40
        x18 = 18
        x19 = 15
        x20 = 16
        for j in range(10):
            snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
            snowman_hat_wool.filled = True
            snowman_hat_wool.fill_color = 'white'
            window.add(snowman_hat_wool)
            snowman_hat = GPolygon()
            snowman_hat.add_vertex((x2, y2))
            snowman_hat.add_vertex((x3, y3))
            snowman_hat.add_vertex((x4, y4))
            snowman_hat.filled = True
            snowman_hat.fill_color = 'red'
            window.add(snowman_hat)
            snowman_face = GOval(14, 14, x=x5, y=y5)
            snowman_face.filled = True
            snowman_face.fill_color = 'white'
            window.add(snowman_face)
            snowman_body = GOval(22, 22, x=x6, y=y6)
            snowman_body.filled = True
            snowman_body.fill_color = 'white'
            window.add(snowman_body)
            snowman_leye = GOval(1, 1, x=x7, y=y7)
            snowman_leye.filled = True
            snowman_leye.fill_color = 'black'
            window.add(snowman_leye)
            snowman_reye = GOval(1, 1, x=x8, y=y8)
            snowman_reye.filled = True
            snowman_reye.fill_color = 'black'
            window.add(snowman_reye)
            snowman_nose = GPolygon()
            snowman_nose.add_vertex((x9, y9))
            snowman_nose.add_vertex((x10, y10))
            snowman_nose.add_vertex((x11, y11))
            snowman_nose.filled = True
            snowman_nose.fill_color = 'orange'
            window.add(snowman_nose)
            snowman_mouth = GLine(x12, y12, x13, y13)
            window.add(snowman_mouth)
            snowman_lhand = GLine(x14, y14, x15, y15)
            window.add(snowman_lhand)
            snowman_rhand = GLine(x16, y16, x17, y17)
            window.add(snowman_rhand)
            snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
            snowman_cloth1.filled = True
            snowman_cloth1.fill_color = 'red'
            snowman_cloth1.color = 'red'
            window.add(snowman_cloth1)
            snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
            snowman_cloth2.filled = True
            snowman_cloth2.fill_color = 'red'
            snowman_cloth2.color = 'red'
            window.add(snowman_cloth2)
            snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
            snowman_cloth3.filled = True
            snowman_cloth3.fill_color = 'red'
            snowman_cloth3.color = 'red'
            window.add(snowman_cloth3)
            x1 += 50
            x2 += 50
            x3 += 50
            x4 += 50
            x5 += 50
            x6 += 50
            x7 += 50
            x8 += 50
            x9 += 50
            x10 += 50
            x11 += 50
            x12 += 50
            x13 += 50
            x14 += 50
            x15 += 50
            x16 += 50
            x17 += 50
            x18 += 50
            x19 += 50
            x20 += 50
        y1 += 50
        y2 += 50
        y3 += 50
        y4 += 50
        y5 += 50
        y6 += 50
        y7 += 50
        y8 += 50
        y9 += 50
        y10 += 50
        y11 += 50
        y12 += 50
        y13 += 50
        y14 += 50
        y15 += 50
        y16 += 50
        y17 += 50
        y18 += 50
        y19 += 50
        y20 += 50

    # snowman61-snowman68
    y1 = 302
    y2 = 312
    y3 = 312
    y4 = 306
    y5 = 312
    y6 = 327
    y7 = 316
    y8 = 316
    y9 = 320
    y10 = 320
    y11 = 318
    y12 = 323
    y13 = 322
    y14 = 330
    y15 = 323
    y16 = 330
    y17 = 323
    y18 = 330
    y19 = 336
    y20 = 342
    x1 = 30
    x2 = 22
    x3 = 30
    x4 = 30
    x5 = 18
    x6 = 14
    x7 = 22
    x8 = 27
    x9 = 16
    x10 = 26
    x11 = 26
    x12 = 23
    x13 = 28
    x14 = 16
    x15 = 10
    x16 = 34
    x17 = 40
    x18 = 18
    x19 = 15
    x20 = 16
    for j in range(8):
        snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
        snowman_hat_wool.filled = True
        snowman_hat_wool.fill_color = 'white'
        window.add(snowman_hat_wool)
        snowman_hat = GPolygon()
        snowman_hat.add_vertex((x2, y2))
        snowman_hat.add_vertex((x3, y3))
        snowman_hat.add_vertex((x4, y4))
        snowman_hat.filled = True
        snowman_hat.fill_color = 'red'
        window.add(snowman_hat)
        snowman_face = GOval(14, 14, x=x5, y=y5)
        snowman_face.filled = True
        snowman_face.fill_color = 'white'
        window.add(snowman_face)
        snowman_body = GOval(22, 22, x=x6, y=y6)
        snowman_body.filled = True
        snowman_body.fill_color = 'white'
        window.add(snowman_body)
        snowman_leye = GOval(1, 1, x=x7, y=y7)
        snowman_leye.filled = True
        snowman_leye.fill_color = 'black'
        window.add(snowman_leye)
        snowman_reye = GOval(1, 1, x=x8, y=y8)
        snowman_reye.filled = True
        snowman_reye.fill_color = 'black'
        window.add(snowman_reye)
        snowman_nose = GPolygon()
        snowman_nose.add_vertex((x9, y9))
        snowman_nose.add_vertex((x10, y10))
        snowman_nose.add_vertex((x11, y11))
        snowman_nose.filled = True
        snowman_nose.fill_color = 'orange'
        window.add(snowman_nose)
        snowman_mouth = GLine(x12, y12, x13, y13)
        window.add(snowman_mouth)
        snowman_lhand = GLine(x14, y14, x15, y15)
        window.add(snowman_lhand)
        snowman_rhand = GLine(x16, y16, x17, y17)
        window.add(snowman_rhand)
        snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
        snowman_cloth1.filled = True
        snowman_cloth1.fill_color = 'red'
        snowman_cloth1.color = 'red'
        window.add(snowman_cloth1)
        snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
        snowman_cloth2.filled = True
        snowman_cloth2.fill_color = 'red'
        snowman_cloth2.color = 'red'
        window.add(snowman_cloth2)
        snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
        snowman_cloth3.filled = True
        snowman_cloth3.fill_color = 'red'
        snowman_cloth3.color = 'red'
        window.add(snowman_cloth3)
        x1 += 50
        x2 += 50
        x3 += 50
        x4 += 50
        x5 += 50
        x6 += 50
        x7 += 50
        x8 += 50
        x9 += 50
        x10 += 50
        x11 += 50
        x12 += 50
        x13 += 50
        x14 += 50
        x15 += 50
        x16 += 50
        x17 += 50
        x18 += 50
        x19 += 50
        x20 += 50

    # snowman70
    snowman70_hat_wool = GOval(4, 4, x=480, y=302)
    snowman70_hat_wool.filled = True
    snowman70_hat_wool.fill_color = 'white'
    window.add(snowman70_hat_wool)
    snowman70_hat = GPolygon()
    snowman70_hat.add_vertex((472, 312))
    snowman70_hat.add_vertex((480, 312))
    snowman70_hat.add_vertex((480, 306))
    snowman70_hat.filled = True
    snowman70_hat.fill_color = 'red'
    window.add(snowman70_hat)
    snowman70_face = GOval(14, 14, x=468, y=312)
    snowman70_face.filled = True
    snowman70_face.fill_color = 'white'
    window.add(snowman70_face)
    snowman70_body = GOval(22, 22, x=464, y=327)
    snowman70_body.filled = True
    snowman70_body.fill_color = 'white'
    window.add(snowman70_body)
    snowman70_leye = GOval(1, 1, x=472, y=316)
    snowman70_leye.filled = True
    snowman70_leye.fill_color = 'black'
    window.add(snowman70_leye)
    snowman70_reye = GOval(1, 1, x=477, y=316)
    snowman70_reye.filled = True
    snowman70_reye.fill_color = 'black'
    window.add(snowman70_reye)
    snowman70_nose = GPolygon()
    snowman70_nose.add_vertex((466, 320))
    snowman70_nose.add_vertex((476, 320))
    snowman70_nose.add_vertex((476, 318))
    snowman70_nose.filled = True
    snowman70_nose.fill_color = 'orange'
    window.add(snowman70_nose)
    snowman70_mouth = GLine(473, 323, 478, 322)
    window.add(snowman70_mouth)
    snowman70_lhand = GLine(466, 330, 460, 323)
    window.add(snowman70_lhand)
    snowman70_rhand = GLine(484, 330, 490, 323)
    window.add(snowman70_rhand)
    snowman70_cloth1 = GRect(14, 2, x=468, y=330)
    snowman70_cloth1.filled = True
    snowman70_cloth1.fill_color = 'red'
    snowman70_cloth1.color = 'red'
    window.add(snowman70_cloth1)
    snowman70_cloth2 = GRect(20, 2, x=465, y=336)
    snowman70_cloth2.filled = True
    snowman70_cloth2.fill_color = 'red'
    snowman70_cloth2.color = 'red'
    window.add(snowman70_cloth2)
    snowman70_cloth3 = GRect(18, 2, x=466, y=342)
    snowman70_cloth3.filled = True
    snowman70_cloth3.fill_color = 'red'
    snowman70_cloth3.color = 'red'
    window.add(snowman70_cloth3)

    # snowman71-snowman78
    y1 = 352
    y2 = 362
    y3 = 362
    y4 = 356
    y5 = 362
    y6 = 377
    y7 = 366
    y8 = 366
    y9 = 370
    y10 = 370
    y11 = 368
    y12 = 373
    y13 = 372
    y14 = 380
    y15 = 373
    y16 = 380
    y17 = 373
    y18 = 380
    y19 = 386
    y20 = 392
    x1 = 30
    x2 = 22
    x3 = 30
    x4 = 30
    x5 = 18
    x6 = 14
    x7 = 22
    x8 = 27
    x9 = 16
    x10 = 26
    x11 = 26
    x12 = 23
    x13 = 28
    x14 = 16
    x15 = 10
    x16 = 34
    x17 = 40
    x18 = 18
    x19 = 15
    x20 = 16
    for j in range(8):
        snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
        snowman_hat_wool.filled = True
        snowman_hat_wool.fill_color = 'white'
        window.add(snowman_hat_wool)
        snowman_hat = GPolygon()
        snowman_hat.add_vertex((x2, y2))
        snowman_hat.add_vertex((x3, y3))
        snowman_hat.add_vertex((x4, y4))
        snowman_hat.filled = True
        snowman_hat.fill_color = 'red'
        window.add(snowman_hat)
        snowman_face = GOval(14, 14, x=x5, y=y5)
        snowman_face.filled = True
        snowman_face.fill_color = 'white'
        window.add(snowman_face)
        snowman_body = GOval(22, 22, x=x6, y=y6)
        snowman_body.filled = True
        snowman_body.fill_color = 'white'
        window.add(snowman_body)
        snowman_leye = GOval(1, 1, x=x7, y=y7)
        snowman_leye.filled = True
        snowman_leye.fill_color = 'black'
        window.add(snowman_leye)
        snowman_reye = GOval(1, 1, x=x8, y=y8)
        snowman_reye.filled = True
        snowman_reye.fill_color = 'black'
        window.add(snowman_reye)
        snowman_nose = GPolygon()
        snowman_nose.add_vertex((x9, y9))
        snowman_nose.add_vertex((x10, y10))
        snowman_nose.add_vertex((x11, y11))
        snowman_nose.filled = True
        snowman_nose.fill_color = 'orange'
        window.add(snowman_nose)
        snowman_mouth = GLine(x12, y12, x13, y13)
        window.add(snowman_mouth)
        snowman_lhand = GLine(x14, y14, x15, y15)
        window.add(snowman_lhand)
        snowman_rhand = GLine(x16, y16, x17, y17)
        window.add(snowman_rhand)
        snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
        snowman_cloth1.filled = True
        snowman_cloth1.fill_color = 'red'
        snowman_cloth1.color = 'red'
        window.add(snowman_cloth1)
        snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
        snowman_cloth2.filled = True
        snowman_cloth2.fill_color = 'red'
        snowman_cloth2.color = 'red'
        window.add(snowman_cloth2)
        snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
        snowman_cloth3.filled = True
        snowman_cloth3.fill_color = 'red'
        snowman_cloth3.color = 'red'
        window.add(snowman_cloth3)
        x1 += 50
        x2 += 50
        x3 += 50
        x4 += 50
        x5 += 50
        x6 += 50
        x7 += 50
        x8 += 50
        x9 += 50
        x10 += 50
        x11 += 50
        x12 += 50
        x13 += 50
        x14 += 50
        x15 += 50
        x16 += 50
        x17 += 50
        x18 += 50
        x19 += 50
        x20 += 50

    # snowman80
    snowman80_hat_wool = GOval(4, 4, x=480, y=352)
    snowman80_hat_wool.filled = True
    snowman80_hat_wool.fill_color = 'white'
    window.add(snowman80_hat_wool)
    snowman80_hat = GPolygon()
    snowman80_hat.add_vertex((472, 362))
    snowman80_hat.add_vertex((480, 362))
    snowman80_hat.add_vertex((480, 356))
    snowman80_hat.filled = True
    snowman80_hat.fill_color = 'red'
    window.add(snowman80_hat)
    snowman80_face = GOval(14, 14, x=468, y=362)
    snowman80_face.filled = True
    snowman80_face.fill_color = 'white'
    window.add(snowman80_face)
    snowman80_body = GOval(22, 22, x=464, y=377)
    snowman80_body.filled = True
    snowman80_body.fill_color = 'white'
    window.add(snowman80_body)
    snowman80_leye = GOval(1, 1, x=472, y=366)
    snowman80_leye.filled = True
    snowman80_leye.fill_color = 'black'
    window.add(snowman80_leye)
    snowman80_reye = GOval(1, 1, x=477, y=366)
    snowman80_reye.filled = True
    snowman80_reye.fill_color = 'black'
    window.add(snowman80_reye)
    snowman80_nose = GPolygon()
    snowman80_nose.add_vertex((466, 370))
    snowman80_nose.add_vertex((476, 370))
    snowman80_nose.add_vertex((476, 368))
    snowman80_nose.filled = True
    snowman80_nose.fill_color = 'orange'
    window.add(snowman80_nose)
    snowman80_mouth = GLine(473, 373, 478, 372)
    window.add(snowman80_mouth)
    snowman80_lhand = GLine(466, 380, 460, 373)
    window.add(snowman80_lhand)
    snowman80_rhand = GLine(484, 380, 490, 373)
    window.add(snowman80_rhand)
    snowman80_cloth1 = GRect(14, 2, x=468, y=380)
    snowman80_cloth1.filled = True
    snowman80_cloth1.fill_color = 'red'
    snowman80_cloth1.color = 'red'
    window.add(snowman80_cloth1)
    snowman80_cloth2 = GRect(20, 2, x=465, y=386)
    snowman80_cloth2.filled = True
    snowman80_cloth2.fill_color = 'red'
    snowman80_cloth2.color = 'red'
    window.add(snowman80_cloth2)
    snowman80_cloth3 = GRect(18, 2, x=466, y=392)
    snowman80_cloth3.filled = True
    snowman80_cloth3.fill_color = 'red'
    snowman80_cloth3.color = 'red'
    window.add(snowman80_cloth3)

    # snowman81-snowman88
    y1 = 402
    y2 = 412
    y3 = 412
    y4 = 406
    y5 = 412
    y6 = 427
    y7 = 416
    y8 = 416
    y9 = 420
    y10 = 420
    y11 = 418
    y12 = 423
    y13 = 422
    y14 = 430
    y15 = 423
    y16 = 430
    y17 = 423
    y18 = 430
    y19 = 436
    y20 = 442
    x1 = 30
    x2 = 22
    x3 = 30
    x4 = 30
    x5 = 18
    x6 = 14
    x7 = 22
    x8 = 27
    x9 = 16
    x10 = 26
    x11 = 26
    x12 = 23
    x13 = 28
    x14 = 16
    x15 = 10
    x16 = 34
    x17 = 40
    x18 = 18
    x19 = 15
    x20 = 16
    for j in range(8):
        snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
        snowman_hat_wool.filled = True
        snowman_hat_wool.fill_color = 'white'
        window.add(snowman_hat_wool)
        snowman_hat = GPolygon()
        snowman_hat.add_vertex((x2, y2))
        snowman_hat.add_vertex((x3, y3))
        snowman_hat.add_vertex((x4, y4))
        snowman_hat.filled = True
        snowman_hat.fill_color = 'red'
        window.add(snowman_hat)
        snowman_face = GOval(14, 14, x=x5, y=y5)
        snowman_face.filled = True
        snowman_face.fill_color = 'white'
        window.add(snowman_face)
        snowman_body = GOval(22, 22, x=x6, y=y6)
        snowman_body.filled = True
        snowman_body.fill_color = 'white'
        window.add(snowman_body)
        snowman_leye = GOval(1, 1, x=x7, y=y7)
        snowman_leye.filled = True
        snowman_leye.fill_color = 'black'
        window.add(snowman_leye)
        snowman_reye = GOval(1, 1, x=x8, y=y8)
        snowman_reye.filled = True
        snowman_reye.fill_color = 'black'
        window.add(snowman_reye)
        snowman_nose = GPolygon()
        snowman_nose.add_vertex((x9, y9))
        snowman_nose.add_vertex((x10, y10))
        snowman_nose.add_vertex((x11, y11))
        snowman_nose.filled = True
        snowman_nose.fill_color = 'orange'
        window.add(snowman_nose)
        snowman_mouth = GLine(x12, y12, x13, y13)
        window.add(snowman_mouth)
        snowman_lhand = GLine(x14, y14, x15, y15)
        window.add(snowman_lhand)
        snowman_rhand = GLine(x16, y16, x17, y17)
        window.add(snowman_rhand)
        snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
        snowman_cloth1.filled = True
        snowman_cloth1.fill_color = 'red'
        snowman_cloth1.color = 'red'
        window.add(snowman_cloth1)
        snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
        snowman_cloth2.filled = True
        snowman_cloth2.fill_color = 'red'
        snowman_cloth2.color = 'red'
        window.add(snowman_cloth2)
        snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
        snowman_cloth3.filled = True
        snowman_cloth3.fill_color = 'red'
        snowman_cloth3.color = 'red'
        window.add(snowman_cloth3)
        x1 += 50
        x2 += 50
        x3 += 50
        x4 += 50
        x5 += 50
        x6 += 50
        x7 += 50
        x8 += 50
        x9 += 50
        x10 += 50
        x11 += 50
        x12 += 50
        x13 += 50
        x14 += 50
        x15 += 50
        x16 += 50
        x17 += 50
        x18 += 50
        x19 += 50
        x20 += 50

    # snowman90
    snowman90_hat_wool = GOval(4, 4, x=480, y=402)
    snowman90_hat_wool.filled = True
    snowman90_hat_wool.fill_color = 'white'
    window.add(snowman90_hat_wool)
    snowman90_hat = GPolygon()
    snowman90_hat.add_vertex((472, 412))
    snowman90_hat.add_vertex((480, 412))
    snowman90_hat.add_vertex((480, 406))
    snowman90_hat.filled = True
    snowman90_hat.fill_color = 'red'
    window.add(snowman90_hat)
    snowman90_face = GOval(14, 14, x=468, y=412)
    snowman90_face.filled = True
    snowman90_face.fill_color = 'white'
    window.add(snowman90_face)
    snowman90_body = GOval(22, 22, x=464, y=427)
    snowman90_body.filled = True
    snowman90_body.fill_color = 'white'
    window.add(snowman90_body)
    snowman90_leye = GOval(1, 1, x=472, y=416)
    snowman90_leye.filled = True
    snowman90_leye.fill_color = 'black'
    window.add(snowman90_leye)
    snowman90_reye = GOval(1, 1, x=477, y=416)
    snowman90_reye.filled = True
    snowman90_reye.fill_color = 'black'
    window.add(snowman90_reye)
    snowman90_nose = GPolygon()
    snowman90_nose.add_vertex((466, 420))
    snowman90_nose.add_vertex((476, 420))
    snowman90_nose.add_vertex((476, 418))
    snowman90_nose.filled = True
    snowman90_nose.fill_color = 'orange'
    window.add(snowman90_nose)
    snowman90_mouth = GLine(473, 423, 478, 422)
    window.add(snowman90_mouth)
    snowman90_lhand = GLine(466, 430, 460, 423)
    window.add(snowman90_lhand)
    snowman90_rhand = GLine(484, 430, 490, 423)
    window.add(snowman90_rhand)
    snowman90_cloth1 = GRect(14, 2, x=468, y=430)
    snowman90_cloth1.filled = True
    snowman90_cloth1.fill_color = 'red'
    snowman90_cloth1.color = 'red'
    window.add(snowman90_cloth1)
    snowman90_cloth2 = GRect(20, 2, x=465, y=436)
    snowman90_cloth2.filled = True
    snowman90_cloth2.fill_color = 'red'
    snowman90_cloth2.color = 'red'
    window.add(snowman90_cloth2)
    snowman90_cloth3 = GRect(18, 2, x=466, y=442)
    snowman90_cloth3.filled = True
    snowman90_cloth3.fill_color = 'red'
    snowman90_cloth3.color = 'red'
    window.add(snowman90_cloth3)

    # snowman91-snowman100
    y1 = 452
    y2 = 462
    y3 = 462
    y4 = 456
    y5 = 462
    y6 = 477
    y7 = 466
    y8 = 466
    y9 = 470
    y10 = 470
    y11 = 468
    y12 = 473
    y13 = 472
    y14 = 480
    y15 = 473
    y16 = 480
    y17 = 473
    y18 = 480
    y19 = 486
    y20 = 492
    x1 = 30
    x2 = 22
    x3 = 30
    x4 = 30
    x5 = 18
    x6 = 14
    x7 = 22
    x8 = 27
    x9 = 16
    x10 = 26
    x11 = 26
    x12 = 23
    x13 = 28
    x14 = 16
    x15 = 10
    x16 = 34
    x17 = 40
    x18 = 18
    x19 = 15
    x20 = 16
    for j in range(10):
        snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
        snowman_hat_wool.filled = True
        snowman_hat_wool.fill_color = 'white'
        window.add(snowman_hat_wool)
        snowman_hat = GPolygon()
        snowman_hat.add_vertex((x2, y2))
        snowman_hat.add_vertex((x3, y3))
        snowman_hat.add_vertex((x4, y4))
        snowman_hat.filled = True
        snowman_hat.fill_color = 'red'
        window.add(snowman_hat)
        snowman_face = GOval(14, 14, x=x5, y=y5)
        snowman_face.filled = True
        snowman_face.fill_color = 'white'
        window.add(snowman_face)
        snowman_body = GOval(22, 22, x=x6, y=y6)
        snowman_body.filled = True
        snowman_body.fill_color = 'white'
        window.add(snowman_body)
        snowman_leye = GOval(1, 1, x=x7, y=y7)
        snowman_leye.filled = True
        snowman_leye.fill_color = 'black'
        window.add(snowman_leye)
        snowman_reye = GOval(1, 1, x=x8, y=y8)
        snowman_reye.filled = True
        snowman_reye.fill_color = 'black'
        window.add(snowman_reye)
        snowman_nose = GPolygon()
        snowman_nose.add_vertex((x9, y9))
        snowman_nose.add_vertex((x10, y10))
        snowman_nose.add_vertex((x11, y11))
        snowman_nose.filled = True
        snowman_nose.fill_color = 'orange'
        window.add(snowman_nose)
        snowman_mouth = GLine(x12, y12, x13, y13)
        window.add(snowman_mouth)
        snowman_lhand = GLine(x14, y14, x15, y15)
        window.add(snowman_lhand)
        snowman_rhand = GLine(x16, y16, x17, y17)
        window.add(snowman_rhand)
        snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
        snowman_cloth1.filled = True
        snowman_cloth1.fill_color = 'red'
        snowman_cloth1.color = 'red'
        window.add(snowman_cloth1)
        snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
        snowman_cloth2.filled = True
        snowman_cloth2.fill_color = 'red'
        snowman_cloth2.color = 'red'
        window.add(snowman_cloth2)
        snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
        snowman_cloth3.filled = True
        snowman_cloth3.fill_color = 'red'
        snowman_cloth3.color = 'red'
        window.add(snowman_cloth3)
        x1 += 50
        x2 += 50
        x3 += 50
        x4 += 50
        x5 += 50
        x6 += 50
        x7 += 50
        x8 += 50
        x9 += 50
        x10 += 50
        x11 += 50
        x12 += 50
        x13 += 50
        x14 += 50
        x15 += 50
        x16 += 50
        x17 += 50
        x18 += 50
        x19 += 50
        x20 += 50

    # inner snowman1-snowman81
    y1 = 27
    y2 = 37
    y3 = 37
    y4 = 31
    y5 = 37
    y6 = 52
    y7 = 41
    y8 = 41
    y9 = 45
    y10 = 45
    y11 = 43
    y12 = 48
    y13 = 47
    y14 = 55
    y15 = 48
    y16 = 55
    y17 = 48
    y18 = 55
    y19 = 61
    y20 = 67
    for i in range(9):
        x1 = 55
        x2 = 47
        x3 = 55
        x4 = 55
        x5 = 43
        x6 = 39
        x7 = 47
        x8 = 52
        x9 = 41
        x10 = 51
        x11 = 51
        x12 = 48
        x13 = 53
        x14 = 41
        x15 = 35
        x16 = 59
        x17 = 65
        x18 = 43
        x19 = 40
        x20 = 41
        for j in range(9):
            snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
            snowman_hat_wool.filled = True
            snowman_hat_wool.fill_color = 'white'
            window.add(snowman_hat_wool)
            snowman_hat = GPolygon()
            snowman_hat.add_vertex((x2, y2))
            snowman_hat.add_vertex((x3, y3))
            snowman_hat.add_vertex((x4, y4))
            snowman_hat.filled = True
            snowman_hat.fill_color = 'deepskyblue'
            window.add(snowman_hat)
            snowman_face = GOval(14, 14, x=x5, y=y5)
            snowman_face.filled = True
            snowman_face.fill_color = 'white'
            window.add(snowman_face)
            snowman_body = GOval(22, 22, x=x6, y=y6)
            snowman_body.filled = True
            snowman_body.fill_color = 'white'
            window.add(snowman_body)
            snowman_leye = GOval(1, 1, x=x7, y=y7)
            snowman_leye.filled = True
            snowman_leye.fill_color = 'black'
            window.add(snowman_leye)
            snowman_reye = GOval(1, 1, x=x8, y=y8)
            snowman_reye.filled = True
            snowman_reye.fill_color = 'black'
            window.add(snowman_reye)
            snowman_nose = GPolygon()
            snowman_nose.add_vertex((x9, y9))
            snowman_nose.add_vertex((x10, y10))
            snowman_nose.add_vertex((x11, y11))
            snowman_nose.filled = True
            snowman_nose.fill_color = 'orange'
            window.add(snowman_nose)
            snowman_mouth = GLine(x12, y12, x13, y13)
            window.add(snowman_mouth)
            snowman_lhand = GLine(x14, y14, x15, y15)
            window.add(snowman_lhand)
            snowman_rhand = GLine(x16, y16, x17, y17)
            window.add(snowman_rhand)
            snowman_cloth1 = GRect(14, 2, x=x18, y=y18)
            snowman_cloth1.filled = True
            snowman_cloth1.fill_color = 'deepskyblue'
            snowman_cloth1.color = 'deepskyblue'
            window.add(snowman_cloth1)
            snowman_cloth2 = GRect(20, 2, x=x19, y=y19)
            snowman_cloth2.filled = True
            snowman_cloth2.fill_color = 'deepskyblue'
            snowman_cloth2.color = 'deepskyblue'
            window.add(snowman_cloth2)
            snowman_cloth3 = GRect(18, 2, x=x20, y=y20)
            snowman_cloth3.filled = True
            snowman_cloth3.fill_color = 'deepskyblue'
            snowman_cloth3.color = 'deepskyblue'
            window.add(snowman_cloth3)
            x1 += 50
            x2 += 50
            x3 += 50
            x4 += 50
            x5 += 50
            x6 += 50
            x7 += 50
            x8 += 50
            x9 += 50
            x10 += 50
            x11 += 50
            x12 += 50
            x13 += 50
            x14 += 50
            x15 += 50
            x16 += 50
            x17 += 50
            x18 += 50
            x19 += 50
            x20 += 50
        y1 += 50
        y2 += 50
        y3 += 50
        y4 += 50
        y5 += 50
        y6 += 50
        y7 += 50
        y8 += 50
        y9 += 50
        y10 += 50
        y11 += 50
        y12 += 50
        y13 += 50
        y14 += 50
        y15 += 50
        y16 += 50
        y17 += 50
        y18 += 50
        y19 += 50
        y20 += 50

    # snowman faces
    y1 = 2
    y2 = 12
    y3 = 12
    y4 = 6
    y5 = 12
    y7 = 16
    y8 = 16
    y9 = 20
    y10 = 20
    y11 = 18
    y12 = 23
    y13 = 22
    for i in range(2):
        x1 = 55
        x2 = 47
        x3 = 55
        x4 = 55
        x5 = 43
        x7 = 47
        x8 = 52
        x9 = 41
        x10 = 51
        x11 = 51
        x12 = 48
        x13 = 53
        for j in range(9):
            snowman_hat_wool = GOval(4, 4, x=x1, y=y1)
            snowman_hat_wool.filled = True
            snowman_hat_wool.fill_color = 'white'
            window.add(snowman_hat_wool)
            snowman_hat = GPolygon()
            snowman_hat.add_vertex((x2, y2))
            snowman_hat.add_vertex((x3, y3))
            snowman_hat.add_vertex((x4, y4))
            snowman_hat.filled = True
            snowman_hat.fill_color = 'red'
            window.add(snowman_hat)
            snowman_face = GOval(14, 14, x=x5, y=y5)
            snowman_face.filled = True
            snowman_face.fill_color = 'white'
            window.add(snowman_face)
            snowman_leye = GOval(1, 1, x=x7, y=y7)
            snowman_leye.filled = True
            snowman_leye.fill_color = 'black'
            window.add(snowman_leye)
            snowman_reye = GOval(1, 1, x=x8, y=y8)
            snowman_reye.filled = True
            snowman_reye.fill_color = 'black'
            window.add(snowman_reye)
            snowman_nose = GPolygon()
            snowman_nose.add_vertex((x9, y9))
            snowman_nose.add_vertex((x10, y10))
            snowman_nose.add_vertex((x11, y11))
            snowman_nose.filled = True
            snowman_nose.fill_color = 'orange'
            window.add(snowman_nose)
            snowman_mouth = GLine(x12, y12, x13, y13)
            window.add(snowman_mouth)
            x1 += 50
            x2 += 50
            x3 += 50
            x4 += 50
            x5 += 50
            x7 += 50
            x8 += 50
            x9 += 50
            x10 += 50
            x11 += 50
            x12 += 50
            x13 += 50
        y1 += 480
        y2 += 480
        y3 += 480
        y4 += 480
        y5 += 480
        y7 += 480
        y8 += 480
        y9 += 480
        y10 += 480
        y11 += 480
        y12 += 480
        y13 += 480

    # WALLY's face
    face1 = GPolygon()
    face1.add_vertex((410, 330))
    face1.add_vertex((420, 330))
    face1.add_vertex((420, 360))
    face1.filled = True
    face1.fill_color = 'papayawhip'
    face1.color = 'papayawhip'
    window.add(face1)
    face2 = GRect(10, 30, x=420, y=330)
    face2.filled = True
    face2.fill_color = 'papayawhip'
    face2.color = 'papayawhip'
    window.add(face2)
    face3 = GPolygon()
    face3.add_vertex((430, 330))
    face3.add_vertex((440, 330))
    face3.add_vertex((430, 360))
    face3.filled = True
    face3.fill_color = 'papayawhip'
    face3.color = 'papayawhip'
    window.add(face3)
    line1 = GLine(410, 330, 420, 360)
    window.add(line1)
    line2 = GLine(440, 330, 430, 360)
    window.add(line2)
    line3 = GLine(420, 360, 430, 360)
    window.add(line3)

    # WALLY's neck
    neck = GRect(6, 4, x=422, y=360)
    neck.filled = True
    neck.fill_color = 'papayawhip'
    window.add(neck)

    # WALLY's glasses
    line = GLine(415, 342, 437, 342)
    window.add(line)
    circle_l = GOval(9, 9, x=415, y=338)
    circle_l.filled = True
    circle_l.fill_color = 'white'
    window.add(circle_l)
    circle_r = GOval(9, 9, x=426, y=338)
    circle_r.filled = True
    circle_r.fill_color = 'white'
    window.add(circle_r)

    # WALLY's eye
    eye_l = GOval(2, 2, x=419, y=341)
    eye_l.filled = True
    window.add(eye_l)
    eye_r = GOval(2, 2, x=429, y=341)
    eye_r.filled = True
    window.add(eye_r)

    # WALLY's nose
    nose = GLine(424, 348, 427, 348)
    window.add(nose)

    # WALLY's mouth
    mouth1 = GLine(420, 350, 425, 353)
    window.add(mouth1)
    mouth2 = GLine(430, 350, 424, 353)
    window.add(mouth2)

    # WALLY's ear
    ear_l = GPolygon()
    ear_l.add_vertex((415, 342))
    ear_l.add_vertex((411, 342))
    ear_l.add_vertex((416, 350))
    ear_l.filled = True
    ear_l.fill_color = 'papayawhip'
    window.add(ear_l)
    ear_r = GPolygon()
    ear_r.add_vertex((437, 342))
    ear_r.add_vertex((441, 342))
    ear_r.add_vertex((433, 350))
    ear_r.filled = True
    ear_r.fill_color = 'papayawhip'
    window.add(ear_r)

    # WALLY's hand
    hand_l = GOval(8, 8, x=407, y=399)
    hand_l.filled = True
    hand_l.fill_color = 'papayawhip'
    window.add(hand_l)
    hand_r = GOval(8, 8, x=435, y=399)
    hand_r.filled = True
    hand_r.fill_color = 'papayawhip'
    window.add(hand_r)

    # WALLY's clothes
    middle_clothes = GRect(20, 30, x=415, y=364)
    middle_clothes.filled = True
    middle_clothes.fill_color = 'white'
    middle_clothes.color = 'white'
    window.add(middle_clothes)
    left_clothes = GRect(8, 35, x=407, y=364)
    left_clothes.filled = True
    left_clothes.fill_color = 'white'
    left_clothes.color = 'white'
    window.add(left_clothes)
    right_clothes = GRect(8, 35, x=435, y=364)
    right_clothes.filled = True
    right_clothes.fill_color = 'white'
    right_clothes.color = 'white'
    window.add(right_clothes)
    red1 = GRect(36, 2, x=407, y=368)
    red1.filled = True
    red1.fill_color = 'red'
    red1.color = 'red'
    window.add(red1)
    red2 = GRect(36, 2, x=407, y=374)
    red2.filled = True
    red2.fill_color = 'red'
    red2.color = 'red'
    window.add(red2)
    red3 = GRect(36, 2, x=407, y=380)
    red3.filled = True
    red3.fill_color = 'red'
    red3.color = 'red'
    window.add(red3)
    red4 = GRect(36, 2, x=407, y=386)
    red4.filled = True
    red4.fill_color = 'red'
    red4.color = 'red'
    window.add(red4)
    red5 = GRect(36, 2, x=407, y=392)
    red5.filled = True
    red5.fill_color = 'red'
    red5.color = 'red'
    window.add(red5)
    cloth1 = GLine(407, 364, 407, 399)
    window.add(cloth1)
    cloth2 = GLine(443, 364, 443, 399)
    window.add(cloth2)
    cloth3 = GLine(407, 364, 443, 364)
    window.add(cloth3)
    cloth4 = GLine(407, 399, 415, 399)
    window.add(cloth4)
    cloth5 = GLine(435, 399, 443, 399)
    window.add(cloth5)
    cloth6 = GLine(415, 374, 415, 399)
    window.add(cloth6)
    cloth7 = GLine(435, 374, 435, 399)
    window.add(cloth7)
    cloth8 = GLine(415, 394, 435, 394)
    window.add(cloth8)

    # WALLY's pants
    left_pants = GRect(10, 45, x=415, y=394)
    left_pants.filled = True
    left_pants.fill_color = 'deepskyblue'
    window.add(left_pants)
    left_pants_line = GLine(420, 394, 415, 400)
    window.add(left_pants_line)
    right_pants = GRect(10, 45, x=425, y=394)
    right_pants.filled = True
    right_pants.fill_color = 'deepskyblue'
    window.add(right_pants)
    right_pants_line = GLine(430, 394, 435, 400)
    window.add(right_pants_line)
    zipper = GOval(2, 10, x=424, y=394)
    zipper.filled = True
    zipper.fill_color = 'dodgerblue'
    window.add(zipper)

    # WALLY's shoes
    left_shoes1 = GRect(9, 7, x=415, y=440)
    left_shoes1.filled = True
    left_shoes1.fill_color = 'saddlebrown'
    left_shoes1.color = 'saddlebrown'
    window.add(left_shoes1)
    left_shoes2 = GPolygon()
    left_shoes2.add_vertex((415, 440))
    left_shoes2.add_vertex((415, 447))
    left_shoes2.add_vertex((410, 447))
    left_shoes2.filled = True
    left_shoes2.fill_color = 'saddlebrown'
    left_shoes2.color = 'saddlebrown'
    window.add(left_shoes2)
    left_shoes_line1 = GLine(415, 440, 410, 447)
    window.add(left_shoes_line1)
    left_shoes_line2 = GLine(410, 447, 424, 447)
    window.add(left_shoes_line2)
    left_shoes_line3 = GLine(424, 440, 424, 447)
    window.add(left_shoes_line3)
    left_shoes_line4 = GLine(412, 445, 424, 445)
    window.add(left_shoes_line4)
    right_shoes1 = GRect(9, 7, x=426, y=440)
    right_shoes1.filled = True
    right_shoes1.fill_color = 'saddlebrown'
    right_shoes1.color = 'saddlebrown'
    window.add(right_shoes1)
    right_shoes2 = GPolygon()
    right_shoes2.add_vertex((435, 440))
    right_shoes2.add_vertex((435, 447))
    right_shoes2.add_vertex((440, 447))
    right_shoes2.filled = True
    right_shoes2.fill_color = 'saddlebrown'
    right_shoes2.color = 'saddlebrown'
    window.add(right_shoes2)
    right_shoes_line1 = GLine(435, 440, 440, 447)
    window.add(right_shoes_line1)
    right_shoes_line2 = GLine(426, 447, 440, 447)
    window.add(right_shoes_line2)
    right_shoes_line3 = GLine(426, 440, 426, 447)
    window.add(right_shoes_line3)
    right_shoes_line4 = GLine(426, 445, 438, 445)
    window.add(right_shoes_line4)

    # WALLY's hat
    hat_wool = GOval(10, 10, x=410, y=310)
    hat_wool.filled = True
    hat_wool.fill_color = 'red'
    hat_wool.color = 'white'
    window.add(hat_wool)
    wool_1 = GLine(410, 310, 413, 313)
    window.add(wool_1)
    wool_2 = GLine(415, 309, 415, 312)
    window.add(wool_2)
    wool_3 = GLine(420, 310, 417, 313)
    window.add(wool_3)
    wool_4 = GLine(422, 315, 419, 315)
    window.add(wool_4)
    wool_5 = GLine(420, 320, 417, 318)
    window.add(wool_5)
    wool_6 = GLine(415, 320, 415, 323)
    window.add(wool_6)
    wool_7 = GLine(410, 320, 413, 318)
    window.add(wool_7)
    wool_8 = GLine(411, 315, 408, 315)
    window.add(wool_8)
    hat1 = GPolygon()
    hat1.add_vertex((415, 318))
    hat1.add_vertex((410, 325))
    hat1.add_vertex((435, 325))
    hat1.filled = True
    hat1.fill_color = 'white'
    window.add(hat1)
    hat2 = GRect(25, 5, x=410, y=325)
    hat2.filled = True
    hat2.fill_color = 'red'
    window.add(hat2)

    # WALLY's hair
    hair1 = GOval(25, 2, x=415, y=330)
    hair1.filled = True
    hair1.fill_color = 'rosybrown'
    window.add(hair1)
    hair2 = GOval(25, 2, x=415, y=332)
    hair2.filled = True
    hair2.fill_color = 'rosybrown'
    window.add(hair2)
    hair3 = GOval(25, 2, x=415, y=334)
    hair3.filled = True
    hair3.fill_color = 'rosybrown'
    window.add(hair3)
    hair4 = GPolygon()
    hair4.add_vertex((410, 330))
    hair4.add_vertex((412, 330))
    hair4.add_vertex((411, 338))
    hair4.filled = True
    hair4.fill_color = 'rosybrown'
    window.add(hair4)
    hair5 = GPolygon()
    hair5.add_vertex((413, 330))
    hair5.add_vertex((415, 330))
    hair5.add_vertex((414, 338))
    hair5.filled = True
    hair5.fill_color = 'rosybrown'
    window.add(hair5)


if __name__ == '__main__':
    main()
