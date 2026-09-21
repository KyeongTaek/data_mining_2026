"""
03. 자료형과 연산자
7) 파이썬의 기본 복사 방식
"""

# Python에서 객체를 복사하는 기본 방식은 Call by reference이다.
# 변수를 다른 변수에 할 당시, 동일한 객체에 대한 참조(reference)를 전달하여, 두 변수가 같은 메모리 위치를 가리키게 되는 것이다.
                                                    #            PM
# 리스트 객체                                        #          |      |
original = [1, 2, 3]                                # ori --> |  1   | [0]
                                                    #         |  2   | [1]
                                                    #         |  3   | [2]

                                                    #            PM
# 참조 복사: original을 copied에 할당                 #          |      |
copied = original                                   # ori --> |  1   | [0]
                                                    #      |  |  2   | [1]
                                                    # cop --  |  3   | [2]

                                                    #            PM
# original의 값을 수정                                #          |      |
original[0] = 100                                   # ori --> |  100 | [0]
                                                    #      |  |  2   | [1]
                                                    # cop --  |  3   | [2]       

                                                    #            PM
# original과 copied 모두 변경된 값을 참조              #          |      |
print("Original: ", original)                       # ori --> |  100 | [0]
print("Copied: ", copied)                           #      |  |  2   | [1]
                                                    # cop --  |  3   | [2]


# 얕은 복사(Shallow Copy): 객체 자체만 복사하고, 객체가 참조하는 하위 객체(내부 리스트나 딕셔너리 등)는 원본 객체의 것을 참조
# 깊은 복사(Deep Copy): 객체와 그 객체가 참조하는 모든 하위 객체까지 모두 복사하여 완전히 독립적인 객체를 생성

import copy

# 원본 객체
original = [[1, 2, 3], [4, 5, 6]]

# 얕은 복사
shallow_copy = copy.copy(original)

# 깊은 복사
deep_copy = copy.deepcopy(original)

# 원본의 하위 객체 수정 테스트
original[0][0] = 100
print("Original:", original)
print("Shallow Copy:", shallow_copy) # 얕은 복사 --> 영향을 받음
print("Deep Copy:", deep_copy) # 깊은 복사 --> 영향을 받지 않음
