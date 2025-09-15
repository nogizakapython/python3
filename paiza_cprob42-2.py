A, B = map(int, input().split())

match A:
    case A if  A > B:
        print(1)
    case A if  A == B:
        print(0)
    case A if A < B:
        print(-1)
