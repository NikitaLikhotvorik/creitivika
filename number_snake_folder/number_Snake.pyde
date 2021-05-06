dict_int = {'score':0,'start':False,'shop':False}
dict_const = {'gran_left':0,'gran_right':600,'snake.scroll_tail_Y':3,'snake.move_to_palette_X':400,'snake.move_to_palette_Y':100,'gran_left_palette_line':50,'gran_right_palette_line':305,'palette_Y_line':50}
dict_const_fill = {'button_LEFT_RIGHT_palette':125,'text_LEFT_RIGHT_palette':0}
dict_const_stroke = {'line_palette1':125,'line_palette2':255,'button_collor_green_pallete':[0,255,0],'button_collor_red_pallete':[255,0,0],'button_palette':0,'RGB_palette':255}
dict_const_strokeWeight = {'line_palette':5,'button_palette':1}
dict_const_rect = {'button_collor_pallete':[50,200,50,50],'button_LEFT_palette':[50,400,25,50],'button_RIGHT_palette':[80,400,25,50],'list_fill':[50,480,55,55]}
dict_const_triangle = {'i':0}
dict_const_ellipse = {'i':0}
dict_const_text = {'RIGHT_paletter':[92.5,440],'LEFT_paletter':[62.5,440]}
dict_const_textSize = {'LEFT_RIGHT_palette':30,'RGB_palette':30}
class button_shop():
    def __init__(self):
        self.snake_X = 300
        self.snake_Y = 100
        self.speed_snake = 2
        self.fill_ = []
        for i in range(3):
            self.fill_.append([])
            for j in range(3):
                for h in range(3):
                    self.fill_[len(self.fill_)-1].append(random(0,255))
        self.str_ = 0
    def draw_(self):
        #рисуем змейку
        snake.draw_()
        snake.scroll_tail_Y(dict_const['snake.scroll_tail_Y'])
        #переносим голову змейки в верх экрана
        snake.move_to(self.snake_X,self.snake_Y)
        if self.snake_X >= 350:
            self.speed_snake = -2
        if self.snake_X <= 250:
            self.speed_snake = 2
        self.snake_X += self.speed_snake
        for i in range(3):
            for j in range(3):
                fill(self.fill_[self.str_*3][i],self.fill_[self.str_*3][i],self.fill_[self.str_*3][i])
                rect(100*i+175,100*j+400,75,75)
