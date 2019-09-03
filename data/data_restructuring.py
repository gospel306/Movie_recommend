#파일 생성
moviedata = open("C:\\Users\\multicampus\\Desktop\\bigdataSub2\\bigdata-sub2\\data\\movies.dat", 'r', encoding='UTF8')
inputdata = open("movieParsing.dat",'w')

#첫 줄은 항목 쓰기
inputdata.write("MovieID,Action,Adventure,Animation,Children's,Comedy,Crime,Documentary,Drama,Fantasy,Film-Noir,Horror,Musical,Mystery,Romance,Sci-Fi,Thriller,War,Western\n")

#파싱해서 넣어주기
genreAll = ["Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]

lines = moviedata.readlines()
for line in lines:
    tmpArr = line.split("::")
    genreArr = tmpArr[2][:-1].split("|")

    inputStr = tmpArr[0]
    
    idx = 0
    for genre in genreAll:
        if idx < len(genreArr) and genre == genreArr[idx]:
            inputStr += ",1"
            idx += 1
        else:
            inputStr += ",0"
    
    inputStr += "\n"
    inputdata.write(inputStr)

inputdata.close()
moviedata.close()