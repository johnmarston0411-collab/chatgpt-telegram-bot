// game.hpp
#ifndef GAME_HPP
#define GAME_HPP

#include <iostream>
#include <vector>

class TicTacToe {
private:
    std::vector<char> board;
    char currentPlayer;

public:
    TicTacToe();
    void displayBoard();
    bool makeMove(int position);
    bool checkWin();
    bool checkDraw();
    void switchPlayer();
    char getCurrentPlayer();
};

#endif // GAME_HPP
