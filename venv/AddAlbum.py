from RootClass import Root
from Album import Album
import copy
import pygame
from Item import Item
import os
import pickle


class AddAlbum:
   Flag = False
   Write = False
   Name = None

   def print_addition_menu(self, screen):
       background_image = pygame.image.load('Backgrounds/index.jpg').convert_alpha()
       background_image = pygame.transform.scale(background_image, (1000, 600))
       font = pygame.font.SysFont('arial', 20)  # name caption
       loading_caption = font.render("Creating new album", False, (0, 0, 0))
       screen.blit(background_image, (0, 0))
       screen.blit(loading_caption, (380, 10))
       font = pygame.font.SysFont('arial', 15)
       button = pygame.image.load("Backgrounds/plate.png")
       font = pygame.font.SysFont('arial', 20)
       button = pygame.transform.scale(button, (100, 40))
       loading_caption = font.render("Create", False, (0, 0, 0))  # grouping in albums
       screen.blit(loading_caption, (520, 510))
       loading_caption = font.render("Cancel", False, (0, 0, 0))  # grouping in albums
       screen.blit(loading_caption, (370, 510))
       screen.blit(button, (500, 500))
       screen.blit(button, (350, 500))
       button = pygame.transform.scale(button, (600, 70))
       screen.blit(button, (200, 230))
       font = pygame.font.SysFont('arial', 25)
       loading_caption = font.render(self.Name, False, (0, 0, 0))  # grouping in albums
       screen.blit(loading_caption, (300, 250))

   def run_adding(self, root, screen):
       self.Name = ""
       self.print_addition_menu(screen)
       while True:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   with open('data.pickle', 'wb') as f:
                       pickle.dump(root, f)
                   raise SystemExit
               if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                       if self.search_events(event.pos, screen, root):
                           return True
               if event.type == pygame.KEYDOWN and self.Write:
                   if event.key == pygame.K_BACKSPACE and len(self.Name) > 0:
                       self.Name = self.Name[:len(self.Name) - 1]
                   else:
                       self.Name += chr(event.key)
                   self.print_addition_menu(screen)
           pygame.display.update()

   def search_events(self, pos, screen, root):
       x, y = pos
       if 200 < x < 800:
           if 230 < y < 300:
               if not self.Write:
                   self.Write = True
       if 500 < y < 540:
           if 500 < x < 600:
               if root.get_current_album(False) is not None:
                   if len(self.Name) == 0:
                       self.Name = "default"
                   newa = Album(self.Name, root.get_current_album(False).Name)
                   newa.Index = 0
                   root.get_current_album(False).add_item(newa)
               return True
           if 350 < x < 450:
               return True
       return False


