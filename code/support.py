from os import walk
import pygame


def import_forder(path):
    surface_list = []
    for _, __, img_files in walk(path):  # 返回的是(dirpath, dirnames, filenames)三元组
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