class button_palette():
    def __init__(self):
        self.x = [175,175,175]
        self._fill_ = [{'R':255,'G':255,'B':255}]
        self.time = True
        self.mousePressed_time = True
        self.int_fill = 0
        self.RGB_ = ['R','G','B']
        #self.mousePressed_time_money = True
    def palette(self):
        #рисуем змейку
        snake.draw_()
        snake.scroll_tail_Y(dict_const['snake.scroll_tail_Y'])
        #переносим голову змейки в верх экрана
        snake.move_to(dict_const['snake.move_to_palette_X'],dict_const['snake.move_to_palette_Y'])
        strokeWeight(dict_const_strokeWeight['line_palette'])
        stroke(dict_const_stroke['line_palette1'])
        #рисуем рычажки управления цветом
        for i in range(1,4):
            line(dict_const['gran_left_palette_line'],dict_const['gran_left_palette_line']*i,dict_const['gran_right_palette_line'],dict_const['gran_left_palette_line']*i)
            textSize(dict_const_textSize['RGB_palette'])
            fill(dict_const_stroke['RGB_palette'])
            text(self.RGB_[i-1],dict_const['gran_left_palette_line']-20,dict_const['gran_left_palette_line']*i+15)
        for i in range(1,4):
            stroke(dict_const_stroke['line_palette2'])
            line(self.x[i-1],dict_const['palette_Y_line'] * i - 10,self.x[i-1],dict_const['palette_Y_line'] * i + 10)
        if mousePressed == True:
            for i in range(1,4):
                #управляем рычажками мышкой
                if mouseX >= dict_const['gran_left_palette_line'] and mouseX <= dict_const['gran_right_palette_line'] and mouseY > i * (50 - 16) + i * 10 and mouseY < i * (50 + 16):
                    self.x[i-1] = mouseX
                if mouseX < dict_const['gran_left_palette_line'] and mouseX > dict_const['gran_left'] and mouseY > i * (50 - 16) + i * 10 and mouseY < i * (50 + 16):
                    self.x[i-1] = dict_const['gran_left_palette_line']
                if mouseX > dict_const['gran_right_palette_line'] and mouseX < dict_const['gran_right_palette_line'] + 45 and mouseY > i * (50 - 16) + i * 10 and mouseY < i * (50 + 16):
                    self.x[i-1] = dict_const['gran_right_palette_line']
                #если нажата левая кнопка то изменяем цвет на -1
                if mouseX > dict_const_rect['button_LEFT_palette'][0]:
                    if mouseX < dict_const_rect['button_LEFT_palette'][0] + dict_const_rect['button_LEFT_palette'][2]:
                        if mouseY > dict_const_rect['button_LEFT_palette'][1]:
                            if mouseY < dict_const_rect['button_LEFT_palette'][1] + dict_const_rect['button_LEFT_palette'][3]:
                                if self.int_fill > 0 and self.mousePressed_time == True:
                                    self.int_fill -= 1
                                    self.mousePressed_time = False
                #если нажата правая кнопка то изменяем цвет на +1
                if mouseX > dict_const_rect['button_RIGHT_palette'][0]:
                    if mouseX < dict_const_rect['button_RIGHT_palette'][0] + dict_const_rect['button_RIGHT_palette'][2]:
                        if mouseY > dict_const_rect['button_RIGHT_palette'][1]:
                            if mouseY < dict_const_rect['button_RIGHT_palette'][1] + dict_const_rect['button_RIGHT_palette'][3]:
                                if self.int_fill < len(self._fill_)-1 and self.mousePressed_time == True:
                                    self.int_fill += 1
                                    self.mousePressed_time = False
            #если нажата кнопка то добавляем цвет в список
            if mouseX > 50 and mouseX < 100 and mouseY > 200 and mouseY < 250 and self.mousePressed_time == True and dict_int['score'] >= 500:
                dict_int['score'] -= 500
                self._fill_.append(dict(R = self.x[0]-dict_const['gran_left_palette_line'],G = self.x[1]-dict_const['gran_left_palette_line'],B = self.x[2]-dict_const['gran_left_palette_line']))
                self.mousePressed_time = False
                self.int_fill = len(self._fill_)-1
            #если нажимаем мышкой на кружок змейки то он меняет цвет
            snake.fill_(self._fill_[self.int_fill]['R'],self._fill_[self.int_fill]['G'],self._fill_[self.int_fill]['B'])
        else:
            self.mousePressed_time = True
        #определяем куплен цвет или нет и изменяем контур кнопки для покупки
        for i in range(len(self._fill_)):
            if self.time == True:
                if self._fill_[i]['R'] == self.x[0]-dict_const['gran_left_palette_line'] and self._fill_[i]['G'] == self.x[1]-dict_const['gran_left_palette_line'] and self._fill_[i]['B'] == self.x[2]-dict_const['gran_left_palette_line']:
                    stroke(dict_const_stroke['button_collor_green_pallete'][0],dict_const_stroke['button_collor_green_pallete'][1],dict_const_stroke['button_collor_green_pallete'][2])
                    self.time = False
                else:
                    stroke(dict_const_stroke['button_collor_red_pallete'][0],dict_const_stroke['button_collor_red_pallete'][1],dict_const_stroke['button_collor_red_pallete'][2])
        #удаляем повторяющиеся цвета
        for i in range(len(self._fill_)-1):
            for j in range(len(self._fill_)):
                if self._fill_[i] == self._fill_[j] and i != j:
                    del self._fill_[j]
                    self.int_fill -= 1
        #если в списке нет элементов то изменяем контур кнопки для покупки на красный
        if len(self._fill_) == 0:
            stroke(dict_const_stroke['button_collor_red_pallete'][0],dict_const_stroke['button_collor_red_pallete'][1],dict_const_stroke['button_collor_red_pallete'][2])
        self.time = True
        fill(self.x[0]-dict_const['gran_left_palette_line'],self.x[1]-dict_const['gran_left_palette_line'],self.x[2]-dict_const['gran_left_palette_line'])
        #рисуем кнопку покупки цветов
        rect(dict_const_rect['button_collor_pallete'][0],dict_const_rect['button_collor_pallete'][1],dict_const_rect['button_collor_pallete'][2],dict_const_rect['button_collor_pallete'][3])
        print(self._fill_)
        strokeWeight(dict_const_strokeWeight['button_palette'])
        stroke(dict_const_stroke['button_palette'])
        fill(dict_const_fill['button_LEFT_RIGHT_palette'])
        #рисуем кнопки вправо и влево
        rect(dict_const_rect['button_LEFT_palette'][0],dict_const_rect['button_LEFT_palette'][1],dict_const_rect['button_LEFT_palette'][2],dict_const_rect['button_LEFT_palette'][3])
        rect(dict_const_rect['button_RIGHT_palette'][0],dict_const_rect['button_RIGHT_palette'][1],dict_const_rect['button_RIGHT_palette'][2],dict_const_rect['button_RIGHT_palette'][3])
        fill(dict_const_fill['text_LEFT_RIGHT_palette'])
        textSize(dict_const_textSize['LEFT_RIGHT_palette'])
        #рисуем на них значки
        text('>',dict_const_text['RIGHT_paletter'][0],dict_const_text['RIGHT_paletter'][1])
        text('<',dict_const_text['LEFT_paletter'][0],dict_const_text['LEFT_paletter'][1])
        fill(self._fill_[self.int_fill]['R'],self._fill_[self.int_fill]['G'],self._fill_[self.int_fill]['B'])
        #рисуем квадрат с купленными цветами
        rect(dict_const_rect['list_fill'][0],dict_const_rect['list_fill'][1],dict_const_rect['list_fill'][2],dict_const_rect['list_fill'][3])
