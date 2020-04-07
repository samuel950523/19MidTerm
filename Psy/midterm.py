import random
from collections import deque

# 측정법의 장.단점 비교 #"
q1 = deque()
q1 = [
    ["자기보고 측정의 장점", "비용이 적게 들고 데이터를 빠르게 모을 수 있다."],
    ["질문지 / 설문조사의 장점", "제한된 시간에 많은 정보 수집 가능"],
    ["질문지 / 설문조사의 단점", "언어적 능력 필요, 부정확 반응 수집 가능"],
    ["면접의 단점", "언어적 능력 필요 / 편향된 반응 통제 어려움"],
    ["행동적 측정 - 자연 관찰의 장점", "영유아 연구에 쉽게 적용가능"],
    ["행동적 측정 - 자연 관찰의 단점", "관찰자 효과 / 이례적이나 바람직하지 못한 행동 관찰 어려움.\n현실적으로 시간과 비용이 너무 많이 든다.\n알려주고 찍기 때문에 완전 자연스럽기는 어렵다."],
    ["행동적 측정 - 구조화된 관찰의 장점", "자연 환경에서 쉽게 일어나지 않는 사건 관찰에 유용"],
    ["행동적 측정 - 구조화된 관찰의 단점", "생태학적 타당성의 제한"],
    ["생리적 측정의 장점", "어떤 측정보다 피험자의 정직한 측정을 할 수 있다."],
    ["생리적 측정의 단점", "but 피험자들이 잘 참여를 안 하려고 함"]
]
l1 = len(q1)

# 변인 #
q2 = deque()
q2 = [
    ["독립 변인", "연구자가 조작하는 변인(원인으로 작용)"],
    ["종속 변인", "그 값이 독립 변인의 값에 좌우되는 변인(효과를 반영)"],
    ["매개 변인", "독립 변인의 작용을 종속 변인에 전달하는 역할을 담당하는 변인"]
]
l2 = len(q2)

# 이론 vs 가설 vs 연구와 관찰 #
q3 = deque()
q3 = [
    ["이론", "현상 또는 현상의 집합을 설명하는 개념들의 조직"],
    ["이론", "예) 낮은 자존감은 우울을 유발한다"],
    ["가설", "원인과 결과 사이의 잠정적, 검증가능한 진술"],
    ["가설", "예) 낮은 자존감을 가진 사람은 우울 척도에서 높은 점수를 보인다."],
    ["연구와 관찰", "한 검사에서 낮은 점수는 다른 검사에서 높은 점수를 예측하는지를 살펴본다."],
    ["연구와 관찰", "예) 자존감과 우울 검사 실시"]
]
l3 = len(q3)

# 관찰자 편향 #
q4 = deque()
q4 = [
    ["관찰자 편향", "개인적 동기와 관찰자의 기대에 기인한 오류"],
    ["표준화", "자료 수집의 전 단계에서 동일하고 일관된 절차를 적용"],
    ["조작화", "관심을 두는 개념들의 의미를 표준화 하는 것"],
    ["조작적 정의", "연구자가 관심을 가지는 변인은 모두 조작적으로 정의되어야 함"]
]
l4 = len(q4)

# 실험법 #
q5 = deque()
q5 = [
    ["실험법의 절차", "피험자의 환경 중 일부를 조작하고 조작된 환경이 피험자의 행동에 미친 영향을 측정"],
    ["실험법의 강점", "변인들 간의 인과관계 결정 가능"],
    ["실험법의 제한점",
        "인위적 실험실 상황에서 얻어진 결과의 일반화에 제약\n실험이 불가능한 연구 주제들이 많다. (ex. 어린시절의 경험과 성인 시절의 관계, 영양소 결핍과 뇌 발달)"],
    ["생태학적 타당도", "특정한 상태와 세팅에서 일어나는 것들은 실생활에서 반영하기 어렵다."]
]
l5 = len(q5)

# 실험법 변인의 구분 #
q6 = deque()
q6 = [
    ["독립변인", "실험집단(TV 폭력물 시청) vs 통제집단(TV 폭력물 무시청)"],
    ["종속변인", "아동들의 공격행동 표출정도"]
]
l6 = len(q6)

# 혼입 변인 #
q7 = deque()
q7 = [
    ["기대효과", "관찰자들이 참가자에게 기대하는 행동을 유도하기 위해 참가자가 모르게 미묘하게 의사소통하기 때문에 나타나는 계획된 반응\nex) 기대격려 -> 기대에 부응하려 노력 -> 실제로 그렇게 됨"],
    ["위약효과", "실험조작이 전혀 없었는데 실험 참가자의 행동에 변화가 나타나는 현상"]
]
l7 = len(q7)

# 혼입 변인의 교정법 #
q8 = deque()
q8 = [
    ["이중 맹목 통제", "실험보조자와 참가자 모두 연구 목적을 모르고, 처치 내용을 모르도록 하여 편향을 제거하는 절차"],
    ["위약 통제", "실험 처치가 이루어지지 않는 실험 집단을 연구 절차에 포함시키는 절차 (가짜약을 먹는 집단을 둠)"],
    ["무선 할당", "연구 참여자들 사이에 개인적 차이와 관련된 혼입 변인을 가능한 제거하고자 하는 절차"]
]
l8 = len(q8)

