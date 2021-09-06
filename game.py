import pygame as pg

from random import randrange

TAMANNO = (800, 600)

class Bola():
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        
        self.derecha = True
        self.arriba = True
    

        self.incremento_x = 5
        self.incremento_y = 5

        
    
    def actualizate(self):
        if self.derecha:
            self.x += 5
        else: 
            self.x -= 5
        
        if self.x + self.w >= TAMANNO[0]:
            self.derecha = False
            
        if self.x <= 0:
            self.derecha = True
            
        if self.arriba:
            self.y -= 5
        else: 
            self.y += 5
        
        if self.y + self.h >= TAMANNO[1]:
            self.arriba = True
            
        if self.y <= 0:
            self.arriba = False
    '''
        if self.x + self.w > TAMANNO[0] and self.x < 0:
            self.incremento_x *= 1
        if self.y + self.h > TAMANNO[1] or self.y < 0:
            self.incremento_y *= 1
    '''
        #print ("X - position: {} derecha: {}".format(self.x, self.derecha))       
        
class Game():

    def __init__(self):
        self.pantalla = pg.display.set_mode(TAMANNO)
        self.reloj = pg.time.Clock()
        self.bolas = []
        for i in range (10):
            tamanyo = randrange(10, 41)
            bola = Bola(randrange(0, TAMANNO[0]),
                             randrange(0, TAMANNO[1]),
                             tamanyo,
                             tamanyo,
                             (randrange(256), randrange(256), randrange(256)))
            
            bola.derecha = randrange(2) == 1
            bola.arriba = randrange(2) == 1
            
            self.bolas.append(bola)
        
    def bucle_principal(self):
        game_over = False
        pg.init()
        
        while not game_over:
            self.reloj.tick(60)
            
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
                    
            for i in range(len(self.bolas)):
                self.bolas[i].actualizate()      
                    
            self.pantalla.fill((0, 0, 0))
            for bola in self.bolas:
                pg.draw.rect(self.pantalla, bola.color,
                             pg.Rect(bola.x, bola.y, bola.w, bola.h))

            pg.display.flip()
            
        pg.quit()    

if __name__ == '__main__':
    juego = Game()
    juego.bucle_principal()

print (__name__)