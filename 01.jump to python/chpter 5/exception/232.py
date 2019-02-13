class Bird:
    def fly(self):
        print("good")
        # raise NotImplementedError 예외를 발생시키는 문장 (raise)


class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()