import traceback

try:
    const = 10 / 0
except ZeroDivisionError:                        #에러이름이 틀려도 에러 발생함.  #알맞은 예외처리가 아닌 메모리에러 처리로 된다면, 프로그램이 중단되고 ZeroDivisionError가 발생 함.
    print("0으로 나눌 수 없습니다.")
except MemoryError:                              #try안의 실행문이 memory에러에 해당되지 않으므로 메모리에러 처리되지 않음.
    print("메모리 에러입니다.")

print("프로그램이 중단되지 않고 여기까지 실행됨.")      #예외처리를 안하고 try문만 작성시 문법 에러 발생.

try:
    const = 10 / 0
except Exception:                                #모든 예외를 처리할 수 있음. 예외들이 객체이고, Exception이 모든 예외의 부모이기 때문에 다른 예외들 대신 처리 가능.
    print("예외가 발생했습니다.")                    #하지만 무슨 예외가 발생했는지 알수 없음.

print("프로그램이 중단되지 않고 여기까지 실행됨.")

try:
    b = 20
    a - b
except Exception as e:                           #발생한 예외를 as를 통해 변수에 할당해 처리해주고 출력해서 어떤 예외가 발생했는지 확인 가능.
    print("예외가 발생했습니다.")
    print(e)
    print(traceback.format_exc())                #traceback을 이용하면 어떤 코드에서 에러가 났는지 알려준다.

print("프로그램이 중단되지 않고 여기까지 실행됨.")

try:
    const = 10
    const += 1
    print(const)
except Exception as e:
    print("예외가 발생했습니다.")
    print(e)
    print(traceback.format_exc())
else:                                           #try문에서 에러가 발생하지 않으면 except문은 실행되지 않고, else문이 실행되어 try문이 종료됨.
    print("정상 종료")
finally:                                        #에러가 발생하더라도 finally구문은 항상 실행 된다.
    print("예외발생 여부와 상관없이 항상 실행")