def button_start():
    global start,score
    snake.dlina_to(0)
    prep.recovery_prep()
    dict_int['score'] = 0
    start = 1
def button():
    fill(255,0,0)
    ellipse(300,400,200,125)
    fill(255)
    triangle(280,375,280,425,330,400)
    
    fill(0,255,0)
    rect(500,700,75,75)
    fill(0,255,0)
    strokeWeight(3)
    ellipse(537.5,730,20,20)
    strokeWeight(1)
    fill(255,0,0)
    rect(520,730,35,35)
    
    fill(0,0,255)
    rect(25,700,75,75)
    fill(0,255,0)
    ellipse(25+37.5,737.5,70,70)
    push()
    noStroke()
    fill(0,0,255)
    ellipse(25+37.5,737.5+20,15,15)
    pop()
    fill(255,0,0)
    ellipse(40,737+10,15,15)
    fill(0,0,0)
    ellipse(45,725,15,15)
    fill("#F2EB11")
    ellipse(65,715,15,15)
    fill('#3DF2BD')
    ellipse(80,732,15,15)
    fill(0,0,255)
    push()
    noStroke()
    translate(87,757)
    rotate(radians(120))
    ellipse(0,0,30,25)
    pop()
list_prep = [] 
gran_left = 0
gran_right = 600
# class Wall:
#     def __init__(self):
#         self.p = []
#         self.p_old = [] 
#     def draw_wall(self,head_X):
#         global gran_left,gran_right
#         self.graniza = 0
#         strokeWeight(10)
#         stroke("#9AECFA")
#         for i in range(len(self.p)):
#             line(self.p[i]['x'] * 120,self.p[i]['y'],self.p[i]['x'] * 120,self.p[i]['y2'])
#             if self.p[i]['y'] >= 500 and self.p[i]['y'] <= 600 and self.graniza == 0:
#                 print('1')
#                 #print('------------------------------------------------')
#                 #for gran in range(len(self.p)):
#                 if head_X < self.p[i]['x'] * 120:
#                     gran_right = self.p[i]['x'] * 120
#                     #print(gran_right)
#                 else: 
#                     gran_right = 600
#                 if head_X > self.p[i]['x'] * 120:
#                     gran_left = self.p[i]['x'] * 120
#                 else: 
#                     gran_left = 0
#                 self.graniza = 1
#             if len(self.p_old) > 0:
#                 if self.p_old[len(self.p_old)-1]['y2'] - 600 > 0 and self.p_old[len(self.p_old)-1]['y2'] - 600 < 50 and self.graniza == 1:
#                     print('2')
#                     self.graniza = 2
#                     gran_right = 600
#                     gran_left = 0
#             if prep.polog_Y() < 360 or prep.polog_Y() > 370:
#                 self.p[i]['y'] += 3
#                 self.p[i]['y2'] += 3
#         for i in range(len(self.p_old)):
#             if prep.polog_Y() < 360 or prep.polog_Y() > 370:
#                 self.p_old[i]['y'] += 3
#                 self.p_old[i]['y2'] += 3
#         if len(self.p) > 0:
#             if self.p[0]['y'] > 600:
#                 self.p_old.append(self.p[0])
#                 del self.p[0]
#         for i in range(len(self.p_old)):
#             line(self.p_old[i]['x'] * 120,self.p_old[i]['y'],self.p_old[i]['x'] * 120,self.p_old[i]['y2'])
#         stroke(0)
#     def plus_wall(self):
#         self.p.append(dict(x = floor(random(1,5)),y = -100,y2 = -200))
class Ball:
    def __init__(self):
        self.p = [dict(x = random(10,590),y = -15,num = floor(random(1,10)),gold = 0)]
    def draw_ball(self,head_X):
        for i in range(len(self.p)):
            strokeWeight(1)
            if self.p[i]['gold'] == 0:
                fill(255,0,0)
            else:
                fill('#FFF827')
            ellipse(self.p[i]['x'],self.p[i]['y'],10,10)
            textSize(12)
            fill('#FFF827')
            text(self.p[i]['num'],self.p[i]['x'],self.p[i]['y']-5)
            if prep.polog_Y() < 360 or prep.polog_Y() > 370:
                self.p[i]['y'] += 3
        if len(self.p) > 0:
            if self.p[0]['y'] >= 800:
                del self.p[0]
        for i in range(len(self.p)):
            if self.p[i]['y'] >= 460 and self.p[i]['y'] <= 540 and self.p[i]['x'] >= head_X - 40 and self.p[i]['x'] <= head_X + 40:
                snake.dlina(self.p[i]['num'])
                del self.p[i]
                return ' '
    def plus_ball(self):
        x = floor(random(0,1000))
        if x == 1:
            self.p.append(dict(x = random(10,590),y = -15,num = floor(random(100,1000)),gold = 1))
        else:
            self.p.append(dict(x = random(10,590),y = -15,num = floor(random(1,10)),gold = 0))
