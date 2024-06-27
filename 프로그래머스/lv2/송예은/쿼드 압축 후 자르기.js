// 재귀 방식으로 접근 
// 내부 값이 모두 같다면 하나로 해당 칸을 [true,압축된 값]으로 변경함
// 그렇지 않다면 4개의 균일한 정사각형 영역으로.. 
// 구현 다 못함

function isSame(arr){
  if (arr[0][0] == 0){
      for (const i of arr){
          const sum = i.reduce((acc,value)=>{
              return acc+value
          },0)
          if (sum != 0){
              return false;
          }
      }
  }else{
      for (const i of arr){
          const sum = i.reduce((acc,value)=>{
              return acc+value
          },0)
          if (sum != i.length){
              return false;
          }
      }
  }return true;
}

function split(arr){
  const topleftArr= arr.slice(0,arr.length/2)
      const bottomleftArr = arr.slice(arr.length/2)
      const toprightArr = []
      const bottomrightArr = []
      
      for (let i=0;i<topleftArr.length;i++){
          toprightArr.push(topleftArr[i].slice(topleftArr[i].length/2));
          topleftArr[i] = topleftArr[i].slice(0,topleftArr[i].length/2);
      }
      for (let i=0;i<bottomleftArr.length;i++){
          bottomrightArr.push(bottomleftArr[i].slice(bottomleftArr[i].length/2));
          bottomleftArr[i] = bottomleftArr[i].slice(0,bottomleftArr[i].length/2);
      }
  return [topleftArr,toprightArr,bottomleftArr,bottomrightArr]
}

function solution(arr) {
  if (arr.length < 2){
      return arr        
  }
  if (isSame(arr)){
      for (let i=0;i<arr.length;i++){
          for (let j=0;j<i.length;j++){
              arr[i][j] = true
          }
      }
  }else{
      for (const i of split(arr)){
          solution(i)
      }
  }
}
