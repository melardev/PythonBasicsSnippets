try:
    user_num = int(input('enter the denominator'))
    result = 3 / user_num
except:
    print('Exception happened')

try:
    result = 10 / user_num
    print(result)
except ZeroDivisionError as e:
    print(e)
except:
    print('another exception')

try:
    result = 10 / user_num
except Exception as e:
    # except(RuntimeError, ZeroDivisionError) as e:
    print("A ZeroDivisionError Happened")
else:
    print("Everything was ok")
finally:
    print("finishing...")

raise RuntimeError
