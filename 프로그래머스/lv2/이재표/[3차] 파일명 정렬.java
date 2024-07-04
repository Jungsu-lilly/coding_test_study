import java.util.*;
class Solution {
    public String[] solution(String[] files) {
        String[] answer = {};
        
        Arrays.sort(files,new Comparator<String>(){
            @Override
            public int compare(String s1,String s2){
                int i1=splitHeader(s1);
                int i2=splitHeader(s2);
                int comHead=s1.substring(0,i1).toUpperCase().compareTo(s2.substring(0,i2).toUpperCase());
                System.out.println("s1 :"+s1.substring(0,i1).toUpperCase());
                System.out.println("s2 : "+s2.substring(0,i2).toUpperCase());
                System.out.println("===");
                if(comHead<0){
                    return -1;
                }else if(comHead>0){
                    return 1;
                }else{
                    int numi1=splitNumber(s1,i1);
                    int numi2=splitNumber(s2,i2);

                    String num1=s1.substring(i1,numi1);
                    String num2=s2.substring(i2,numi2);
                    
                    Integer n1=Integer.valueOf(num1);  
                    Integer n2=Integer.valueOf(num2);
                    if(n1<n2){
                        return -1;
                    }else if(n1>n2){
                        return 1;
                    }else{
                        return 0;
                    }
                }
            }
        });
        return files;
    }
    public int splitHeader(String s){
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)>='0' && s.charAt(i)<='9'){
                return i;
            }
        }
        return s.length();
    }
    public int splitNumber(String s,int header){
        for(int i=header;i<s.length();i++){
            if(!(s.charAt(i)>='0'&&s.charAt(i)<='9')){
                return i;
            }
        }
        return s.length();
    }
}
