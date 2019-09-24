// 既存の iOS コードをいじる以外では初めて Swift を書いた。
// AtCoder の Swift は古いので全然出てこない。
// 文字列の扱いの面倒くささで嫌気が差した。
let S  = readLine()!
let C = Array(S.characters)

var count = [Character: Int]()

for c in C{
  if (count[c] == nil){
    count[c] = 1
  }
  else{
    if let a = count[c]{
    	count[c] = a + 1
    }
  }
}

var ans = "Yes"
for i in count.values {
  if i != 2 {
    ans = "No"
  }
}

if count.count != 2 {
  ans = "No"
}

print(ans)
