#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 08:18:30 2021

@author: toku
"""

def nQueens(size):
    # board = [-1] * size
    board = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]
    rQueens(board, 0, size)
    print (board)
    disp_board(board)
    

def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


def rQueens(board, current, size):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
        return False

def disp_board(board):
    loc_dot, loc_q = '. ', 'Q '
    b_len = len(board)
    for i in range(b_len):
        loc_line = ''
        bq = board[i]
        loc_line = loc_line + loc_dot * bq + loc_q + loc_dot * \
            (b_len - bq - 1)
        print(loc_line)
        
            
nQueens(10)

