f = open('c:/test/abc.txt', 'w')            #test라는 폴더를 만들고, abc파일은 만들어놓지 않아도 코드를 실행시키면 자동으로 생성된다.
for i in range(1, 8):
    f.write('%d번째\n'%i)
f.close()                                   #close를 해줘야 파일 실행이 정상적으로 멈춘다.

f = open('c:/test/abc.txt', 'r')
m = f.readlines()                           #파일의 전체 내용을 읽는 메소드, 한줄만 읽을 때는 readline메소드를 사용.
f.close()

for i in m:
    print(i, end="")                        #end연산자는 줄바꿈을 하지않게 해줌.