# 실험 설계의 유형 #
q9 = deque()
q9 = [
    ["피험자간 설계", "참가자들을 실험조건 또는 통제조건으로 무선 할당하는 연구 설계\n-> 피험자들은 진짜 약만 먹거나, 가짜 약만 먹게됨"],
    ["피험자내 설계", "참가자 각자에게 처치를 하기 전 후의 행동을 비교하는 방법\n-> 다 동일한 처치를 받게 됨. subject 간 동일.\nex) program 측정. 왕따 추방 프로그램. 공격성 이타성을 프로그램 전후에 check"]
]
l9 = len(q9)

# 상관 연구 #
q10 = deque()
q10 = [
    ["절차", "관심 있는 두 개 이상의 변인들의 의미 있는 관련성 파악이 목적\n연구자의 개입 없이 두 개 이상의 변인에 대한 정보 수집"],
    ["강점", "자연스런 환경 속 변인들 간 관계의 강도와 방향에 대한 평가 가능"],
    ["제한점", "변인들 간의 인과관계 결정 불가"],
    ["인과성에 관하여 설명", "인과성은 전혀 결정 불가하다. but 두가지 이상의 변인들이 관련이 있다 만 파악해도 좋음.\n관계의 정보와 관계의 방향에 대한 평가 가능\n정적인 방향 : a가 증가하면 b도 증가\n부적 상관 : a가 증가하면 b는 감소"],
    ["상관계수", "절댓값이 1에 가까울수록 더 관계. (+는 정적, -는 부적)"]
]
l10 = len(q10)

# 상관 연구의 예 #
q11 = deque()
q11 = [
    ["상관의 관찰 : 자존감이 낮을수록 우울하다 일 때, 가능한 원인 -> 결과 set",
     "1) 낮은 자존감 -> 우울\n2) 우울 -> 낮은 자존감\n3) 고통스런 사건 또는 생물학적 요인 -> 낮은 자존감과 우울\n적절한 통제 비교를 하지 않았을 때 상관은 비논리적일수도"]
]
l11 = len(q11)

# 신뢰도 #
q12 = deque()
q12 = [
    ["신뢰도란", "평가도구에 의해 일관성 있는 점수가 나오는 정도.\n단, 측정하고자 하는 기저 개념이 변하지 않고 유지되는 범위 내에서 고려해야함"],
    ["신뢰도가 높다 란?", "동일 대상으로 측정 했을 때, 측정하는 것이 달라지지 않았을 때, 그 점수가 일정하게 나온다."],
    ["검사-재검사 신뢰도의 장점", "제작에 용이. 가장 많이 시행됨"],
    ["검사-재검사 신뢰도의 단점", "피험자 입장에서 다시 참여해야하기 때문에 이상적이지 못함.\n연습효과를 상쇄시킬 수 없다.\nretest를 시행하는 시점이 연구자들마다 주관적으로 다름."],
    ["동형검사 신뢰도란", "표면적인 내용은 다른 버전을 두 개 만들어내어서 '같은 날' 시행하는 검사. 컨텐츠는 다르지만 묻고 싶은 것은 같음"],
    ["동형검사 신뢰도의 장점", "연습효과 일어나지 않고 retest하는 시점이 당일로 같음"],
    ["동형검사 신뢰도의 단점", "제작에 어렵다"],
    ["반분 신뢰도란", "하나를 잘 만들어서 반으로 쪼갬.\nex)20문항을 10문항씩 쪼개서 A버전, B버전으로 나눔"],
    ["반분 신뢰도의 장점", "제작에 용이. 연습효과가 일어나지 않음"]
]
l12 = len(q12)


def mkq(q):
    myrand = random.randrange(0, len(q))
    print(q[myrand][0])
    print("답 : ", end='')
    input()
    print("->  " + q[myrand][1])
    print("")
    q.pop(myrand)


def mkq_reverse(q):
    myrand = random.randrange(0, len(q))
    print(q[myrand][1])
    print("답 : ", end='')
    input()
    print("->  " + q[myrand][0])
    print("")
    q.pop(myrand)


def go(q, length):
    for _ in range(length):
        mkq(q)


def go_re(q, length):
    for _ in range(length):
        mkq_reverse(q)


while(True):
    print("어떤 것을 공부하고 싶으신가요? 종료하려면 0 입력")
    print("1. 측정법의 장.단점 비교")
    print("2. 변인")
    print("3. 이론 vs 가설 vs 연구와 관찰")
    print("4. 관찰자 편향")
    print("5. 실험법")
    print("6. 실험법 변인 구분")
    print("7. 혼입 변인")
    print("8. 혼입 변인의 구분법")
    print("9. 실험 설계의 유형")
    print("10. 상관 연구")
    print("11. 상관 연구의 예")
    print("12. 신뢰도")
    c = int(input())

    if c == 1:
        go(q1, l1)
    elif c == 2:
        go_re(q2, l2)
    elif c == 3:
        go_re(q3, l3)
    elif c == 4:
        go_re(q4, l4)
    elif c == 5:
        go(q5, l5)
    elif c == 6:
        go_re(q6, l6)
    elif c == 7:
        go_re(q7, l7)
    elif c == 8:
        go_re(q8, l8)
    elif c == 9:
        go_re(q9, l9)
    elif c == 10:
        go(q10, l10)
    elif c == 11:
        go(q11, l11)
    elif c == 12:
        go(q12, l12)
    else:
        break