import java.util.*;
class Solution {
    int answer = -1;
    public int solution(String[] board) {
        int o=0;
        int x=0;
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[i].length();j++){
                if(board[i].charAt(j)=='O'){
                    o++;    
                }else if(board[i].charAt(j)=='X'){
                    x++;
                }
                
            }
        }
        
        System.out.println(o);
        System.out.println(x);
        System.out.println(isGameWin(board,'O'));
        
        
        if(o<x){
            return 0;
        }
        if(o-x>=2){
            return 0;
        }
        if(isGameWin(board,'O') && o<=x){
            return 0;
        }
        if(isGameWin(board,'X')&&o!=x){
            return 0;
        }
        return 1;
    }
    public boolean isGameWin(String[] board,char sign){
        if(board[0].charAt(0)==sign&&board[0].charAt(1)==sign&&board[0].charAt(2)==sign){
            return true;
        }
        else if(board[1].charAt(0)==sign&&board[1].charAt(1)==sign&&board[1].charAt(2)==sign){
            return true;
        }
        else if(board[2].charAt(0)==sign&&board[2].charAt(1)==sign&&board[2].charAt(2)==sign){
            return true;
        }
        else if(board[0].charAt(0)==sign&&board[1].charAt(0)==sign&&board[2].charAt(0)==sign){
            return true;
        }
        else if(board[0].charAt(1)==sign&&board[1].charAt(1)==sign&&board[2].charAt(1)==sign){
            return true;
        }
        else if(board[0].charAt(2)==sign&&board[1].charAt(2)==sign&&board[2].charAt(2)==sign){
            return true;
        }
        else if(board[0].charAt(0)==sign&&board[1].charAt(1)==sign&&board[2].charAt(2)==sign){
            return true;
        }
        else if(board[0].charAt(2)==sign&&board[1].charAt(1)==sign&&board[2].charAt(0)==sign){
            return true;
        }
        return false;
    }
}
