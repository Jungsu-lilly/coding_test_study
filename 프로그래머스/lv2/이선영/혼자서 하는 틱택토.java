class Solution {
    public int solution(String[] board) {
        int[][] dr = {{0,0,0},{1,1,1},{2,2,2},{0,1,2},{0,1,2},
                      {0,1,2},{0,1,2},{0,1,2}};
        int[][] dc = {{0,1,2},{0,1,2},{0,1,2},{0,0,0},{1,1,1},
                      {2,2,2},{0,1,2},{2,1,0}};
        
        int answer = 0;
        char[][] map = new char[3][3];
        int Ocnt = 0, Xcnt = 0;
        
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                map[i][j] = board[i].charAt(j);
                if(map[i][j] == 'O') Ocnt++;
                else if(map[i][j] == 'X') Xcnt++;
            }
        }
        
        int oLineCnt = 0, xLineCnt = 0;
        for(int i=0; i<8; i++){
            char value = map[dr[i][0]][dc[i][0]];
            if(value == '.') continue;
            
            for(int j=0; j<3; j++){ 
                if(map[dr[i][j]][dc[i][j]] != value) break;
                if(j == 2){
                    if(map[dr[i][0]][dc[i][0]]== 'X') xLineCnt++;
                    else oLineCnt++;
                }
            }
            
           
        }
        
        if(Xcnt == 0 && Ocnt ==0) answer = 1;
        else if(Ocnt-Xcnt == 1 && xLineCnt == 0 && oLineCnt <= 2) answer = 1;
    
        else if(Xcnt == Ocnt && oLineCnt == 0 && xLineCnt  <=1) answer = 1;
        
        System.out.println("Ocnt : "+Ocnt + " Xcnt : " + Xcnt + " xline : " + xLineCnt + " oLine : " + oLineCnt);
        return answer;
    }
}
