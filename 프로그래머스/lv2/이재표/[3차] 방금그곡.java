import java.util.*;
class Solution {
    public String solution(String m, String[] musicinfos) {
        int n=musicinfos.length;
        String[]compare=new String[n];
        String answer="(None)";
        Integer mtime=-1;
        m=convert(m);
        System.out.println(m);
        for(int i=0;i<n;i++){
            String[]info=musicinfos[i].split(",");
            char[] music=convert(info[3]).toCharArray();
            
            Integer time=convertTime(info[0],info[1]);
            
            String full="";
            for(int j=0;j<time;j++){
                full+=music[j%(music.length)];
            }
            compare[i]=String.valueOf(full);
            if(compare[i].contains(m)){
                if(time>mtime){
                    answer=info[2];
                    mtime=time;
                }
            }
        }
        return answer;
    }
    
    public Integer convertTime(String start,String end){
        String[]endarr=end.split(":");
        String[]startarr=start.split(":");
        return (Integer.valueOf(endarr[0])-Integer.valueOf(startarr[0]))*60+(Integer.valueOf(endarr[1])-Integer.valueOf(startarr[1]));
    }
    
    public String convert(String name){
        String answer="";
        char[]charname=name.toCharArray();
        Map<Character,Character>map=new HashMap<>();
        map.put('C','Q');
        map.put('D','W');
        map.put('F','P');
        map.put('G','R');
        map.put('A','T');
        for(int i=0;i<charname.length;i++){
            if (i < charname.length - 1 && charname[i + 1] == '#'){
                answer+=map.get(charname[i]);
                i+=1;
            }else{
                answer+=charname[i];
            }
        }
        return answer;
    }
}
