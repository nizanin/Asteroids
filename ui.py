import csv
from constants import SCORE_FILE
from leaderboard import load_scores
import pygame

def enter_name(screen, font):
    name = ""
    while True:
        screen.fill((0,0,0))
        text = font.render("Enter your nickname:", True, (255,255,255))
        name_text = font.render(name, True, (255,255,0))

        screen.blit(text,(300,300))
        screen.blit(name_text,(300,350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 12:
                        name += event.unicode


def show_leaderboard(screen, font):
    scores = load_scores()
    while True:
        screen.fill((0,0,0))
        title = font.render("LEADERBOARD", True, (255,255,255))
        screen.blit(title,(350,150))

        # Tytuł
        title = font.render("LEADERBOARD", True, (255, 255, 255))
        screen.blit(title, (350, 150))

        col_rank_x = 100
        col_date_x = col_rank_x + 100
        col_name_x = col_date_x + 400
        col_score_x = col_name_x + 250
        col_time_x = col_score_x + 150

        # nagłówek
        header_rank = font.render("Rank", True, (200,200,200))
        header_date = font.render("Date/Time", True, (200,200,200))
        header_name = font.render("Name", True, (200,200,200))
        header_score = font.render("Score", True, (200,200,200))
        header_time = font.render("Time(s)", True, (200,200,200))

        screen.blit(header_rank, (col_rank_x, 200))
        screen.blit(header_date, (col_date_x, 200))
        screen.blit(header_name, (col_name_x, 200))
        screen.blit(header_score, (col_score_x, 200))
        screen.blit(header_time, (col_time_x, 200))

        # dane
        y = 250
        for i, score in enumerate(scores[:10]):
            timestamp, name, points, game_time = score
            screen.blit(font.render(str(i+1), True, (255,255,255)), (col_rank_x, y))
            screen.blit(font.render(timestamp, True, (255,255,255)), (col_date_x, y))
            screen.blit(font.render(name, True, (255,255,255)), (col_name_x, y))
            screen.blit(font.render(str(points), True, (255,255,255)), (col_score_x, y))
            screen.blit(font.render(f"{game_time:.1f}s", True, (255,255,255)), (col_time_x, y))
            y += 30

        # Informacja o kontynuowaniu
        continue_text = font.render("Press any key to continue", True, (200,200,200))
        screen.blit(continue_text,(300,600))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return
            
def end_menu(screen, font):
    while True:
        screen.fill((0,0,0))
        text1 = font.render("ENTER - New Game", True, (255,255,255))
        text2 = font.render("ESC - Quit", True, (255,255,255))
        screen.blit(text1,(320,320))
        screen.blit(text2,(320,380))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "restart"
                if event.key == pygame.K_ESCAPE:
                    return "quit"