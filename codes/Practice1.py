def largest(list):
    answer=[]
    for i in list:
        if len(i)>=0 and len(i)<=5:
            answer.append(i)
    return answer[0]
largest(['Apple','Hello','Jules'])