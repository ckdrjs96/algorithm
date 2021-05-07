def solution(routes):
    routes.sort(key=lambda x:x[0])

    cnt=1
    cam_inn=-30001
    cam_out=30001
    for inn,out in routes:
        #카메라 위치에서 벗어나면 새로운 카메라 추가
        if cam_out < inn:
            cnt+=1
            cam_inn,cam_out=inn,out
        #카메라 공통구간만들기
        else:
            cam_inn=max(cam_inn,inn)
            cam_out=min(cam_out,out)

    return cnt