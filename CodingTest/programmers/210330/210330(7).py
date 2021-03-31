def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")
    answer = ""
    for runner in range(len(completion)):
        if participant[runner] != completion[runner]:
            answer = participant[runner]
            print(answer)
            break
        else:
            continue
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))