#Змейка  
class Snake:
    def __init__(self,x_,y_,d,n):
        self.d = d
        self.n = n
        self.p = []
        for i in range(n):
            self.p.append(dict(x = x_,y = y_,R = 255,G = 255,B = 255))
    def fill_(self,r,g,b):
        for i in range(len(self.p)):
            if mousePressed == 1:
                if mouseX >= 390 and mouseX <= 410 and mouseY > self.p[i]['y'] - 7 and mouseY < self.p[i]['y'] + 7:
                    self.p[i]['R'] = r
                    self.p[i]['G'] = g
                    self.p[i]['B'] = b
                    #print(self.p[len(self.p)-i-1]['y'])
                    #print(mouseY)
    def draw_(self):
        global palette
        strokeWeight(1)
        if self.n <= 40:
            for i in range(self.n):
                fill(self.p[self.n-1-i]['R'], self.p[self.n-1-i]['G'], self.p[self.n-1-i]['B'])
                circle(self.p[self.n-1-i]['x'],self.p[self.n-1-i]['y'],self.d)
        else:
            for i in range(40):
                fill(self.p[40-1-i]['R'], self.p[40-1-i]['G'], self.p[40-1-i]['B'])
                circle(self.p[40-1-i]['x'],self.p[40-1-i]['y'],self.d)
        textSize(10)
        if palette == 0 and dict_int['shop'] == False:
            text(self.n,self.p[0]['x'],self.p[0]['y']-10)
    def move_to(self,x,y):
        self.p[0]['x'] = x
        self.p[0]['y'] = y
        self.head_to_gran()
        self.move_tail()
    def move(self,dx,dy):
        self.p[0]['x'] += dx
        self.p[0]['y'] += dy
        self.head_to_gran()
        self.move_tail()
    def head_to_gran(self):
        global gran_left,gran_right
        if self.p[0]['x'] <= gran_left:
            self.p[0]['x'] = gran_left
        if self.p[0]['x'] >= gran_right:
            self.p[0]['x'] = gran_right
    def dlina(self,d):
        self.n += d
        if d > 0:
            for i in range(d):
                self.p.append(dict(x = 300,y = 1000,R = 255,G = 255,B = 255))
    def dlina_to(self,d):
        self.n = d
    def move_tail(self):
        for i in range(1,self.n):
            dx = self.p[i]['x'] - self.p[i-1]['x']
            dy = self.p[i]['y'] - self.p[i-1]['y']
            d = sqrt(dx**2 + dy**2)
            if self.d < d:
                self.p[i]['x'] = (self.d / d) * (self.p[i]['x'] - self.p[i-1]['x']) + self.p[i-1]['x']
                self.p[i]['y'] = (self.d / d) * (self.p[i]['y'] - self.p[i-1]['y']) + self.p[i-1]['y']
    def scroll_tail_Y(self,dy):
        for i in range(1,self.n):
            self.p[i]['y'] += dy
    def get_n(self):
        return self.n
    def head_X(self):
        return self.p[0]['x']
#Препятствия
class Prep:
    def __init__(self):
        self.del_index = 5
        self.prep = []
        self.graniza = 0
    def recovery_prep(self):
        global score
        self.del_index = 5
        self.prep = []
        for i in range(5):
            self.prep.append(dict(x = 120*i,y = -120,num = floor(random(3,50))))            
    def move_prep(self,get_n,head):
        global gran_left,gran_right,score
        if self.prep[0]['y'] > 380 and self.prep[0]['y'] < 530 and self.del_index < 5:
            gran_left = self.prep[self.del_index]['x']
            gran_right = self.prep[self.del_index]['x'] + 120
        else:
            gran_left = 0
            gran_right = 600
        strokeWeight(10)
        if self.del_index == 5:
            for i in range(len(self.prep)):
                if self.prep[i]['y'] < 365:
                    self.prep[i]['y'] += 3
                else:
                    if get_n > 0 and self.prep[i]['x'] <= head and self.prep[i]['x'] + 120 >= head:
                        self.prep[i]['num'] -= 1
                        dict_int['score'] += 1
                        snake.dlina(-1)
                if self.prep[i]['num'] > 0 and i != self.del_index:
                    fill("#34FFFD")
                    rect(self.prep[i]['x'],self.prep[i]['y'],120,120)
                    fill(0)
                    text(self.prep[i]['num'],self.prep[i]['x']+60,self.prep[i]['y']+60)
                else:
                    self.del_index = i
                    #del self.prep[i]
        else:
            for i in range(len(self.prep)):
                self.prep[i]['y'] += 3
                if self.prep[i]['num'] > 0:
                    fill("#34FFFD")
                    rect(self.prep[i]['x'],self.prep[i]['y'],120,120)
                    fill(0)
                    text(self.prep[i]['num'],self.prep[i]['x']+60,self.prep[i]['y']+60)
            if self.prep[0]['y'] >= 800:
                self.recovery_prep()
        if snake.get_n() <= 0:
            for i in range(len(self.prep)):
                self.del_index = i  
    def polog_Y(self):
        return self.prep[0]['y']
start = 0
snake = Snake(300,600,15,40)
prep = Prep()
background_ = [0,0,0]
ball = Ball()
i = 1
#wall = Wall()
palette = 0
Button_palette = button_palette()
shop = button_shop()
def setup():
    global immage
    immage = loadImage("fon2.png")
    size(600,800)
    background(255)
    textSize(20)
    textAlign(CENTER, BOTTOM)
def draw():
    global start,immage,background_,i,palette
    background(background_[0],background_[1],background_[2])
    image(immage,0,0,600,800)
    fill(255)
    textSize(25)
    text('money:',300,25)
    text(dict_int['score'],300,50)
    if start == 1:
        ball.draw_ball(snake.head_X())
        #wall.draw_wall(snake.head_X())
        snake.draw_()
        snake.scroll_tail_Y(3)
        snake.move_to(mouseX,500)
        textSize(20)
        prep.move_prep(snake.get_n(),snake.head_X())
        fill(255-background_[0],255-background_[1],255-background_[2])
        if i % 100 == 0:
            ball.plus_ball()
        #if i % 100 == 0:
            #wall.plus_wall()
        i += 1
    else:
        i = 1
    if snake.get_n() <= 0:
        start = 0
    if start == 0 and palette == 0 and dict_int['shop'] == False:
        button()
    if palette == 1 or dict_int['shop'] == True:
        fill(255,0,0)
        strokeWeight(1)
        rect(500,0,100,60)
        fill(0)
        textSize(20)
        text('BACK',550,40)
        if palette == 1:
            Button_palette.palette()
        else:
            shop.draw_()
def mousePressed():
    global start,palette
    if start == 0 and mouseX > 200 and mouseX < 400 and mouseY > 400 - 62.5 and mouseY < 400 + 62.5 and palette == 0:
        button_start()
    if start == 0 and mouseX > 500 and mouseX < 600 and mouseY > 0 and mouseY < 60 and dict_int['shop'] == True:
        snake.dlina_to(40)
        dict_int['shop'] = False
    if start == 0 and mouseX > 500 and mouseX < 575 and mouseY > 700 and mouseY < 775 and dict_int['shop'] == False:
        dict_int['shop'] = True
        shop.draw_()
        snake.dlina_to(20)
    if start == 0 and mouseX > 25 and mouseX < 100 and mouseY > 700 and mouseY < 775:
        palette = 1
        snake.dlina_to(40)
    if start == 0 and mouseX > 500 and mouseX < 600 and mouseY > 0 and mouseY < 60 and palette == 1:
        palette = 0
        snake.dlina_to(40)
